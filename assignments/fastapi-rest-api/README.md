# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a fully functional REST API using the FastAPI framework, learning how to define routes, handle HTTP methods, model request and response data with Pydantic, and test your endpoints.

## 📝 Tasks

### 🛠️ Create a FastAPI App with Basic Routes

#### Description
Set up a FastAPI application and define two starter routes: a root route that returns a welcome message and a health check route. Run the app locally and verify both routes respond correctly.

#### Requirements
Completed program should:

- Install and import `fastapi` and `uvicorn`
- Define a `GET /` route that returns a welcome message as JSON
- Define a `GET /health` route that returns `{"status": "ok"}`
- Run successfully with `uvicorn main:app --reload`


### 🛠️ Build CRUD Endpoints for a Resource

#### Description
Choose a simple resource (e.g., a list of books or tasks) and implement Create, Read, Update, and Delete endpoints for it. Store items in an in-memory list or dictionary.

#### Requirements
Completed program should:

- Define a `GET /items` route that returns all items
- Define a `GET /items/{item_id}` route that returns a single item by ID
- Define a `POST /items` route that accepts JSON and adds a new item
- Define a `DELETE /items/{item_id}` route that removes an item
- Return a meaningful `404` response when an item is not found


### 🛠️ Add Pydantic Models for Request and Response Validation

#### Description
Replace plain dictionaries with Pydantic models to validate incoming request data and shape response output. FastAPI uses these models to auto-generate interactive API documentation.

#### Requirements
Completed program should:

- Define a Pydantic `BaseModel` class for the item resource with at least 3 fields
- Use the model as the request body type in the `POST` route
- Use the model as the response type in `GET` routes
- Access the auto-generated docs at `http://127.0.0.1:8000/docs` and confirm all endpoints appear
