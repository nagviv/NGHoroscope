# Jyotish Complete Full-Stack Astrology Platform (Phase 19 - Enterprise Security & Prometheus Metrics)

Production-grade Vedic & Western Astrological platform featuring **Prometheus Metrics Export**, **Enterprise Security Headers Middleware**, Stripe/Razorpay In-App Billing, Live WebSockets, Secondary Progressions, Sarvatobhadra Chakra (SBC), Kota Chakra, Tajika Varshaphala, Synastry Matchmaking, and Celery Workers.

## What's Added in Phase 19
1. **Prometheus Metrics Exporter (`app/metrics.py` & `/metrics`)**:
   - Real-time performance monitoring of API request counts, latencies, and calculation execution times.
2. **Security Headers Middleware (`app/middleware/security.py`)**:
   - Hardens the HTTP transport layer against XSS, clickjacking, and MIME-sniffing.

## Quick Start with Docker
```bash
docker-compose up --build
```
Access the application at `http://localhost`.
