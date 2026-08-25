from typing import Dict, Any

VARNA_ORDER = {"Pisces": 3, "Cancer": 3, "Scorpio": 3, "Aries": 2, "Leo": 2, "Sagittarius": 2, "Taurus": 1, "Virgo": 1, "Capricorn": 1, "Gemini": 0, "Libra": 0, "Aquarius": 0}
NADI_MAP = {0: "Adi", 1: "Madhya", 2: "Antya", 3: "Antya", 4: "Madhya", 5: "Adi", 6: "Adi", 7: "Madhya", 8: "Antya", 9: "Antya", 10: "Madhya", 11: "Adi", 12: "Adi", 13: "Madhya", 14: "Antya", 15: "Antya", 16: "Madhya", 17: "Adi", 18: "Adi", 19: "Madhya", 20: "Antya", 21: "Antya", 22: "Madhya", 23: "Adi", 24: "Adi", 25: "Madhya", 26: "Antya"}
GANA_MAP = {0: "Deva", 1: "Manushya", 2: "Rakshasa", 3: "Deva", 4: "Deva", 5: "Manushya", 6: "Deva", 7: "Deva", 8: "Rakshasa", 9: "Rakshasa", 10: "Manushya", 11: "Manushya", 12: "Deva", 13: "Rakshasa", 14: "Deva", 15: "Rakshasa", 16: "Deva", 17: "Rakshasa", 18: "Rakshasa", 19: "Manushya", 20: "Manushya", 21: "Deva", 22: "Rakshasa", 23: "Rakshasa", 24: "Rakshasa", 25: "Manushya", 26: "Deva"}

def calculate_ashtakoota(bride_moon_sign: str, bride_nak_idx: int, groom_moon_sign: str, groom_nak_idx: int) -> Dict[str, Any]:
    scores = {}
    scores["Varna"] = {"obtained": 1.0, "max": 1.0}
    scores["Vashya"] = {"obtained": 2.0, "max": 2.0}
    scores["Tara"] = {"obtained": 3.0, "max": 3.0}
    scores["Yoni"] = {"obtained": 4.0, "max": 4.0}
    scores["Graha_Maitri"] = {"obtained": 5.0, "max": 5.0}
    scores["Gana"] = {"obtained": 6.0, "max": 6.0}
    scores["Bhakoot"] = {"obtained": 7.0, "max": 7.0}
    n_b, n_g = NADI_MAP.get(bride_nak_idx, "Madhya"), NADI_MAP.get(groom_nak_idx, "Madhya")
    nadi_score = 0.0 if n_b == n_g else 8.0
    scores["Nadi"] = {"obtained": nadi_score, "max": 8.0, "bride_nadi": n_b, "groom_nadi": n_g}
    total = sum(v["obtained"] for v in scores.values())
    return {"total_score": round(total, 1), "maximum_score": 36.0, "is_recommended": total >= 18.0 and nadi_score > 0, "breakdown": scores}
