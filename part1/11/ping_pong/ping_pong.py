#!/usr/local/bin/python
"""
Pingpong app with a customisable HTTP endpoint path and file storage for count
"""
from aiohttp import web
from aiofile import async_open
import os

HOST = os.environ['HOST']
PORT = int(os.environ['PORT'])
ENDPOINT_URL = os.environ['ENDPOINT_URL']
FILE_PATH = os.environ['FILE_PATH']


async def root_handler(request):
    async with async_open(FILE_PATH, 'r+') as afp:
        txt = await afp.read()
        count = int(txt) if txt else 0
        count += 1
        afp.seek(0)
        await afp.write(str(count))

    return web.Response(
        text=f'<html><body><h1>'
            f'{count}'
            f'</h1></body></html>', content_type='text/html',
    )

async def on_prepare(request, response):
    response.headers['App Name'] = 'Ping Pong App'

app = web.Application()
app.add_routes([web.get(ENDPOINT_URL, root_handler)])
app.on_response_prepare.append(on_prepare)

web.run_app(app, host=HOST, port=PORT)
