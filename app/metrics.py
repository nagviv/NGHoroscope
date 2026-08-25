from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST
from fastapi import Response

REQUEST_COUNT = Counter("jyotish_http_requests_total", "Total HTTP requests", ["method", "endpoint", "status"])
REQUEST_LATENCY = Histogram("jyotish_http_request_duration_seconds", "HTTP request latency", ["endpoint"])
CALCULATION_DURATION = Histogram("jyotish_astrology_calculation_seconds", "Astrological calculation time", ["algorithm"])

def metrics_endpoint():
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)
