## Simple Crud Project 

A Simple Crud Project that uses Slice DB as main key value store for storing data and uses task queue huey for async processing.

### Features
- Slice DB: Slice DB is an ultra-simple and fast, Python-based, in-memory key-value store that communicates using the RESP protocol.
- Kubernetes Deployment: Utilizes Kubernetes for managing deployment, auto-scaling, and management of containerized applications.
- FastAPI: Modern, fast web framework for building APIs with Python 3.7+ based on standard Python type hints.
- Huey as a REDIS Queue: Lightweight task queue built on top of Redis, allows offloading time-consuming tasks to the background.

## Getting Started

To run this project locally, you'll need:

### Using Python

You'll need:
1. **Python 3+**

```
$ git clone https://github.com/ranjitmahadik/crud-with-slice-db
$ cd crud-with-slice-db
$ pip3 install -r requirements.txt
$ mv .example.env .env
$ uvicorn main:app --reload
```

### Using Docker

You'll need:
1.  **Docker**

```
$ git clone https://github.com/ranjitmahadik/crud-with-slice-db
$ cd crud-with-slice-db
$ mv .example.env .env
$ docker compose up -d
```

### Using K8
```
$ git clone https://github.com/ranjitmahadik/crud-with-slice-db
$ cd crud-with-slice-db
$ cd deployment/
$ kubectl apply -f .
```
