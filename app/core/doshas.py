from typing import Dict, Any, List
import swisseph as swe

def check_mangal_dosha(chart: Dict[str, Any]) -> Dict[str, Any]:
    """Checks Manglik (Kuja) Dosha from Lagna, Moon, and Venus, with classical cancellations."""
    mars = chart["planets"]["Mars"]
    moon = chart["planets"]["Moon"]
    venus = chart["planets"]["Venus"]
    
    # House positions of Mars relative to Lagna, Moon, and Venus
    mars_lagna_house = mars["house"]
    mars_moon_house = ((mars["sign_index"] - moon["sign_index"]) % 12) + 1
    mars_venus_house = ((mars["sign_index"] - venus["sign_index"]) % 12) + 1
    
    dosha_houses = [1, 2, 4, 7, 8, 12]
    
    is_from_lagna = mars_lagna_house in dosha_houses
    is_from_moon = mars_moon_house in dosha_houses
    is_from_venus = mars_venus_house in dosha_houses
    
    is_present = is_from_lagna or is_from_moon or is_from_venus
    
    # Classical Cancellations
    cancellations = []
    # 1. Mars in own sign (Aries/Scorpio) or Exalted (Capricorn)
    if mars["sign_index"] in [0, 7, 9]:
        cancellations.append("Mars is placed in its own or exalted sign.")
    # 2. Jupiter conjoining or aspecting Mars
    if chart["planets"]["Jupiter"]["house"] == mars["house"]:
        cancellations.append("Benefic Jupiter conjoins Mars, neutralizing aggressive tendencies.")
        
    is_cancelled = len(cancellations) > 0
    severity = "None"
    if is_present:
        if is_cancelled:
            severity = "Low / Cancelled"
        elif is_from_lagna and is_from_moon:
            severity = "High"
        else:
            severity = "Moderate"
            
    return {
        "is_present": is_present and not is_cancelled,
        "is_cancelled": is_cancelled,
        "severity": severity,
        "cancellation_reasons": cancellations,
        "placements": {
            "from_lagna_house": mars_lagna_house,
            "from_moon_house": mars_moon_house,
            "from_venus_house": mars_venus_house
        }
    }


def check_sade_sati(natal_moon_sign_idx: int, transit_saturn_sign_idx: int) -> Dict[str, Any]:
    """Evaluates Shani Sade Sati and Dhaiya relative to Natal Moon."""
    diff = (transit_saturn_sign_idx - natal_moon_sign_idx) % 12
    
    # Sade Sati occurs when Saturn is 12th (11), 1st (0), or 2nd (1) from Moon
    if diff == 11:
        return {
            "is_active": True,
            "phase": "Rising Phase (12th from Moon)",
            "description": "Saturn transiting behind Moon; triggers restructuring, mental discipline, and travel/expenses."
        }
    elif diff == 0:
        return {
            "is_active": True,
            "phase": "Peak Phase (Janma Shani - 1st from Moon)",
            "description": "Saturn transiting directly over natal Moon; demands high emotional resilience and perseverance."
        }
    elif diff == 1:
        return {
            "is_active": True,
            "phase": "Setting Phase (2nd from Moon)",
            "description": "Saturn transiting 2nd from Moon; focus shifts to family, speech, financial stabilization."
        }
    elif diff == 3: # 4th from Moon
        return {
            "is_active": False,
            "dhaiya": "Kantaka Shani (4th from Moon)",
            "description": "Small 2.5-year transit challenging peace of mind and domestic balance."
        }
    elif diff == 7: # 8th from Moon
        return {
            "is_active": False,
            "dhaiya": "Ashtama Shani (8th from Moon)",
            "description": "Major transformation and career restructuring cycle."
        }
    else:
        return {
            "is_active": False,
            "phase": "None",
            "description": "Saturn is not currently in a Sade Sati or major Dhaiya transit relative to natal Moon."
        }


def check_kaal_sarp_dosha(chart: Dict[str, Any]) -> Dict[str, Any]:
    """Checks if all 7 visible planets are hemmed between Rahu and Ketu."""
    rahu_lon = chart["planets"]["Rahu"]["longitude"]
    ketu_lon = chart["planets"]["Ketu"]["longitude"]
    
    visible_planets = ["Sun", "Moon", "Mars", "Mercury", "Jupiter", "Venus", "Saturn"]
    
    side_a = 0
    side_b = 0
    
    for p in visible_planets:
        p_lon = chart["planets"][p]["longitude"]
        # Normalize relative to Rahu
        rel_to_rahu = (p_lon - rahu_lon) % 360.0
        if rel_to_rahu < 180.0:
            side_a += 1
        else:
            side_b += 1
            
    is_present = (side_a == 7 or side_b == 7)
    return {
        "is_present": is_present,
        "type": "Full Kaal Sarp" if is_present else ("Partial / Neutral" if (side_a == 6 or side_b == 6) else "None"),
        "description": "All planets hemmed between Rahu and Ketu axis, indicating karmic turning points." if is_present else "Planets are freely distributed across the chart."
    }
