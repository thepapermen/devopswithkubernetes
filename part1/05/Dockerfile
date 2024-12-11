FROM sunpeek/poetry:py3.12-slim

WORKDIR /usr/src/app

COPY . .

RUN poetry install

# Commented out env vars to set them inside kubernetes deployment.yaml manifest instead
# ENV HOST=0.0.0.0
# ENV PORT=8080

CMD exec poetry run python ./todo/manage.py runserver ${HOST}:${PORT}
