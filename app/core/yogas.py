from typing import Dict, Any, List
from app.core.constants import RASHIS, RASHI_LORDS, PLANET_DIGNITIES

def detect_yogas(chart: Dict[str, Any]) -> List[Dict[str, Any]]:
    """Evaluates and identifies classical Vedic Yogas present in the chart."""
    yogas = []
    planets = chart["planets"]
    asc = chart["ascendant"]
    
    # Helper getters
    def get_house_lord(house_num: int) -> str:
        rashi_idx = (asc["sign_index"] + (house_num - 1)) % 12
        return RASHI_LORDS[rashi_idx]
    
    def is_kendra(h: int) -> bool:
        return h in [1, 4, 7, 10]
    
    def is_trikona(h: int) -> bool:
        return h in [1, 5, 9]

    # 1. Gajakesari Yoga: Jupiter in Kendra (1,4,7,10) from Moon
    moon_house = planets["Moon"]["house"]
    jup_house = planets["Jupiter"]["house"]
    dist_from_moon = ((jup_house - moon_house) % 12) + 1
    if dist_from_moon in [1, 4, 7, 10]:
        yogas.append({
            "name": "Gajakesari Yoga",
            "category": "Auspicious / Wisdom & Fame",
            "description": "Jupiter is in a Kendra from the Moon, bestowing intelligence, enduring reputation, and virtuous character."
        })

    # 2. Budhaditya Yoga: Sun and Mercury conjunction
    if planets["Sun"]["house"] == planets["Mercury"]["house"]:
        yogas.append({
            "name": "Budhaditya Yoga",
            "category": "Intellect & Professional Acumen",
            "description": "Conjunction of Sun and Mercury in house {house} conferring analytical prowess and leadership skills.".format(
                house=planets["Sun"]["house"]
            )
        })

    # 3. Pancha Mahapurusha Yogas (Mars, Mercury, Jupiter, Venus, Saturn in Kendra & Own/Exalted)
    mahapurushas = {
        "Mars": ("Ruchaka Yoga", "Physical courage, executive leadership, property dominance"),
        "Mercury": ("Bhadra Yoga", "Intellectual genius, eloquence, exceptional discernment"),
        "Jupiter": ("Hamsa Yoga", "Spiritual wisdom, nobility, moral reverence"),
        "Venus": ("Malavya Yoga", "Refined artistic tastes, luxury, charm, prosperous relationships"),
        "Saturn": ("Sasa Yoga", "Command over masses, enduring perseverance, strategic authority")
    }
    
    for p_name, (yoga_name, y_desc) in mahapurushas.items():
        p_data = planets[p_name]
        dignity = PLANET_DIGNITIES[p_name]
        if is_kendra(p_data["house"]):
            if p_data["sign_index"] == dignity["exalted"] or p_data["sign_index"] in dignity["own"]:
                yogas.append({
                    "name": yoga_name,
                    "category": "Pancha Mahapurusha Yoga",
                    "description": f"{p_name} placed in Kendra in its exalted/own sign, conferring {y_desc}."
                })

    # 4. Chandra Mangala Yoga: Moon and Mars conjunction
    if planets["Moon"]["house"] == planets["Mars"]["house"]:
        yogas.append({
            "name": "Chandra Mangala Yoga",
            "category": "Wealth & Enterprise",
            "description": "Conjunction of Moon and Mars creates strong financial instincts and commercial drive."
        })

    # 5. Kendra-Trikona Raja Yoga (Relationship between Kendra & Trikona Lords)
    lord_4 = get_house_lord(4)
    lord_5 = get_house_lord(5)
    lord_9 = get_house_lord(9)
    lord_10 = get_house_lord(10)
    
    # Check 9th & 10th lord connection (Dharma-Karmadhipati Yoga)
    if planets[lord_9]["house"] == planets[lord_10]["house"]:
        yogas.append({
            "name": "Dharma-Karmadhipati Raja Yoga",
            "category": "High Executive Raja Yoga",
            "description": f"9th lord ({lord_9}) and 10th lord ({lord_10}) are conjoined, signifying exceptional career eminence."
        })
        
    # Check 4th & 5th lord connection
    if lord_4 != lord_5 and planets[lord_4]["house"] == planets[lord_5]["house"]:
        yogas.append({
            "name": "Kendra-Trikona Raja Yoga",
            "category": "Raja Yoga",
            "description": f"4th lord ({lord_4}) and 5th lord ({lord_5}) combine, granting status, education, and prosperity."
        })

    # 6. Viparita Raja Yogas (Dusthana lords in Dusthanas 6, 8, 12)
    lord_6 = get_house_lord(6)
    lord_8 = get_house_lord(8)
    lord_12 = get_house_lord(12)
    
    if planets[lord_6]["house"] in [6, 8, 12]:
        yogas.append({
            "name": "Harsha Yoga (Viparita)",
            "category": "Viparita Raja Yoga",
            "description": f"6th lord ({lord_6}) in a Dusthana creates resilience against adversaries and financial triumph over obstacles."
        })
    if planets[lord_8]["house"] in [6, 8, 12]:
        yogas.append({
            "name": "Sarala Yoga (Viparita)",
            "category": "Viparita Raja Yoga",
            "description": f"8th lord ({lord_8}) in a Dusthana grants longevity, sudden unexpected gains, and composure under pressure."
        })
    if planets[lord_12]["house"] in [6, 8, 12]:
        yogas.append({
            "name": "Vimala Yoga (Viparita)",
            "category": "Viparita Raja Yoga",
            "description": f"12th lord ({lord_12}) in a Dusthana creates independence, frugal wealth preservation, and honorable standing."
        })

    return yogas
