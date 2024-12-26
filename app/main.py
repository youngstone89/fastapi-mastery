
from fastapi import FastAPI
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor

from app.core.opentelemetry import init_opentelemetry
from app.features.semantic_search.presentation.routes import \
    semantic_search_routes

app = FastAPI()
app.include_router(semantic_search_routes.router, prefix="/semantic_search")

init_opentelemetry()
FastAPIInstrumentor.instrument_app(app)
