#!/usr/local/bin/python
"""
Read file output from log_output and return contents on / HTTP endpoint
"""

from aiohttp import web
from aiofile import async_open
import os

HOST = os.environ['HOST']
PORT = int(os.environ['PORT'])
FILE_PATH = os.environ['FILE_PATH']

async def root_handler(request):
    async with async_open(FILE_PATH, 'r') as afp:
        return web.Response(
            text=f'<html><body><h1>'
                f'{await afp.read()}'
                f'</h1></body></html>', content_type='text/html',
        )
async def on_prepare(request, response):
    response.headers['App Name'] = 'Show Output App'

app = web.Application()
app.add_routes([web.get("/", root_handler)])
app.on_response_prepare.append(on_prepare)

web.run_app(app, host=HOST, port=PORT)
