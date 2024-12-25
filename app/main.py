from typing import Union

from fastapi import FastAPI

from app.features.semantic_search.presentation.routes import \
    semantic_search_routes

app = FastAPI()
app.include_router(semantic_search_routes.router, prefix="/semantic_search")
