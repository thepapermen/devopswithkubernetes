#!/usr/local/bin/python
"""
Log output to file each 5 secs using native Linux kernel asynchronous I/O
"""
import uuid
import datetime
import asyncio
from aiofile import async_open
import os


FILE_PATH = os.environ['FILE_PATH']

uuid_output = str(uuid.uuid4())

async def log_output():
   while True:
      async with async_open(FILE_PATH, 'w') as afp:
         await afp.write(f'{datetime.datetime.now()}: {uuid_output}')
      await asyncio.sleep(5)

asyncio.run(log_output())