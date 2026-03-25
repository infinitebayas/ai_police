FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY pyproject.toml README.md LICENSE ./
COPY src ./src
COPY jurisdiction-profiles ./jurisdiction-profiles
COPY web ./web
COPY .env.example ./.env.example

RUN python -m pip install --upgrade pip && \
    python -m pip install .[api]

EXPOSE 8000

CMD ["python", "-m", "ai_police", "serve"]
