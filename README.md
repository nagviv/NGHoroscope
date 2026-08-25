# Jyotish Complete Full-Stack Astrology Platform (Phase 15 - SBC & Kota Chakra)

Production-grade Vedic Astrology platform featuring **Sarvatobhadra Chakra (SBC)**, **Kota Chakra Fort Defense System**, Varshaphala (Tajika), Synastry PDF Reports, Ashtakavarga Kakshya Timing, Elective Muhurta, Celery workers, KP, Jaimini, Parashara, and JWT auth.

## What's Added in Phase 15
1. **Sarvatobhadra Chakra (SBC) 81-Square Grid Engine (`app/core/sbc.py` & `/api/v1/chart/sbc`)**:
   - 28-Nakshatra grid analysis (including Abhijit).
   - Precision Front, Right, and Left **Vedha (Piercing/Aspects)** from transiting planets onto sensitive natal points (*Janma, Karma, Sanghatika, Manasa, Vainashika, Adhana*).
2. **Kota Chakra Fort Defense System (`app/core/kota.py` & `/api/v1/chart/kota`)**:
   - 4-Zone fortress partitioning: *Stambha (Pillar), Madhya (Inner), Prakara (Wall), Bahya (Exterior)*.
   - Evaluates *Kota Swami* (Lord of the Fort) and *Kota Pala* (Fort Guardian) for health, surgery, resilience, and crisis timing.
3. **Monetization & Billing Subsystem (`app/services/payment_service.py`)**:
   - Webhook & verification structures for Stripe and Razorpay payments for unlocking premium multi-page Kundli PDFs and unlimited AI consultations.
4. **Frontend Chakra Dashboard (`ChakraPanel.tsx`)**:
   - Visual inspection grid of Sarvatobhadra Vedhas and Kota Chakra fortress occupancy.

## Quick Start with Docker
```bash
docker-compose up --build
```
Access the application at `http://localhost`.
