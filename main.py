import asyncio
import threading
import time
from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/async/items/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None):
    current_thread = threading.current_thread()
    print('{} received request for{}'.format(
        current_thread.native_id, item_id))
    await asyncio.sleep(10)
    return {"item_id": item_id, "q": q}


@app.get("/sync/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    current_thread = threading.current_thread()
    print('{} received request for{}'.format(
        current_thread.native_id, item_id))
    time.sleep(10)
    return {"item_id": item_id, "q": q}