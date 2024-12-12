#!/usr/local/bin/python

import uuid
import datetime
import asyncio

uuid_output = str(uuid.uuid4())

async def log_output():
    while True:
        print(f'{datetime.datetime.now()}: {uuid_output}')
        await asyncio.sleep(5)

asyncio.run(log_output())
    
