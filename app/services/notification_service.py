from datetime import datetime
from app.models.entities import User, SavedProfile
from app.core.panchang import calculate_panchang_details
from app.core.ephemeris import compute_chart_raw
from app.core.dasha import calculate_vimshottari, get_active_dasha

class NotificationService:
    @staticmethod
    def send_daily_digest(user: User, profile: SavedProfile, now: datetime) -> bool:
        """Formats and sends daily personalized horoscope and Panchang digest."""
        p_details = calculate_panchang_details(now, profile.timezone_offset, profile.latitude, profile.longitude)
        
        # Build notification payload
        message = (
            f"Namaste {user.name},\n\n"
            f"Here is your Vedic Astrological Daily Digest for {now.strftime('%Y-%m-%d')}:\n"
            f"• Tithi: {p_details['tithi']['name']} ({p_details['tithi']['paksha']})\n"
            f"• Nakshatra: {p_details['nakshatra']['name']} (Pada {p_details['nakshatra']['pada']})\n"
            f"• Day (Vara): {p_details['vara']}\n"
            f"• Rahu Kaal: {p_details['rahu_kaal']} (Avoid starting major ventures)\n\n"
            f"Wishing you a peaceful and auspicious day ahead."
        )
        
        # In production: dispatch via SMTP, Twilio WhatsApp API, or Push Notification SDK
        print(f"[NOTIFICATION DISPATCHED to {user.email}]:\n{message}\n")
        return True

    @staticmethod
    def check_and_notify_transitions(profile: SavedProfile, now: datetime) -> int:
        """Checks if a major Dasha or Antardasha transition is active."""
        birth_dt = datetime(profile.year, profile.month, profile.day, profile.hour, profile.minute, profile.second)
        natal = compute_chart_raw(birth_dt, profile.timezone_offset, profile.latitude, profile.longitude)
        dasha_tree = calculate_vimshottari(natal["planets"]["Moon"]["longitude"], birth_dt)
        active = get_active_dasha(dasha_tree, now)
        
        # Log active dasha state for worker monitoring
        print(f"[DASHA AUDIT] Profile {profile.name} running {active['mahadasha']}-{active['antardasha']}")
        return 1
