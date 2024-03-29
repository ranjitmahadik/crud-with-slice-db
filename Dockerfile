FROM python:3.9-slim

WORKDIR /app

COPY ./requirements.txt ./requirements.txt

RUN pip install --no-cache-dir -r /app/requirements.txt

COPY . /app

EXPOSE 8000

CMD ["/bin/bash", "-c", "uvicorn main:app --host 0.0.0.0 --port 8000"]