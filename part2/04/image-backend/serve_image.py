#!/usr/local/bin/python
"""
Update image cache if old, serve image on HTTP endpoint.
"""
import os.path
import glob
import datetime
import asyncio
from aiohttp import web, ClientSession
import os

HOST = os.environ['HOST']
PORT = int(os.environ['PORT'])
URL = os.environ['URL']
MEDIA_ROOT = os.environ['MEDIA_ROOT']
IMAGE_LIFE_MINUTES = float(os.environ['IMAGE_LIFE_MINUTES'])
IMAGE_SOURCE_URL = os.environ['IMAGE_SOURCE_URL']

TIME_FORMAT = '%Y-%m-%d-%H:%M:%S.jpg'
IMAGE_PATH_GLOB = ''.join([MEDIA_ROOT, '*.jpg'])


image_path = None

async def update_image_if_old():
    now_time = datetime.datetime.now()
    images = glob.glob(IMAGE_PATH_GLOB)
    if len(images) > 0:
        image_name = os.path.basename(images[0])
        image_time = datetime.datetime.strptime(image_name, TIME_FORMAT)
        difference_in_minutes = (now_time - image_time).total_seconds() / 60
        if difference_in_minutes >= IMAGE_LIFE_MINUTES:
            await download_image(now_time)
            for image in images:
                os.remove(image)
    else:
        await download_image(now_time)

async def threaded_write(file_path, content):
    def stdlib_write(f, c):
        with open(f, 'wb') as fp:
            fp.write(c)
    await asyncio.to_thread(stdlib_write, file_path, content)

async def download_image(now_time):
    file_name = now_time.strftime(TIME_FORMAT)
    file_path = os.path.join(MEDIA_ROOT, file_name)
    global image_path
    async with ClientSession() as session:
        async with session.get(IMAGE_SOURCE_URL) as resp:
            if resp.status == 200:
                await threaded_write(file_path, await resp.read())
                image_path = file_path
            else:
                raise Exception(f'Unable to download image, got HTTP {resp.status}!')

async def image_updater():
    while True:
        await update_image_if_old()
        await asyncio.sleep(5)

async def threaded_read(file_path):
    def stdlib_read(f):
        with open(f, 'rb') as fp:
            return fp.read()
    return await asyncio.to_thread(stdlib_read, file_path)

async def root_handler(request):
        return web.Response(body=await threaded_read(image_path),
                            content_type='image/jpeg')

async def on_prepare(request, response):
    response.headers['App-Name'] = 'Image Backend App'

app = web.Application()
app.add_routes([web.get(URL, root_handler)])
app.on_response_prepare.append(on_prepare)

async def serve():
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, host=HOST, port=PORT)
    await site.start()
    await asyncio.Event().wait()

async def main():
    await asyncio.gather(image_updater(), serve())

asyncio.run(main())
