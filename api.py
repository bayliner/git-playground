from fastapi import FastAPI, File, UploadFile
from typing import Optional
from pydantic import BaseModel
from todo import todo_router
from dt import dt_router
from typing_extensions import Annotated

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

@app.post(("/files/"))
async def create_file(file: Annotated[bytes, File()]):
    return {"file_size:": len(file)}

@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    return {"filename": file.filename}

# @app.get("/items/{item_id}")
# async def items(item_id: int, q: Optional[str] = None):
#     return {
#         "item_id": item_id, "q" : q
#     }

# @app.put("/items_put/{item_id}")
# async def update_item(item_id: int, item: ItemOrigin):
#     return {"item_name": item.name, "item_id": item_id}

# @app.post("/items_all")
# async def create_item(item: ItemOrigin):
#     #item.is_offer = False
#     return item


app.include_router(todo_router)
app.include_router(dt_router)