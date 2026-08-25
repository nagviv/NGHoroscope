# Jyotish Complete Full-Stack Astrology Platform (Phase 9 - KP Astrology)

Production-ready Vedic Astrology platform featuring **Krishnamurti Paddhati (KP Astrology)**, Parashara and Jaimini systems, JWT auth, saved horoscopes, and multi-style SVG charts.

## What's Added in Phase 9 (KP Astrology Engine)
1. **Placidus House Cusps with KP / Lahiri Ayanamsa (`app/core/kp.py`)**:
   - Exact Placidus degree cusps (1st through 12th Cusp).
2. **249 KP Sub-Lord Table**:
   - Computes Sign Lord, Star (Nakshatra) Lord, Sub-Lord, and Sub-Sub-Lord for all 9 Grahas and 12 House Cusps.
3. **KP Ruling Planets (RP)**:
   - Evaluates real-time / birth Ruling Planets (Lagna Sign & Star Lord, Moon Sign & Star Lord, Day Lord).
4. **KP 4-Fold Planetary Significators**:
   - Determines House Significations based on:
     - Level A: Planets in star of occupant
     - Level B: House Occupant
     - Level C: Planets in star of house lord
     - Level D: House Lord
5. **Frontend KP Sub-Lord Table UI (`KPPanel.tsx`)**:
   - Interactive UI inspector displaying 12 Cusps, Planetary Sub-Lords, and Ruling Planets.

## Quick Start with Docker
```bash
docker-compose up --build
```
Access the application at `http://localhost`.
