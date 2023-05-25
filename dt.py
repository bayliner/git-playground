from fastapi import FastAPI, APIRouter, HTTPException, status
from pydantic import BaseModel

dt_router = APIRouter()

dtDegree = 0.0
degree_list = []

class DtStatus(BaseModel):
    deg: float

dtStatus = DtStatus

@dt_router.get("/dtdegree/{dt_degree}")
async def add_degree(dt_degree: float) -> dict:
    global dtDegree 
    dtDegree = dt_degree
    degree_list.clear()
    degree_list.append(dtDegree)
    return {
        "message": dtDegree
    }

@dt_router.post("/dtdegree")
async def add_degree(deg: float) -> dict:
    global dtDegree 
    dtDegree = deg
    degree_list.clear()
    degree_list.append(dtDegree)
    return {
        "message": dtDegree
    }

@dt_router.post("/dtnews")
async def add_degree(deg: str) -> dict:
    global dtDegree
    if deg.__contains__("north") | deg.__contains__("North"):
        dtDegree = 0.0
    if deg.__contains__("east") | deg.__contains__("East"):
        dtDegree = 90.0
    if deg.__contains__("west") | deg.__contains__("West"):
        dtDegree = 270.0
    if deg.__contains__("south") | deg.__contains__("South"):
        dtDegree = 180.0

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