from typing import Dict, Any
from sqlalchemy.orm import Session
from app.models.entities import User

class PaymentService:
    @staticmethod
    def create_checkout_session(user: User, tier: str) -> Dict[str, Any]:
        prices = {"Premium_Monthly": 9.99, "Annual_Pass": 79.99, "Kundli_Report_Single": 4.99}
        amount = prices.get(tier, 9.99)
        return {
            "user_id": user.id,
            "tier": tier,
            "amount": amount,
            "currency": "USD",
            "gateway": "Stripe / Razorpay",
            "checkout_url": f"https://checkout.stripe.com/pay/cs_test_{user.id}_{tier}"
        }

    @staticmethod
    def fulfill_order(db: Session, user_id: int, tier: str) -> User:
        user = db.query(User).filter(User.id == user_id).first()
        if user:
            user.subscription_tier = tier
            user.ai_credits += 50
            db.commit()
            db.refresh(user)
        return user
