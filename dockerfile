FROM python:3.13-slim AS builder

ENV PYTHONDONTWRITEBITECODE=1
ENV PYTHONUNBUFFERD=1

WORKDIR /app
COPY . /app
RUN python -m venv /venv
RUN apt-get update \
    && apt-get -y install libpq-dev gcc \
    && /venv/bin/pip install -r requirements.txt

FROM python:3.13-slim
ENV PYTHONDONTWRITEBITECODE=1
ENV PYTHONUNBUFFERD=1

WORKDIR /app
COPY . /app
COPY --from=builder /venv /venv
ENV PATH="/venv/bin:$PATH"

ENTRYPOINT [ "python", "manage.py", "runserver", "0.0.0.0:8000"]


