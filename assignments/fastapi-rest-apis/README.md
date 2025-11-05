# 📘 Assignment: REST APIs with FastAPI

## 🎯 Objective

Learn how to build RESTful APIs using the FastAPI framework. Students will implement basic CRUD endpoints, use Pydantic models for validation, and run the app with Uvicorn.

## 📝 Tasks

### 🛠️ Build a Simple CRUD API

#### Description
Create a small REST API for an "item" resource. The API should support creating, reading, updating, and deleting items. Use Pydantic models for request/response validation and keep the data in an in-memory store (a Python dict) for simplicity.

#### Requirements
Completed project should:

- Use FastAPI to define the application and routes.
- Define a Pydantic model for the item schema (fields: id, name, description).
- Implement endpoints:
  - POST /items/ — create a new item
  - GET /items/{id} — retrieve a single item
  - GET /items/ — list all items
  - PUT /items/{id} — update an item
  - DELETE /items/{id} — delete an item
- Validate input and return appropriate HTTP status codes (400/404 where applicable).
- Provide a README section with instructions to run the app locally using Uvicorn.

### 🛠️ Optional enhancements

- Add query parameters for filtering or pagination on the list endpoint.
- Persist data to a simple JSON file instead of in-memory storage.
- Add unit tests using `pytest` and `httpx` or `starlette` test client.

---

## How to run (development)

1. Create a virtual environment and install requirements:

```
pip install -r requirements.txt
```

2. Start the server with Uvicorn:

```
uvicorn starter_code:app --reload
```

3. Open the interactive API docs at http://127.0.0.1:8000/docs

---

## Deliverables

- A working FastAPI app in `starter_code.py` (or similar) inside this folder.
- A brief explanation in this README of any design choices or optional features you implemented.
