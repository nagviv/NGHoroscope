# Jyotish Complete Full-Stack Astrology Platform (Phase 13 - Matchmaking PDF & Synastry)

Production-grade Vedic Astrology platform featuring **Synastry / Ashtakoota Matchmaking PDF Report Generation**, Ashtakavarga Kakshya Timing, Elective Muhurta, Celery background workers, KP, Jaimini, Parashara, and JWT auth.

## What's Added in Phase 13
1. **Ashtakoota Matchmaking PDF Report Generator (`/api/v1/matchmaking/pdf`)**:
   - Generates a PDF compatibility report detailing the 36-point Ashtakoota score (Varna, Vashya, Tara, Yoni, Graha Maitri, Gana, Bhakoot, Nadi), mutual Mangal Dosha analysis, and final Vedic alignment verdict.
2. **Astrological Metrics & Planetary Strengths Endpoint (`/api/v1/chart/metrics`)**:
   - Computes normalized percentage scores for planetary dignities, Shadbala rupas, and house strength metrics.
3. **Frontend Synastry & PDF Export Integration**:
   - Dedicated matchmaking comparison view and direct PDF report download.

## Quick Start with Docker
```bash
docker-compose up --build
```
Access the application at `http://localhost`.
