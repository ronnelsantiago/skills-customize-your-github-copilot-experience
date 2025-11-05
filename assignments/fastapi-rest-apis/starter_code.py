from typing import Dict, List, Optional

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="FastAPI Items API")


class Item(BaseModel):
    id: int
    name: str
    description: Optional[str] = None


# In-memory store: id -> Item
store: Dict[int, Item] = {}


@app.post("/items/", response_model=Item, status_code=201)
def create_item(item: Item):
    if item.id in store:
        raise HTTPException(status_code=400, detail="Item with this ID already exists")
    store[item.id] = item
    return item


@app.get("/items/", response_model=List[Item])
def list_items():
    return list(store.values())


@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int):
    item = store.get(item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


@app.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, updated: Item):
    if item_id != updated.id:
        raise HTTPException(status_code=400, detail="ID in path and body must match")
    if item_id not in store:
        raise HTTPException(status_code=404, detail="Item not found")
    store[item_id] = updated
    return updated


@app.delete("/items/{item_id}", status_code=204)
def delete_item(item_id: int):
    if item_id not in store:
        raise HTTPException(status_code=404, detail="Item not found")
    del store[item_id]
    return None


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("starter_code:app", host="127.0.0.1", port=8000, reload=True)
