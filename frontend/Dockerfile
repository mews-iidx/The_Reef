FROM python:3.9-buster
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY ./ ./

ENTRYPOINT ["uvicorn", "main:app", "--port", "3000", "--host", "0.0.0.0", "--reload"]