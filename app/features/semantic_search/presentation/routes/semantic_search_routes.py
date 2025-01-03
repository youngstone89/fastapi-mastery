import asyncio
import threading
import time
from typing import Union

from pydantic import BaseModel

from app.features.semantic_search.application.usecases.semantic_search_usecase import \
    SemanticSearchUseCase
from app.features.semantic_search.domain.services.semantic_search_service import \
    SemanticSearchService
from fastapi import APIRouter, Depends

router = APIRouter()
service = SemanticSearchService()


def get_semantic_search_usecase():
    return SemanticSearchUseCase(service)

class SentenceInput(BaseModel):
    text: str
    
@router.post("/add-sentence")
async def add_sentence(input: SentenceInput, usecase: SemanticSearchUseCase = Depends(get_semantic_search_usecase)):
    usecase.add_sentence(input.text)
    return {"message": "Sentence added successfully"}


@router.get("/async-find-intention")
async def async_find_intention(query: str, usecase: SemanticSearchUseCase = Depends(get_semantic_search_usecase)):
    current_thread = threading.current_thread()
    print('async_find_intention[{}] received request'.format(
        current_thread.native_id))
    intention = await usecase.async_find_intention(query)
    return {"intention": intention}


@router.get("/sync-find-intention")
async def sync_find_intention(query: str, usecase: SemanticSearchUseCase = Depends(get_semantic_search_usecase)):
    current_thread = threading.current_thread()
    print('sync_find_intention[{}] received request'.format(
        current_thread.native_id))
    intention = await usecase.sync_find_intention(query)
    return {"intention": intention}


@router.get("/")
def read_root():
    return {"Hello": "World"}


@router.get("/async/items/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None):
    current_thread = threading.current_thread()
    print('{} received request for{}'.format(
        current_thread.native_id, item_id))
    await asyncio.sleep(10)
    return {"item_id": item_id, "q": q}


@router.get("/sync/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    current_thread = threading.current_thread()
    print('{} received request for{}'.format(
        current_thread.native_id, item_id))
    time.sleep(10)
    return {"item_id": item_id, "q": q}
