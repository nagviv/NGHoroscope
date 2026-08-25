# Jyotish Core Engine & FastAPI Service

A high-precision Vedic Astrological Calculation Microservice built with FastAPI and Swiss Ephemeris (`pyswisseph`).

## Features
- Sidereal calculations (Chitrapaksha / Lahiri Ayanamsa)
- Whole Sign Bhava / House calculation
- Nakshatra & Pada determination
- Divisional charts: D1 (Rashi), D9 (Navamsha), D10 (Dashamsha)
- Complete 120-year Vimshottari Mahadasha and Antardasha timeline
- RESTful API with automated Pydantic schema validation

## Quick Start

### 1. Setup Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Run Tests
```bash
pytest tests/
```

### 3. Run Development Server
```bash
uvicorn app.main:app --reload --port 8000
```
API Documentation will be available at `http://localhost:8000/docs`.
