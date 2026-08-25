# Jyotish Complete Full-Stack Astrology Platform (Phase 6)

Production-grade Vedic Astrology platform featuring high-precision calculations, classical rules microservice, React frontend, **PDF Kundli Report Generator (ReportLab)**, **Shadbala (Planetary Strengths)**, and automated **GitHub Actions CI/CD**.

## New Additions in Phase 6
1. **Exportable PDF Kundli Report (`/api/v1/chart/pdf`)**:
   - Generates a multi-page PDF Kundli report containing Planetary Details, D1 Rashi, D9 Navamsha, Active Yogas, Doshas, and Vimshottari Dasha timeline.
2. **Shadbala Strength Module (`app/core/shadbala.py`)**:
   - Computes Sthana Bala, Dig Bala, Kaala Bala, Cheshta Bala, and Naisargika Bala to calculate planetary virupas and rupas.
3. **GitHub Actions CI/CD Pipeline (`.github/workflows/ci.yml`)**:
   - Automated testing on push/PR for both Python backend (pytest) and React frontend (TypeScript compilation and build).

## Quick Start with Docker
```bash
docker-compose up --build
```
Access the application at `http://localhost`.
