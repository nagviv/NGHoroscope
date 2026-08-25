from typing import Dict, Any

VARNA_ORDER = {
    "Pisces": 3, "Cancer": 3, "Scorpio": 3,     # Brahmin
    "Aries": 2, "Leo": 2, "Sagittarius": 2,     # Kshatriya
    "Taurus": 1, "Virgo": 1, "Capricorn": 1,    # Vaishya
    "Gemini": 0, "Libra": 0, "Aquarius": 0      # Shudra
}

NADI_MAP = {
    0: "Adi", 1: "Madhya", 2: "Antya",
    3: "Antya", 4: "Madhya", 5: "Adi",
    6: "Adi", 7: "Madhya", 8: "Antya",
    9: "Antya", 10: "Madhya", 11: "Adi",
    12: "Adi", 13: "Madhya", 14: "Antya",
    15: "Antya", 16: "Madhya", 17: "Adi",
    18: "Adi", 19: "Madhya", 20: "Antya",
    21: "Antya", 22: "Madhya", 23: "Adi",
    24: "Adi", 25: "Madhya", 26: "Antya"
}

GANA_MAP = {
    0: "Deva", 1: "Manushya", 2: "Rakshasa",
    3: "Deva", 4: "Deva", 5: "Manushya",
    6: "Deva", 7: "Deva", 8: "Rakshasa",
    9: "Rakshasa", 10: "Manushya", 11: "Manushya",
    12: "Deva", 13: "Rakshasa", 14: "Deva",
    15: "Rakshasa", 16: "Deva", 17: "Rakshasa",
    18: "Rakshasa", 19: "Manushya", 20: "Manushya",
    21: "Deva", 22: "Rakshasa", 23: "Rakshasa",
    24: "Rakshasa", 25: "Manushya", 26: "Deva"
}

def calculate_ashtakoota(
    bride_moon_sign: str, bride_nak_idx: int,
    groom_moon_sign: str, groom_nak_idx: int
) -> Dict[str, Any]:
    """Computes full 36-point Ashtakoota compatibility table."""
    scores = {}
    
    # 1. Varna (Max 1 point)
    v_b = VARNA_ORDER.get(bride_moon_sign, 0)
    v_g = VARNA_ORDER.get(groom_moon_sign, 0)
    scores["Varna"] = {"obtained": 1.0 if v_g >= v_b else 0.0, "max": 1.0}
    
    # 2. Vashya (Max 2 points)
    scores["Vashya"] = {"obtained": 2.0 if bride_moon_sign == groom_moon_sign else 1.0, "max": 2.0}
    
    # 3. Tara (Max 3 points)
    tara_dist_1 = ((groom_nak_idx - bride_nak_idx) % 9)
    tara_dist_2 = ((bride_nak_idx - groom_nak_idx) % 9)
    auspicious_taras = [1, 2, 4, 6, 8]
    tara_score = 0.0
    if tara_dist_1 in auspicious_taras:
        tara_score += 1.5
    if tara_dist_2 in auspicious_taras:
        tara_score += 1.5
    scores["Tara"] = {"obtained": tara_score, "max": 3.0}
    
    # 4. Yoni (Max 4 points)
    yoni_match = 4.0 if (bride_nak_idx % 14) == (groom_nak_idx % 14) else 2.5
    scores["Yoni"] = {"obtained": yoni_match, "max": 4.0}
    
    # 5. Graha Maitri (Max 5 points)
    scores["Graha_Maitri"] = {"obtained": 5.0 if bride_moon_sign == groom_moon_sign else 3.5, "max": 5.0}
    
    # 6. Gana (Max 6 points)
    g_b = GANA_MAP.get(bride_nak_idx, "Manushya")
    g_g = GANA_MAP.get(groom_nak_idx, "Manushya")
    if g_b == g_g:
        gana_score = 6.0
    elif (g_b == "Deva" and g_g == "Manushya") or (g_b == "Manushya" and g_g == "Deva"):
        gana_score = 4.0
    elif g_b == "Rakshasa" or g_g == "Rakshasa":
        gana_score = 0.0
    else:
        gana_score = 1.5
    scores["Gana"] = {"obtained": gana_score, "max": 6.0}
    
    # 7. Bhakoot (Max 7 points)
    sign_dist = (VARNA_ORDER.get(groom_moon_sign, 0) - VARNA_ORDER.get(bride_moon_sign, 0)) % 12
    # Inauspicious 6/8 (Shadashtak) or 2/12 (Dwirdwadash)
    if sign_dist in [6, 8, 2, 12]:
        bhakoot_score = 0.0
    else:
        bhakoot_score = 7.0
    scores["Bhakoot"] = {"obtained": bhakoot_score, "max": 7.0}
    
    # 8. Nadi (Max 8 points)
    n_b = NADI_MAP.get(bride_nak_idx, "Madhya")
    n_g = NADI_MAP.get(groom_nak_idx, "Madhya")
    nadi_score = 0.0 if n_b == n_g else 8.0
    scores["Nadi"] = {"obtained": nadi_score, "max": 8.0, "bride_nadi": n_b, "groom_nadi": n_g}
    
    total_obtained = sum(v["obtained"] for v in scores.values())
    
    return {
        "total_score": round(total_obtained, 1),
        "maximum_score": 36.0,
        "is_recommended": total_obtained >= 18.0 and nadi_score > 0,
        "breakdown": scores
    }
