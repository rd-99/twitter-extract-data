from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()


def Items(BaseModel) :
    name : str
    id : int
    k : Union[int , None] = None
@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.put("/items/{id}")
def put_api(id : int) :
    return (id + 99)