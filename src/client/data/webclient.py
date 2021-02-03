import asyncio
import json
import random
import sys

from tornado import gen
from tornado.ioloop import IOLoop
from tornado.iostream import StreamClosedError
from tornado.tcpclient import TCPClient

from utils import HistoricalQueue, InputUpdate, IOThreadFailed


class WebClient:
    def __init__(self, rate: int = 32):  # floating point is exact (power of 2)
        self.rate = rate

    async def loop_send(self, retry_count=0):
        if retry_count > 1:
            IOThreadFailed.put(True)
            raise IOError("Can't connect to server, retried too many times!")

        client = None
        stream = None

        try:
            client = TCPClient()
            stream = await client.connect(sys.argv[1], int(sys.argv[2]))
            cli_id = str(random.randint(0, 10))
            b_id = b'id:' + cli_id.encode() + b';'
            await stream.write(b_id)
            while True:
                data = await stream.read_until(b";", max_bytes=500)
                print(data)
                if data == b'id;':
                    await stream.write(b_id)
                    break
                elif data != b_id:
                    print("Server didn't get id!")
                    stream.close()
                    client.close()
                    await self.loop_send(retry_count + 1)
                else:
                    break

        except StreamClosedError:
            print('Stream closed while trying to send id')
            if stream:
                stream.close()
            if client:
                client.close()
            await self.loop_send(retry_count + 1)

        while True:
            timer = gen.sleep(1 / self.rate)
            try:
                data = InputUpdate.get()
                if data:
                    dd = data.asdict()
                    flat_data = {}
                    for i in dd:
                        for j in dd[i]:
                            flat_data[j.value] = int(dd[i][j])
                    data_str = ''.join(filter(lambda ch: ch not in '{}"', json.dumps(flat_data, separators=(',', ':'))))
                    print(data_str)
                    await stream.write(bytes(data_str, encoding='utf-8') + b';')
                await timer
            except StreamClosedError:
                print('Stream was closed when trying to send key press!')
                exit(1)

    def start_client(self):
        asyncio.set_event_loop(asyncio.new_event_loop())
        IOLoop.current().run_sync(self.loop_send)
        IOLoop.current().start()
