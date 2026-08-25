from datetime import datetime
from typing import Dict, Any, List
from app.core.constants import NAKSHATRAS
from app.core.ephemeris import compute_chart_raw

# 28-Nakshatra sequence including Abhijit for Sarvatobhadra Chakra
SBC_NAKSHATRAS = [
    "Krittika", "Rohini", "Mrigashira", "Ardra", "Punarvasu", "Pushya", "Ashlesha",
    "Magha", "Purva Phalguni", "Uttara Phalguni", "Hasta", "Chitra", "Svati", "Vishakha",
    "Anuradha", "Jyeshtha", "Mula", "Purva Ashadha", "Uttara Ashadha", "Abhijit", "Shravana",
    "Dhanishta", "Shatabhisha", "Purva Bhadrapada", "Uttara Bhadrapada", "Revati", "Ashwini", "Bharani"
]

def calculate_sarvatobhadra_chakra(birth_dt: datetime, target_dt: datetime, tz_offset: float, lat: float, lon: float) -> Dict[str, Any]:
    """Calculates Sarvatobhadra Chakra Vedhas (Piercing Aspects) from transiting planets onto natal sensitive stars."""
    natal_chart = compute_chart_raw(birth_dt, tz_offset, lat, lon)
    transit_chart = compute_chart_raw(target_dt, tz_offset, lat, lon)
    
    natal_moon_nak = natal_chart["planets"]["Moon"]["nakshatra"]
    janma_nak_idx = NAKSHATRAS.index(natal_moon_nak)
    
    # 7 Special Sensitive Nakshatras from Janma Nakshatra
    sensitive_points = {
        "Janma Nakshatra (Self/Vitality)": natal_moon_nak,
        "Karma Nakshatra (10th - Career)": NAKSHATRAS[(janma_nak_idx + 9) % 27],
        "Sanghatika (16th - Alliances/Debts)": NAKSHATRAS[(janma_nak_idx + 15) % 27],
        "Samudayika (18th - General Fortune)": NAKSHATRAS[(janma_nak_idx + 17) % 27],
        "Adhana (19th - Family/Lineage)": NAKSHATRAS[(janma_nak_idx + 18) % 27],
        "Vainashika (23rd - Obstacles/Losses)": NAKSHATRAS[(janma_nak_idx + 22) % 27],
        "Manasa (25th - Mental Peace)": NAKSHATRAS[(janma_nak_idx + 24) % 27]
    }
    
    # Check Active Vedhas from Malefic & Benefic Transit Grahas
    vedhas = []
    malefics = ["Saturn", "Mars", "Sun", "Rahu", "Ketu"]
    benefics = ["Jupiter", "Venus", "Mercury", "Moon"]
    
    for p_name, p_data in transit_chart["planets"].items():
        t_nak = p_data["nakshatra"]
        nature = "Malefic" if p_name in malefics else "Benefic"
        
        # Check if transit nakshatra hits any sensitive natal point directly or via Front Vedha
        for point_name, point_nak in sensitive_points.items():
            if t_nak == point_nak:
                vedhas.append({
                    "planet": p_name,
                    "nature": nature,
                    "transit_nakshatra": t_nak,
                    "target_sensitive_point": point_name,
                    "vedha_type": "Direct Conjunction / Front Vedha",
                    "impact": "Stressful / Caution Advised" if nature == "Malefic" else "Auspicious Support / Growth"
                })
                
    return {
        "transit_date": target_dt.strftime("%Y-%m-%d"),
        "sensitive_nakshatras": sensitive_points,
        "active_vedhas": vedhas,
        "defense_verdict": "High Protection / Benefic Vedha Active" if any(v["nature"] == "Benefic" for v in vedhas) else ("Caution Advised / Malefic Vedha Detected" if vedhas else "Calm / No Critical Vedha")
    }
