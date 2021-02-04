import asyncio
import sys

from tornado import gen
from tornado.ioloop import IOLoop
from tornado.iostream import StreamClosedError
from tornado.tcpclient import TCPClient

from client_utils import IOThreadFailed, stringify
from input_data import InputUpdate
from update_data import UpdateData, ServerUpdate


class WebClient:
    def __init__(self, rate: int = 32):  # floating point is exact (power of 2)
        self.rate = rate

    async def loop_send(self, retry_count=0):
        if retry_count > 1:
            IOThreadFailed.put(True)
            raise IOError("Can't connect to server, retried too many times!")

        client = None
        stream = None

        async def retry():
            if stream:
                stream.close()
            if client:
                client.close()
            await self.loop_send(retry_count + 1)

        async def read():
            try:
                return await stream.read_until(b";")
            except StreamClosedError:
                print('Stream closed while trying read')
                await retry()

        async def write(to_write):
            try:
                return await stream.write(to_write)
            except StreamClosedError:
                print('Stream closed while trying write')
                await retry()

        try:
            client = TCPClient()
            stream = await client.connect(sys.argv[1], int(sys.argv[2]))
            cli_id = sys.argv[3]
            b_id = b'id:' + cli_id.encode() + b';'
            await stream.write(b_id)
        except StreamClosedError:
            print('Stream closed while trying to establish connection')
            await retry()
            return  # Never called

        while True:
            data = await read()
            print(data)
            if data == b'id;':
                await write(b_id)
                break
            elif data != b_id:
                print("Server didn't get id!")
                await retry()
            else:
                break

        ServerUpdate.put(UpdateData({}, {}))

        async def receive_update():
            while True:
                new_data = await read()
                update_data = UpdateData.from_json(new_data[:-1])
                ServerUpdate.put(update_data)

        IOLoop.current().add_callback(receive_update)
        retry_count = 0
        while True:
            timer = gen.sleep(1 / self.rate)
            data = InputUpdate.get()
            if data:
                dd = data.asdict()
                flat_data = {}
                for i in dd:
                    for j in dd[i]:
                        flat_data[j.value] = int(dd[i][j])
                data_str = stringify(flat_data)
                await write(bytes(data_str, encoding='utf-8') + b';')
            await timer

    def start_client(self):
        asyncio.set_event_loop(asyncio.new_event_loop())
        IOLoop.current().run_sync(self.loop_send)
        IOLoop.current().start()
