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

### End Points

1. Create Post:
```
curl -X POST http://localhost:8000/api/v1/post \
  -H "Content-Type: application/json" \
  -d '{"key": "your_key", "value": "your_value", "ttl": 3600}'
```
2. Get Post:
```
curl http://localhost:8000/api/v1/post/your_key
```

3. Update Post:
```
curl -X PUT http://localhost:8000/api/v1/post \
  -H "Content-Type: application/json" \
  -d '{"key": "your_key", "value": "updated_value", "ttl": 7200}'
```

4. Delete Post:
```
curl -X DELETE http://localhost:8000/api/v1/post/your_key
```

5. Add Post If Not Exists:
```
curl -X POST http://localhost:8000/api/v1/post-if-not-exists/ \
  -H "Content-Type: application/json" \
  -d '{"key": "your_key", "value": "your_value", "ttl": 3600}'
```
