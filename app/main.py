from typing import Union

from fastapi import FastAPI
from opentelemetry import trace
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import \
    OTLPSpanExporter
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor

from app.features.semantic_search.presentation.routes import \
    semantic_search_routes

# Initialize TracerProvider
resource = Resource.create({"service.name": "your-service-name"})
tracer_provider = TracerProvider(resource=resource)
trace.set_tracer_provider(tracer_provider)

# Set up OTLP exporter to send traces to Jaeger
otlp_exporter = OTLPSpanExporter(endpoint="http://jaeger:4317")
span_processor = BatchSpanProcessor(otlp_exporter)
tracer_provider.add_span_processor(span_processor)

app = FastAPI()
app.include_router(semantic_search_routes.router, prefix="/semantic_search")

FastAPIInstrumentor.instrument_app(app)
