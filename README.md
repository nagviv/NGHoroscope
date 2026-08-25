# Jyotish Complete Full-Stack Astrology Platform (Phase 11 - Background Worker & Notifications)

Production-ready Vedic Astrology platform featuring **Celery & Redis automated background workers** for scheduled daily transits, personalized Panchang, and Dasha transition alerts alongside Parashara, Jaimini, KP, and Muhurta calculation suites.

## What's Added in Phase 11
1. **Celery Worker & Beat Scheduler (`app/worker.py`)**:
   - Automated daily task execution (`dispatch_daily_astrological_digest`).
   - Automated periodic check for Dasha transitions and Sade Sati status changes (`check_dasha_transitions`).
2. **Notification Dispatch Service (`app/services/notification_service.py`)**:
   - Dispatches formatted astrological summaries via Email (SMTP) and Webhook payloads (ready for WhatsApp/SMS gateways like Twilio/Meta Business API).
3. **Containerized Worker & Redis Service (`docker-compose.yml`)**:
   - Adds Redis broker/backend and Celery worker/beat containers alongside the FastAPI backend and React frontend.

## Quick Start with Docker
```bash
docker-compose up --build
```
Access the application at `http://localhost`.
