from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# a class to define the item
class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None

# a get request to read an item
@app.get("/")
def read_root():
    return {"Hello": "World"}

# a post request to create an item
@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

# a put request to update an item
@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}