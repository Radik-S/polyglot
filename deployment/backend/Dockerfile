FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

WORKDIR /app

# Runtime + build deps for Debian slim.
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        libstdc++6 \
        libpq5 \
        build-essential \
        libpq-dev \
        rustc \
        cargo \
        pkg-config \
    && rm -rf /var/lib/apt/lists/*

COPY components/backend/requirements.txt /app/requirements.txt

RUN pip install --upgrade pip \
    && pip install -r /app/requirements.txt \
    && pip install gunicorn \
    && apt-get purge -y --auto-remove \
        build-essential \
        libpq-dev \
        rustc \
        cargo \
        pkg-config

# Copy backend code explicitly (without .env).
COPY components/backend/alembic.ini /app/alembic.ini
COPY components/backend/wsgi.py /app/wsgi.py
COPY components/backend/polyglot /app/polyglot

EXPOSE 8080

CMD ["sh", "-c", "alembic upgrade head && gunicorn --bind 0.0.0.0:8080 wsgi:app"]
