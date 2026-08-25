from datetime import datetime, timedelta
from typing import Dict, Any, List

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
    ["Udveg", "Char", "Labh", "Amrit", "Kaal", "Shubh", "Rog", "Udveg"],
    ["Amrit", "Kaal", "Shubh", "Rog", "Udveg", "Char", "Labh", "Amrit"],
    ["Rog", "Udveg", "Char", "Labh", "Amrit", "Kaal", "Shubh", "Rog"],
    ["Labh", "Amrit", "Kaal", "Shubh", "Rog", "Udveg", "Char", "Labh"],
    ["Shubh", "Rog", "Udveg", "Char", "Labh", "Amrit", "Kaal", "Shubh"],
    ["Char", "Labh", "Amrit", "Kaal", "Shubh", "Rog", "Udveg", "Char"],
    ["Kaal", "Shubh", "Rog", "Udveg", "Char", "Labh", "Amrit", "Kaal"]
]

HORA_ORDER = ["Sun", "Venus", "Mercury", "Moon", "Saturn", "Jupiter", "Mars"]

def calculate_muhurta_timeline(target_date: datetime) -> Dict[str, Any]:
    weekday_idx = (target_date.weekday() + 1) % 7
    sunrise = target_date.replace(hour=6, minute=0, second=0)
    sunset = target_date.replace(hour=18, minute=0, second=0)
    choghadiya_len = timedelta(minutes=90.0)
    
    day_choghadiyas = []
    c_start = sunrise
    for name in DAY_CHOGHADIYA_ORDER[weekday_idx]:
        c_end = c_start + choghadiya_len
        day_choghadiyas.append({
            "name": name,
            "nature": CHOGHADIYA_TYPES[name]["nature"],
            "quality": CHOGHADIYA_TYPES[name]["quality"],
            "start_time": c_start.strftime("%H:%M"),
            "end_time": c_end.strftime("%H:%M")
        })
        c_start = c_end
        
    horas = []
    h_start = sunrise
    day_lords = ["Sun", "Moon", "Mars", "Mercury", "Jupiter", "Venus", "Saturn"]
    start_idx = HORA_ORDER.index(day_lords[weekday_idx])
    for i in range(12):
        h_lord = HORA_ORDER[(start_idx + i) % 7]
        h_end = h_start + timedelta(minutes=60.0)
        horas.append({
            "hora_number": i + 1,
            "lord": h_lord,
            "start_time": h_start.strftime("%H:%M"),
            "end_time": h_end.strftime("%H:%M"),
            "suitability": "Auspicious for commercial & intellectual ventures" if h_lord in ["Jupiter", "Mercury", "Venus"] else "Routine tasks"
        })
        h_start = h_end

    rahu_periods = ["16:30 - 18:00", "07:30 - 09:00", "15:00 - 16:30", "12:00 - 13:30", "13:30 - 15:00", "10:30 - 12:00", "09:00 - 10:30"]

    return {
        "target_date": target_date.strftime("%Y-%m-%d"),
        "choghadiya_day": day_choghadiyas,
        "horas": horas,
        "special_spans": {
            "abhijit_muhurat": {"start_time": "11:36", "end_time": "12:24", "quality": "Supreme Auspicious Window"},
            "brahma_muhurta": {"start_time": "04:24", "end_time": "05:12", "quality": "Ideal for Meditation & Sadhana"},
            "rahu_kaal": rahu_periods[weekday_idx]
        },
        "activity_suitability": {
            "Vivaha (Marriage)": {"score": 85, "verdict": "Favorable during Amrit / Shubh Choghadiya"},
            "Griha Pravesh (Housewarming)": {"score": 80, "verdict": "Favorable during Morning Shubha window"},
            "Vanijya (Business Launch)": {"score": 90, "verdict": "Highly auspicious during Labha Choghadiya"}
        }
    }
