#!/usr/local/bin/python
"""
Log output to stdout each 5 secs and serve it as HTTP endpoint on / as well,
on HOST and PORT env vars, also read and display ping / pong value from file.
"""
import uuid
import datetime
import asyncio
from aiohttp import web
from aiofile import async_open
import os

HOST = os.environ['HOST']
PORT = int(os.environ['PORT'])
FILE_PATH = os.environ['FILE_PATH']

uuid_output = str(uuid.uuid4())

async def log_output():
    while True:
        print(f'{datetime.datetime.now()}: {uuid_output}')
        await asyncio.sleep(5)

async def root_handler(request):
    async with async_open(FILE_PATH, 'r') as afp:
        return web.Response(
            text=f'<html><body>'
                f'<h1>{datetime.datetime.now()}: {uuid_output}</h1>'
                f'<h2>Ping / Pongs: {await afp.read()}</h2>' 
                f'</body></html>', content_type='text/html',
        )
async def on_prepare(request, response):
    response.headers['App Name'] = 'Log Output App'

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
