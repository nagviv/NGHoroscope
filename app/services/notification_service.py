from datetime import datetime
from app.models.entities import User, SavedProfile
from app.core.panchang import calculate_panchang_details

class NotificationService:
    @staticmethod
    def send_daily_digest(user: User, profile: SavedProfile, now: datetime) -> bool:
        p_details = calculate_panchang_details(now, profile.timezone_offset, profile.latitude, profile.longitude)
        print(f"[NOTIFICATION] Dispatched to {user.email}")
        return True
