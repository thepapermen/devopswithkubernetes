FROM python:3-alpine

WORKDIR /usr/src/app

COPY . .

RUN pip install aiofile

# FILE_PATH var must be set for the service to properly run

ENV FILE_PATH='hello.txt'

ENTRYPOINT ["./log_output.py"]
