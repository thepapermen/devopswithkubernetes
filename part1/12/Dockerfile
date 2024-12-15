FROM sunpeek/poetry:py3.12-slim

WORKDIR /usr/src/app

COPY . .

RUN poetry install

ENV HOST=0.0.0.0
ENV PORT=8080
ENV IMAGE_LIFE_MINUTES=0.1
ENV MEDIA_ROOT=/usr/src/app/todo/todo/media/

CMD exec poetry run python ./todo/manage.py runserver ${HOST}:${PORT}
