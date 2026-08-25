# Jyotish Complete Full-Stack Astrology Platform (Phase 10 - Muhurta & i18n)

Production-grade Vedic Astrology platform featuring **Muhurta (Elective Auspicious Timing)**, Multi-Language Internationalization (English, Hindi, Telugu, Tamil, Sanskrit), Krishnamurti Paddhati (KP), Jaimini, Parashara, and JWT auth.

## What's Added in Phase 10
1. **Elective Muhurta Engine (`app/core/muhurta.py`)**:
   - Day & Night **Choghadiya** (Amrit, Shubh, Labh, Char, Rog, Kaal, Udveg).
   - 24 Planetary **Horas** calculated from local sunrise.
   - **Abhijit Muhurat**, **Brahma Muhurta**, **Rahu Kaal**, **Yamaganda**, and **Gulika Kaal**.
   - Activity Suitability Scores for:
     - **Vivaha (Marriage)**
     - **Griha Pravesh (Housewarming)**
     - **Vanijya (New Business / Trading)**
     - **Yatra (Travel)**
     - **Kraya-Vikraya (Property / Asset Purchase)**
2. **Multi-Language Localization Support**:
   - UI and calculation string dictionaries across English, Hindi (हिंदी), Telugu (తెలుగు), Tamil (தமிழ்), and Sanskrit (संस्कृत).
3. **Frontend Muhurta Inspector (`MuhurtaPanel.tsx`)**:
   - Interactive timetable and activity compatibility dashboard.

## Quick Start with Docker
```bash
docker-compose up --build
```
Access the application at `http://localhost`.
