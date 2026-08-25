# Jyotish Core & AI Astrologer Microservice (Phase 3)

A high-precision Vedic Astrological Calculation engine paired with an **intelligent, context-injected Jyotish AI Q&A Engine**.

## What's Added in Phase 3

1. **Context-Injected AI Astrologer (`/api/v1/ai/ask`)**:
   - Deterministically calculates and serializes user natal chart, active Vimshottari Mahadasha/Antardasha, Yogas, and real-time transits into an optimized JSON prompt payload.
   - Built-in classical Jyotish knowledge base (House significations, Karakas, planetary relationships).
   - Strict ethical guardrails against fatalistic predictions, emphasizing actionable Vedic guidance, timing, and traditional remedies (Mantras, behavioral adjustments, gemstones, daan).
   - Multi-provider LLM support (OpenAI / Google Gemini / Anthropic) with an included deterministic fallback engine.

2. **Real-time Gochar (Transits) Engine (`/api/v1/chart/transits`)**:
   - Calculates live planetary transits against natal lagna and moon houses.
   - Identifies active planetary aspects and Sade Sati / Dhaiya transit hits.

3. **Daily Astrological Panchang & Horoscopes (`/api/v1/panchang/daily`)**:
   - Daily Tithi, Vara, Nakshatra, Yoga, Karana, and Rahu Kaal calculations.

## Quick Start

### 1. Setup Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Configure Environment Variables (Optional for AI)
```bash
export OPENAI_API_KEY="your-openai-key"       # Or set GEMINI_API_KEY
```

### 3. Run Test Suite
```bash
pytest tests/ -v
```

### 4. Run Development Server
```bash
uvicorn app.main:app --reload --port 8000
```
Interactive Swagger Documentation: `http://localhost:8000/docs`
