# Jyotish Complete Full-Stack Astrology Platform (Phase 7 - Jaimini Engine)

Production-grade Vedic Astrology platform featuring Parashara and **Jaimini Astrological Subsystems**, high-precision ephemeris calculations, React frontend with multi-style SVG charts, PDF generation, and CI/CD pipelines.

## What's Added in Phase 7 (Jaimini Sutras Engine)
1. **7 Chara Karakas Calculation (`app/core/jaimini.py`)**:
   - Computes the 7 non-Rahu Karakas based on decreasing degree within signs:
     - **Atmakaraka (AK)**: Soul signifier & life purpose
     - **Amatyakaraka (AmK)**: Career, intellect & professional status
     - **Bhratrikaraka (BK)**: Siblings, gurus & courage
     - **Matrikaraka (MK)**: Mother, emotional sanctuary & vehicles
     - **Putrakaraka (PK)**: Children, creativity & intellect
     - **Gnatikaraka (GK)**: Obstacles, competition & disease
     - **Darakaraka (DK)**: Spouse, romantic partners & alliances
2. **Karakamsha & Arudha Padas**:
   - Identifies the Navamsha sign occupied by Atmakaraka (Karakamsha Lagna).
   - Computes Arudha Lagna (AL) and Upapada Lagna (UL).
3. **Jaimini Chara Dasha Timeline**:
   - Computes sign-based major period cycles for lifetime timing of events.

## Quick Start
```bash
docker-compose up --build
```
Access the application at `http://localhost`.
