#!/usr/local/bin/python
"""
Pingpong app with a customisable HTTP endpoint path
"""
from aiohttp import web
import os

HOST = os.environ['HOST']
PORT = int(os.environ['PORT'])
ENDPOINT_URL = os.environ['ENDPOINT_URL']

counter = 0

async def root_handler(request):
    global counter
    counter += 1
    return web.Response(
        text=f'<html><body><h1>'
            f'{counter}'
            f'</h1></body></html>', content_type='text/html',
    )
async def on_prepare(request, response):
    response.headers['App Name'] = 'Ping Pong App'

app = web.Application()
app.add_routes([web.get(ENDPOINT_URL, root_handler)])
app.on_response_prepare.append(on_prepare)

web.run_app(app, host=HOST, port=PORT)
