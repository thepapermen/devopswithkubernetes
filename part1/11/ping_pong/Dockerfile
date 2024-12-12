FROM python:3-alpine

WORKDIR /usr/src/app

COPY . .

RUN pip install aiohttp && pip install aiofile

# HOST, PORT, ENDPOINT_URL and FILE_PATH vars must be set for the service to properly run

ENV HOST=0.0.0.0
ENV PORT=3000
ENV ENDPOINT_URL='/'
ENV FILE_PATH='hello.txt'

ENTRYPOINT ["./ping_pong.py"]
