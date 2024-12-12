FROM python:3-alpine

WORKDIR /usr/src/app

COPY . .

RUN pip install aiohttp && pip install aiofile

# HOST, PORT and FILE_PATH vars must be set for the service to properly run

ENTRYPOINT ["./log_output.py"]
