FROM python:3.9-buster
ENV PYTHONUNBUFFERED=1

WORKDIR /api

RUN pip install poetry

COPY pyproject.toml* poetry.lock* ./

RUN poetry install

COPY app ./app

ENTRYPOINT ["poetry", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--reload"]
