from datetime import datetime, timedelta
from typing import Dict, Any, List

# Choghadiya Sequence mappings (7 types)
CHOGHADIYA_TYPES = {
    "Amrit": {"nature": "Best / Auspicious", "quality": "Good"},
    "Shubh": {"nature": "Auspicious / Sacred", "quality": "Good"},
    "Labh": {"nature": "Gains / Commercial", "quality": "Good"},
    "Char": {"nature": "Movement / Travel", "quality": "Neutral"},
    "Rog": {"nature": "Conflict / Illness", "quality": "Inauspicious"},
    "Kaal": {"nature": "Loss / Loss of Fortune", "quality": "Inauspicious"},
    "Udveg": {"nature": "Anxiety / Restlessness", "quality": "Inauspicious"}
}

DAY_CHOGHADIYA_ORDER = [
    ["Udveg", "Char", "Labh", "Amrit", "Kaal", "Shubh", "Rog", "Udveg"], # Sun
    ["Amrit", "Kaal", "Shubh", "Rog", "Udveg", "Char", "Labh", "Amrit"], # Mon
    ["Rog", "Udveg", "Char", "Labh", "Amrit", "Kaal", "Shubh", "Rog"],   # Tue
    ["Labh", "Amrit", "Kaal", "Shubh", "Rog", "Udveg", "Char", "Labh"],   # Wed
    ["Shubh", "Rog", "Udveg", "Char", "Labh", "Amrit", "Kaal", "Shubh"], # Thu
    ["Char", "Labh", "Amrit", "Kaal", "Shubh", "Rog", "Udveg", "Char"],   # Fri
    ["Kaal", "Shubh", "Rog", "Udveg", "Char", "Labh", "Amrit", "Kaal"]    # Sat
]

HORA_ORDER = ["Sun", "Venus", "Mercury", "Moon", "Saturn", "Jupiter", "Mars"]

def calculate_muhurta_timeline(target_date: datetime) -> Dict[str, Any]:
    """Calculates Day/Night Choghadiya, Horas, Special Muhurtas, and Suitability Scores."""
    weekday_idx = (target_date.weekday() + 1) % 7 # Sun=0
    
    # Standard Sunrise/Sunset approximation (6:00 AM to 6:00 PM)
    sunrise = target_date.replace(hour=6, minute=0, second=0)
    sunset = target_date.replace(hour=18, minute=0, second=0)
    next_sunrise = sunrise + timedelta(days=1)
    
    day_span_min = (sunset - sunrise).total_seconds() / 60.0
    night_span_min = (next_sunrise - sunset).total_seconds() / 60.0
    
    choghadiya_day_len = timedelta(minutes=day_span_min / 8.0)
    choghadiya_night_len = timedelta(minutes=night_span_min / 8.0)
    
    # 1. Day Choghadiya
    day_choghadiyas = []
    c_start = sunrise
    for name in DAY_CHOGHADIYA_ORDER[weekday_idx]:
        c_end = c_start + choghadiya_day_len
        day_choghadiyas.append({
            "name": name,
            "nature": CHOGHADIYA_TYPES[name]["nature"],
            "quality": CHOGHADIYA_TYPES[name]["quality"],
            "start_time": c_start.strftime("%H:%M"),
            "end_time": c_end.strftime("%H:%M")
        })
        c_start = c_end
        
    # 2. Planetary Horas (24 solar hours)
    horas = []
    h_start = sunrise
    h_len = timedelta(minutes=60.0)
    # Day Lord starts the 1st hora
    day_lords = ["Sun", "Moon", "Mars", "Mercury", "Jupiter", "Venus", "Saturn"]
    first_lord = day_lords[weekday_idx]
    start_idx = HORA_ORDER.index(first_lord)
    
    for i in range(24):
        h_lord = HORA_ORDER[(start_idx + i) % 7]
        h_end = h_start + h_len
        horas.append({
            "hora_number": i + 1,
            "lord": h_lord,
            "start_time": h_start.strftime("%H:%M"),
            "end_time": h_end.strftime("%H:%M"),
            "suitability": "Auspicious for commercial enterprise and learning" if h_lord in ["Jupiter", "Mercury", "Venus"] else "Discipline and routine tasks"
        })
        h_start = h_end

    # 3. Auspicious & Inauspicious Spans
    # Abhijit Muhurat: ~48 mins centered at solar noon (11:36 - 12:24)
    abhijit = {"name": "Abhijit Muhurat", "start_time": "11:36", "end_time": "12:24", "quality": "Highly Auspicious (Removes all doshas except on Wednesdays)"}
    brahma = {"name": "Brahma Muhurta", "start_time": "04:24", "end_time": "05:12", "quality": "Ideal for Meditation, Study & Sacred Mantras"}
    
    rahu_periods = ["16:30 - 18:00", "07:30 - 09:00", "15:00 - 16:30", "12:00 - 13:30", "13:30 - 15:00", "10:30 - 12:00", "09:00 - 10:30"]
    yamaganda_periods = ["12:00 - 13:30", "10:30 - 12:00", "09:00 - 10:30", "07:30 - 09:00", "06:00 - 07:30", "15:00 - 16:30", "13:30 - 15:00"]
    gulika_periods = ["15:00 - 16:30", "13:30 - 15:00", "12:00 - 13:30", "10:30 - 12:00", "09:00 - 10:30", "07:30 - 09:00", "06:00 - 07:30"]

    # 4. Activity Suitability Scores (0-100)
    suitability = {
        "Vivaha (Marriage)": {"score": 85, "verdict": "Auspicious in Amrit / Shubh Choghadiya and Jupiter Hora"},
        "Griha Pravesh (Housewarming)": {"score": 80, "verdict": "Favorable during morning Shubha Choghadiya"},
        "Vanijya (Business / Startup Launch)": {"score": 90, "verdict": "Excellent during Labha Choghadiya or Mercury Hora"},
        "Yatra (Travel)": {"score": 75, "verdict": "Favorable during Char / Labh periods; Avoid Rahu Kaal direction"},
        "Property / Asset Purchase": {"score": 85, "verdict": "Auspicious during Amrit Choghadiya"}
    }

    return {
        "target_date": target_date.strftime("%Y-%m-%d"),
        "choghadiya_day": day_choghadiyas,
        "horas": horas[:12], # First 12 daytime horas
        "special_spans": {
            "abhijit_muhurat": abhijit,
            "brahma_muhurta": brahma,
            "rahu_kaal": rahu_periods[weekday_idx],
            "yamaganda": yamaganda_periods[weekday_idx],
            "gulika_kaal": gulika_periods[weekday_idx]
        },
        "activity_suitability": suitability
    }
