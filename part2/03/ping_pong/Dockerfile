FROM python:3-alpine

WORKDIR /usr/src/app

COPY . .

RUN pip install aiohttp

# HOST, PORT, ENDPOINT_URL vars must be set for the service to properly run

ENV HOST=0.0.0.0
ENV PORT=3000
ENV ENDPOINT_URL='/'

ENTRYPOINT ["./ping_pong.py"]
