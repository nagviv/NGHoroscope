# Jyotish Core Engine & Classical Analysis Service (Phase 2)

A production-grade Vedic Astrological Calculation and Classical Jyotish Rules Engine microservice built with FastAPI and Swiss Ephemeris (`pyswisseph`).

## Features Added in Phase 2
- **Yoga Identification Engine**: Detects Raja Yogas, Dhana Yogas, Gajakesari, Pancha Mahapurusha Yogas (Ruchaka, Bhadra, Hamsa, Malavya, Sasa), Budhaditya, Neechbhanga Raja Yoga, Viparita Raja Yogas, and Chandra Yogas.
- **Dosha Analysis Module**:
  - **Manglik (Kuja) Dosha**: Evaluates Mars from Lagna, Moon, and Venus across 1st, 2nd, 4th, 7th, 8th, and 12th houses with Parashara cancellation rules.
  - **Shani Sade Sati**: Tracks exact 7.5-year transit phase (Rising, Peak, Setting) and Shani Dhaiya (Kantaka/Ashtama Shani).
  - **Kaal Sarp & Guru Chandal Doshas**.
- **Ashtakavarga System**: Computes Sarvashtakavarga (SAV) points (0-56 scale per rashi) and planetary Bhinnashtakavarga (BAV).
- **Ashtakoota Matchmaking (Synastry)**: Complete 36-point compatibility engine (Varna, Vashya, Tara, Yoni, Graha Maitri, Gana, Bhakoot, Nadi) with dosha exception rules.

## Quick Start

### 1. Setup Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Run Comprehensive Test Suite
```bash
pytest tests/ -v
```

### 3. Run Development Server
```bash
uvicorn app.main:app --reload --port 8000
```
Interactive Swagger API documentation: `http://localhost:8000/docs`
