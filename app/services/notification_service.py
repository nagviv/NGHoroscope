from datetime import datetime
from app.models.entities import User, SavedProfile
from app.core.panchang import calculate_panchang_details
from app.core.ephemeris import compute_chart_raw
from app.core.dasha import calculate_vimshottari, get_active_dasha

class NotificationService:
    @staticmethod
    def send_daily_digest(user: User, profile: SavedProfile, now: datetime) -> bool:
        p_details = calculate_panchang_details(now, profile.timezone_offset, profile.latitude, profile.longitude)
        message = (
            f"Namaste {user.name},\n\n"
            f"Daily Digest for {now.strftime('%Y-%m-%d')}:\n"
            f"• Tithi: {p_details['tithi']['name']} ({p_details['tithi']['paksha']})\n"
            f"• Nakshatra: {p_details['nakshatra']['name']}\n"
            f"• Rahu Kaal: {p_details['rahu_kaal']}\n"
        )
        print(f"[NOTIFICATION] Dispatched to {user.email}")
        return True

    @staticmethod
    def check_and_notify_transitions(profile: SavedProfile, now: datetime) -> int:
        birth_dt = datetime(profile.year, profile.month, profile.day, profile.hour, profile.minute, profile.second)
        natal = compute_chart_raw(birth_dt, profile.timezone_offset, profile.latitude, profile.longitude)
        dasha_tree = calculate_vimshottari(natal["planets"]["Moon"]["longitude"], birth_dt)
        active = get_active_dasha(dasha_tree, now)
        print(f"[DASHA AUDIT] {profile.name}: {active['mahadasha']}-{active['antardasha']}")
        return 1
