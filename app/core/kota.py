from datetime import datetime
from typing import Dict, Any, List
from app.core.constants import NAKSHATRAS, RASHI_LORDS
from app.core.ephemeris import compute_chart_raw

def calculate_kota_chakra(birth_dt: datetime, target_dt: datetime, tz_offset: float, lat: float, lon: float) -> Dict[str, Any]:
    """Calculates Kota Chakra (Fort Defense) transit occupancy across Stambha, Madhya, Prakara, and Bahya."""
    natal_chart = compute_chart_raw(birth_dt, tz_offset, lat, lon)
    transit_chart = compute_chart_raw(target_dt, tz_offset, lat, lon)
    
    natal_moon_nak = natal_chart["planets"]["Moon"]["nakshatra"]
    janma_idx = NAKSHATRAS.index(natal_moon_nak)
    
    # Kota Swami (Lord of the Fort) & Kota Pala (Guard of the Fort)
    kota_swami = RASHI_LORDS[natal_chart["planets"]["Moon"]["sign_index"]]
    kota_pala = NAKSHATRAS[(janma_idx + 14) % 27]
    
    # 4 Fortress Zones
    # Stambha (Core Pillar), Madhya (Inner Court), Prakara (Fort Wall), Bahya (Exterior Perimeter)
    fortress_zones = {
        "Stambha (Core Pillar)": [],
        "Madhya (Inner Fortress)": [],
        "Prakara (Fort Wall)": [],
        "Bahya (Exterior Outer)": []
    }
    
    for p_name, p_data in transit_chart["planets"].items():
        t_nak_idx = NAKSHATRAS.index(p_data["nakshatra"])
        dist = (t_nak_idx - janma_idx) % 27
        
        if dist in [0, 1, 2]:
            fortress_zones["Stambha (Core Pillar)"].append(p_name)
        elif dist in [3, 4, 5, 6]:
            fortress_zones["Madhya (Inner Fortress)"].append(p_name)
        elif dist in [7, 8, 9, 10, 11]:
            fortress_zones["Prakara (Fort Wall)"].append(p_name)
        else:
            fortress_zones["Bahya (Exterior Outer)"].append(p_name)
            
    # Evaluation: Malefics in Stambha indicate siege/stress, Benefics indicate defense
    stambha_malefics = [p for p in fortress_zones["Stambha (Core Pillar)"] if p in ["Saturn", "Mars", "Rahu", "Ketu"]]
    defense_status = "Fortress Under High Siege (Health/Vitality Caution)" if stambha_malefics else "Fortress Resilient & Guarded"

    return {
        "transit_date": target_dt.strftime("%Y-%m-%d"),
        "kota_swami": kota_swami,
        "kota_pala_nakshatra": kota_pala,
        "fortress_zones": fortress_zones,
        "stambha_siege_malefics": stambha_malefics,
        "defense_status": defense_status
    }
