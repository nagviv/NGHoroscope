# Jyotish Complete Full-Stack Astrology Platform (Phase 8 - Auth & Saved Profiles)

Production-ready Vedic Astrology platform featuring JWT Authentication, Multi-Profile Saved Horoscopes (SQLAlchemy/SQLite/PostgreSQL), Parashara & Jaimini calculation engines, interactive multi-style SVG charts, PDF generation, and Docker orchestration.

## What's Added in Phase 8
1. **User Authentication & Authorization**:
   - JWT-based authentication (`/api/v1/auth/register`, `/api/v1/auth/login`, `/api/v1/auth/me`).
   - Secure password hashing using PBKDF2/SHA256.
2. **Saved Kundli Profiles Database**:
   - Endpoints to create, list, retrieve, and delete saved family/client charts (`/api/v1/profiles`).
   - Database persistence via SQLAlchemy models supporting SQLite (default local) and PostgreSQL.
3. **Frontend Auth & Profile Selector**:
   - React state handling for user login/registration and quick loading of saved horoscopes into the interactive dashboard.

## Quick Start with Docker
```bash
docker-compose up --build
```
Access the application at `http://localhost`.
