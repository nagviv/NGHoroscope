# Jyotish Complete Full-Stack Astrology Platform (Phase 16 - Progressions & Solar Arc)

Production-grade Vedic & Western Astrological platform featuring **Secondary Progressions**, **Solar Arc Directions**, Sarvatobhadra Chakra (SBC), Kota Chakra, Tajika Varshaphala, Synastry PDF Reports, Ashtakavarga Kakshya Timing, Elective Muhurta, Celery workers, KP, Jaimini, Parashara, and JWT auth.

## What's Added in Phase 16
1. **Secondary Progressions Engine (`app/core/progressions.py` & `/api/v1/chart/progressions`)**:
   - Computes secondary progressed planetary positions based on the classical **Day-for-a-Year (Major Progression)** formula.
   - Computes **Solar Arc Directions** (advancing all natal planets by the Progressed Sun's arc distance).
   - Generates exact aspects (Conjunctions, Sextiles, Squares, Trines, Oppositions) with precision 1° orbs against natal placements.
2. **Frontend Progressions Dashboard (`ProgressionsPanel.tsx`)**:
   - Displays Progressed vs Natal coordinates, active Solar Arc hits, and major lifetime milestone triggers.

## Quick Start with Docker
```bash
docker-compose up --build
```
Access the application at `http://localhost`.
