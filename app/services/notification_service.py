from datetime import datetime
from app.models.entities import User, SavedProfile

class NotificationService:
    @staticmethod
    def send_daily_digest(user: User, profile: SavedProfile, now: datetime) -> bool:
        print(f"[NOTIFICATION] Dispatched to {user.email}")
        return True
