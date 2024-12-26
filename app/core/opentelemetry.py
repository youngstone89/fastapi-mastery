import os

from opentelemetry import trace
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import \
    OTLPSpanExporter
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor


def init_opentelemetry():
    APP_PROFILE = os.environ.get("APP_PROFILE", "local")
    if APP_PROFILE == "local":
        return

    OTEL_SERVICE_NAME = os.environ.get("OTEL_SERVICE_NAME", "fastapi-app")
    OTEL_EXPORTER_OTLP_ENDPOINT = os.environ.get(
        "OTEL_EXPORTER_OTLP_ENDPOINT", "http://jaeger:4317")
    resource = Resource.create({"service.name": OTEL_SERVICE_NAME})
    tracer_provider = TracerProvider(resource=resource)
    trace.set_tracer_provider(tracer_provider)

    # Set up OTLP exporter to send traces to Jaeger
    otlp_exporter = OTLPSpanExporter(endpoint=OTEL_EXPORTER_OTLP_ENDPOINT)
    span_processor = BatchSpanProcessor(otlp_exporter)
    tracer_provider.add_span_processor(span_processor)
