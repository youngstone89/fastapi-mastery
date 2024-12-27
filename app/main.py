
import os

from fastapi import FastAPI
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor

from app.core.opentelemetry import init_opentelemetry
from app.features.semantic_search.presentation.routes import \
    semantic_search_routes

app = FastAPI()
app.include_router(semantic_search_routes.router, prefix="/semantic_search")

init_opentelemetry()
FastAPIInstrumentor.instrument_app(app)

# Function to call on startup


def initialize_resources():
    print("Initializing resources...")
    os.environ["TOKENIZERS_PARALLELISM"] = "false"

    semantic_search_routes.service.add_sentence("Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.")


@app.on_event("startup")
async def startup_event():
    # Call the function
    initialize_resources()
    print("Application startup complete.")
