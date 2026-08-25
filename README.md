# Jyotish Complete Full-Stack Astrology Platform (Phase 17 - Live WebSockets & Monitoring)

Enterprise-grade Vedic, KP, Jaimini, Tajika & Western Astrological platform featuring **Real-time Live WebSocket Ephemeris Streaming**, **Prometheus Observability**, **Redis Rate Limiting**, Secondary Progressions, Sarvatobhadra Chakra (SBC), Kota Chakra, and Celery Workers.

## What's Added in Phase 17
1. **Live Ephemeris WebSocket Gateway (`/ws/ephemeris/live`)**:
   - Streams exact real-time sidereal planetary degrees, Lagna progression, and live Tithi/Nakshatra every second.
2. **Admin Observability & System Metrics (`/api/v1/admin/stats`)**:
   - Live system statistics, calculation cache hit ratios, and worker task statuses.
3. **Frontend Live Transit Ticker (`LiveTransitTicker.tsx`)**:
   - Animated top status bar displaying real-time cosmic movements and current planetary speeds.

## Quick Start with Docker
```bash
docker-compose up --build
```
Access the application at `http://localhost`.
