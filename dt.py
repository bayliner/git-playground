from fastapi import FastAPI, APIRouter, HTTPException, status
from pydantic import BaseModel

dt_router = APIRouter()

dtDegree = 0.0
degree_list = []

class DtStatus(BaseModel):
    deg: float

dtStatus = DtStatus

@dt_router.post("/dtdegree")
async def add_degree(deg: float) -> dict:
    global dtDegree 
    dtDegree = deg
    degree_list.clear()
    degree_list.append(app.dtDegree)
    return {
        "message": app.dtDegree
    }

@dt_router.post("/dtnews")
async def add_degree(deg: str) -> dict:
    if deg.__contains__("north") | deg.__contains__("North"):
        app.dtDegree = 0.0
    if deg.__contains__("east") | deg.__contains__("East"):
        app.dtDegree = 90.0
    if deg.__contains__("west") | deg.__contains__("West"):
        app.dtDegree = 270.0
    if deg.__contains__("south") | deg.__contains__("South"):
        app.dtDegree = 180.0

    degree_list.clear()
    degree_list.append(dtDegree)
    return {
        "message": dtDegree
    }

@dt_router.get("/dtstatus/")
async def get_dt() -> dict:
    return {
        "degree": dtDegree
    }
    # raise HTTPException(
    #     status_code=status.HTTP_404_NOT_FOUND,
    #     detail="Todo woth supplied ID doesn't exist"
    # )