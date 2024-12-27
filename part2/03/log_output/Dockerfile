FROM python:3-alpine

WORKDIR /usr/src/app

COPY . .

RUN pip install aiohttp

ENV HOST=0.0.0.0
ENV PORT=3000
ENV PINGPONG_URL=http://x.x.x.x:3001/pingpong

ENTRYPOINT ["./log_output.py"]
