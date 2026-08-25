# Jyotish Complete Full-Stack Astrology Platform (Phase 18 - Stripe & Razorpay Billing)

Production-grade Vedic & Western Astrological platform featuring **Stripe & Razorpay In-App Billing**, Live WebSockets, Secondary Progressions, Sarvatobhadra Chakra (SBC), Kota Chakra, Tajika Varshaphala, Synastry Matchmaking, and Celery Workers.

## What's Added in Phase 18
1. **In-App Billing & Subscription Gateway (`app/services/payment_service.py` & `/api/v1/billing/*`)**:
   - Creates secure payment checkouts for Stripe and Razorpay.
   - Automated webhook processing to grant premium tier status and AI credit refills upon successful payment confirmation.
2. **Frontend Billing Modal (`BillingModal.tsx`)**:
   - Upgradable subscription packages for professional astrologers and enthusiasts.

## Quick Start with Docker
```bash
docker-compose up --build
```
Access the application at `http://localhost`.
