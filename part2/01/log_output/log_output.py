#!/usr/local/bin/python
"""
Log output to stdout each 5 secs and serve it as HTTP endpoint on / as well,
on HOST and PORT env vars, also read and display ping / pong value from file.
"""
import uuid
import datetime
import asyncio
from aiohttp import web, ClientSession
import os

HOST = os.environ['HOST']
PORT = int(os.environ['PORT'])
PINGPONG_URL = os.environ['PINGPONG_URL']

uuid_output = str(uuid.uuid4())

async def log_output():
    while True:
        print(f'{datetime.datetime.now()}: {uuid_output}')
        await asyncio.sleep(5)


async def root_handler(request):
    async with ClientSession() as session:
        async with session.get(PINGPONG_URL) as resp:
            count = (await resp.json())['count']

            return web.Response(
                text=f'<html><body>\n'
                    f'<h1>{datetime.datetime.now()}: {uuid_output}</h1>\n'
                    f'<h2>Ping / Pongs: {count}</h2>\n' 
                    f'</body></html>\n', content_type='text/html',
            )

async def on_prepare(request, response):
    response.headers['App-Name'] = 'Log Output App'

app = web.Application()
app.add_routes([web.get("/", root_handler)])
app.on_response_prepare.append(on_prepare)

async def serve():
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, host=HOST, port=PORT)
    await site.start()
    await asyncio.Event().wait()

async def main():
    await asyncio.gather(log_output(), serve())

asyncio.run(main())
