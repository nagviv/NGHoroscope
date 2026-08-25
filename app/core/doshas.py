from typing import Dict, Any

def check_mangal_dosha(chart: Dict[str, Any]) -> Dict[str, Any]:
    mars = chart["planets"]["Mars"]
    moon = chart["planets"]["Moon"]
    venus = chart["planets"]["Venus"]
    
    h_lagna = mars["house"]
    h_moon = ((mars["sign_index"] - moon["sign_index"]) % 12) + 1
    h_venus = ((mars["sign_index"] - venus["sign_index"]) % 12) + 1
    
    dosha_houses = [1, 2, 4, 7, 8, 12]
    is_present = (h_lagna in dosha_houses) or (h_moon in dosha_houses) or (h_venus in dosha_houses)
    
    cancellations = []
    if mars["sign_index"] in [0, 7, 9]:
        cancellations.append("Mars is placed in own or exalted sign.")
    if chart["planets"]["Jupiter"]["house"] == mars["house"]:
        cancellations.append("Benefic Jupiter conjoins Mars.")
        
    is_cancelled = len(cancellations) > 0
    return {
        "is_present": is_present and not is_cancelled,
        "is_cancelled": is_cancelled,
        "severity": "Cancelled" if is_cancelled else ("High" if (h_lagna in dosha_houses and h_moon in dosha_houses) else ("Moderate" if is_present else "None")),
        "cancellation_reasons": cancellations
    }

def check_sade_sati(natal_moon_sign_idx: int, transit_saturn_sign_idx: int) -> Dict[str, Any]:
    diff = (transit_saturn_sign_idx - natal_moon_sign_idx) % 12
    if diff == 11:
        return {"is_active": True, "phase": "Rising Phase (12th from Moon)", "description": "Saturn transiting 12th from Moon."}
    elif diff == 0:
        return {"is_active": True, "phase": "Peak Phase (Janma Shani)", "description": "Saturn transiting over natal Moon."}
    elif diff == 1:
        return {"is_active": True, "phase": "Setting Phase (2nd from Moon)", "description": "Saturn transiting 2nd from Moon."}
    return {"is_active": False, "phase": "None", "description": "No active Sade Sati."}

def check_kaal_sarp_dosha(chart: Dict[str, Any]) -> Dict[str, Any]:
    rahu_lon = chart["planets"]["Rahu"]["longitude"]
    visible = ["Sun", "Moon", "Mars", "Mercury", "Jupiter", "Venus", "Saturn"]
    side_a = sum(1 for p in visible if ((chart["planets"][p]["longitude"] - rahu_lon) % 360.0) < 180.0)
    is_present = (side_a == 7 or side_a == 0)
    return {
        "is_present": is_present,
        "type": "Full Kaal Sarp" if is_present else "None",
        "description": "All planets hemmed within nodal axis." if is_present else "Planets are distributed across the chart."
    }
