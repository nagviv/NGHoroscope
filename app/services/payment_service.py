from typing import Dict, Any

class PaymentService:
    @staticmethod
    def create_checkout_session(user_id: int, tier: str) -> Dict[str, Any]:
        """Creates a checkout intent session for Stripe / Razorpay subscription."""
        prices = {"Premium_Monthly": 9.99, "Annual_Pass": 79.99, "Kundli_Report_Single": 4.99}
        amount = prices.get(tier, 9.99)
        return {
            "user_id": user_id,
            "tier": tier,
            "amount": amount,
            "currency": "USD",
            "status": "initiated",
            "checkout_url": f"https://checkout.stripe.com/pay/cs_test_{user_id}_{tier}"
        }

    @staticmethod
    def handle_successful_webhook(event_payload: dict) -> bool:
        print(f"[PAYMENT WEBHOOK] Successfully processed tier upgrade: {event_payload.get('tier')}")
        return True
