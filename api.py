from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
from todo import todo_router

app = FastAPI()

class ItemOrigin(BaseModel):
    name: str
    price: float
    is_offer: Optional[bool] = None


@app.get("/")
async def welcome() -> dict:
    return {
        "message": "Hello fastapi world!"
    }

@app.get("/items/{item_id}")
async def items(item_id: int, q: Optional[str] = None):
    return {
        "item_id": item_id, "q" : q
    }

@app.put("/items_put/{item_id}")
async def update_item(item_id: int, item: ItemOrigin):
    return {"item_name": item.name, "item_id": item_id}

@app.post("/items_all")
async def create_item(item: ItemOrigin):
    #item.is_offer = False
    return item


app.include_router(todo_router)