# Jyotish Complete Full-Stack Astrology Platform (Phase 4)

A comprehensive Vedic Astrology platform featuring a high-precision calculation & classical rules microservice alongside an interactive, mobile-responsive **React + TypeScript frontend**.

## Complete Feature Matrix
- **Astrological Computation Engine**: Sidereal Chitrapaksha/Lahiri calculations via Swiss Ephemeris (`pyswisseph`).
- **Interactive SVG Chart Renderers**:
  - **North Indian Diamond Chart**: Lagna fixed at the top center with dynamic diamond/triangle polygon partitioning.
  - **South Indian Box Chart**: Fixed clockwise zodiac from Pisces to Aries with dynamic planetary placements.
- **Divisional Charts (Shodashvarga)**: Instant toggling across D1 (Rashi), D9 (Navamsha), and D10 (Dashamsha).
- **Vimshottari Dasha Explorer**: Multi-level 120-year Mahadasha & Antardasha timeline visualizer.
- **Classical Analysis Dashboard**:
  - Yoga detection (Gajakesari, Budhaditya, Pancha Mahapurushas, Raja Yogas).
  - Dosha assessment (Mangal Dosha with Parashara cancellations, Shani Sade Sati phase tracker, Kaal Sarp).
  - Sarvashtakavarga (SAV) 12-sign bindu distribution chart.
- **Ashtakoota Matchmaking Engine**: 36-point compatibility report with mutual Manglik alignment.
- **AI Astrologer Chat Interface**: Deterministic chart payload serialization into contextual LLM prompts.

## Quick Start

### 1. Run the Python Backend
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```

### 2. Run the React Frontend
```bash
cd frontend
npm install
npm run dev
```
Open `http://localhost:5173` to explore your astrology platform.
