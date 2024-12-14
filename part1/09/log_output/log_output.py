#!/usr/local/bin/python
"""
Log output to stdout each 5 secs and serve it on HTTP endpoint on / as well,
on HOST and PORT env vars.
"""
import uuid
import datetime
import asyncio
from aiohttp import web
import os

uuid_output = str(uuid.uuid4())

async def log_output():
    while True:
        print(f'{datetime.datetime.now()}: {uuid_output}')
        await asyncio.sleep(5)

async def root_handler(request):
    return web.Response(
        text=f'<html><body><h1>'
            f'{datetime.datetime.now()}: {uuid_output}'
            f'</h1></body></html>', content_type='text/html',
    )
async def on_prepare(request, response):
    response.headers['App Name'] = 'Log Output App'

app = web.Application()
app.add_routes([web.get("/", root_handler)])
app.on_response_prepare.append(on_prepare)

async def serve():
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, host=os.environ['HOST'], port=int(os.environ['PORT']))
    await site.start()
    await asyncio.Event().wait()

async def main():
    await asyncio.gather(log_output(), serve())

asyncio.run(main())
