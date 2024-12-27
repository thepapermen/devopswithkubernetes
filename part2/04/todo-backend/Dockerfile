FROM ghcr.io/astral-sh/uv:python3.12-alpine

WORKDIR /usr/src/app

COPY . .

RUN uv sync --frozen

ENV HOST=0.0.0.0
ENV PORT=8080

CMD exec uv run -- ./todo/manage.py runserver ${HOST}:${PORT}
