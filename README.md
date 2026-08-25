# Jyotish Complete Full-Stack Astrology Platform (Phase 14 - Varshaphala / Tajika)

Production-grade Vedic Astrology platform featuring **Varshaphala (Tajika Solar Return Annual Horoscope)**, Synastry PDF Generation, Ashtakavarga Kakshya Timing, Elective Muhurta, Celery workers, KP, Jaimini, Parashara, and JWT auth.

## What's Added in Phase 14
1. **Varshaphala (Tajika Annual Chart) Engine (`app/core/varshaphala.py` & `/api/v1/chart/varshaphala`)**:
   - Exact Sidereal Sun Return timestamp calculation for any target year.
   - Computes the Varsha Lagna & Annual Kundli.
   - **Muntha Calculation**: Progression of 1 sign per completed year.
   - **Varsheshwara (Lord of the Year)** determination using the classical 5 Panchadhikaris.
   - **Tajika Yogas**: Detects Ithasala (Muthashila), Ishrafa (Musaripha), Nakta, and Yamaya yogas.
2. **Frontend Varshaphala Inspector (`VarshaphalaPanel.tsx`)**:
   - Annual predictive dashboard displaying the Varsha Chart, Muntha, Year Lord, and active Tajika configurations.

## Quick Start with Docker
```bash
docker-compose up --build
```
Access the application at `http://localhost`.
