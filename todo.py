from fastapi import APIRouter, Path, HTTPException, status
from pydantic import BaseModel

todo_router = APIRouter()

todo_list = []


class Item(BaseModel):
    item: str
    status: str

class Todo(BaseModel):
    id: int
    item: Item

    class Config:
        schema_extra = {
            "example": {
                "id": 1,
                "item": "Example Schema!"
            }
        }


@todo_router.post("/todo")
async def add_todo(todo: Todo) -> dict:
    todo_list.append(todo)
    return {
        "message": "Todo added successfully."
    }

@todo_router.get("/todo")
async def retrieve_todos() -> dict:
    return {
        "todos": todo_list
    }


@todo_router.get("/todo/{todo_id}")
async def get_single_todo(todo_id: int = Path(..., titile="The ID od the todo to retrieve.")) -> dict:
    for todo in todo_list:
        if  todo.id == todo_id:
            return {
                "todo": todo
            }
    # return {
    #     "message": "Todo with supplied ID doesn't exist"
    # }
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Todo woth supplied ID doesn't exist"
    )