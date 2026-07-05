from fastapi import FastAPI, HTTPException

app = FastAPI()

# TODO: Task 3 - Define a Pydantic model for your item resource
# from pydantic import BaseModel
# class Item(BaseModel):
#     id: int
#     name: str
#     description: str

# In-memory store
items = {}
next_id = 1


# TODO: Task 1 - Add a root GET / route that returns a welcome message


# TODO: Task 1 - Add a GET /health route that returns {"status": "ok"}


# TODO: Task 2 - Add a GET /items route that returns all items


# TODO: Task 2 - Add a GET /items/{item_id} route that returns one item
# Hint: raise HTTPException(status_code=404, detail="Item not found") if missing


# TODO: Task 2 - Add a POST /items route that creates a new item


# TODO: Task 2 - Add a DELETE /items/{item_id} route that removes an item


# Run with: uvicorn starter_code:app --reload
