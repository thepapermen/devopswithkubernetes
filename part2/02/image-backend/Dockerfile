FROM python:3-alpine

WORKDIR /usr/src/app

COPY . .

RUN pip install aiohttp

ENV HOST=0.0.0.0
ENV PORT=3000
ENV URL=/image
ENV MEDIA_ROOT=/usr/src/app
ENV IMAGE_LIFE_MINUTES=60
ENV IMAGE_SOURCE_URL="https://picsum.photos/1200"

ENTRYPOINT ["./serve_image.py"]
