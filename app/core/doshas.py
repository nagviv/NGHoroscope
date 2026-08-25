from typing import Dict, Any

def check_mangal_dosha(chart: Dict[str, Any]) -> Dict[str, Any]:
    mars = chart["planets"]["Mars"]
    moon = chart["planets"]["Moon"]
    venus = chart["planets"]["Venus"]
    h_lagna = mars["house"]
    dosha_houses = [1, 2, 4, 7, 8, 12]
    is_present = h_lagna in dosha_houses
    cancellations = ["Mars in own/exalted sign"] if mars["sign_index"] in [0, 7, 9] else []
    is_cancelled = len(cancellations) > 0
    return {
        "is_present": is_present and not is_cancelled,
        "is_cancelled": is_cancelled,
        "severity": "Cancelled" if is_cancelled else ("High" if is_present else "None"),
        "cancellation_reasons": cancellations
    }

def check_sade_sati(natal_moon_sign_idx: int, transit_saturn_sign_idx: int) -> Dict[str, Any]:
    diff = (transit_saturn_sign_idx - natal_moon_sign_idx) % 12
    if diff in [11, 0, 1]:
        phases = {11: "Rising Phase", 0: "Peak Phase", 1: "Setting Phase"}
        return {"is_active": True, "phase": phases[diff], "description": "Saturn in Sade Sati span."}
    return {"is_active": False, "phase": "None", "description": "No active Sade Sati."}

def check_kaal_sarp_dosha(chart: Dict[str, Any]) -> Dict[str, Any]:
    rahu_lon = chart["planets"]["Rahu"]["longitude"]
    visible = ["Sun", "Moon", "Mars", "Mercury", "Jupiter", "Venus", "Saturn"]
    side_a = sum(1 for p in visible if ((chart["planets"][p]["longitude"] - rahu_lon) % 360.0) < 180.0)
    is_present = (side_a == 7 or side_a == 0)
    return {"is_present": is_present, "type": "Full Kaal Sarp" if is_present else "None", "description": "Planetary nodal axis."}
