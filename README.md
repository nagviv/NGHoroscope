# Jyotish Complete Full-Stack Astrology Platform (Phase 12 - Kakshya Engine)

Production-grade Vedic Astrology platform featuring **Ashtakavarga Kakshya Transit Timing**, Elective Muhurta, Celery & Redis background workers, Krishnamurti Paddhati (KP), Jaimini, Parashara, and JWT auth.

## What's Added in Phase 12
1. **Ashtakavarga Kakshya Precision Engine (`app/core/kakshya.py`)**:
   - Divides each 30° sign into 8 equal Kakshyas (3°45' each) ruled by the 7 planets and Ascendant.
   - Evaluates active Gochar transiting planets against natal BAV point matrices to identify auspicious/inauspicious transit degree spans.
2. **Frontend Kakshya Transit Inspector (`KakshyaPanel.tsx`)**:
   - Visual inspection grid of the 8 Kakshya zones per sign and active transiting grahas.

## Quick Start with Docker
```bash
docker-compose up --build
```
Access the application at `http://localhost`.
