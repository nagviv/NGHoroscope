def compute_d9_navamsha(longitude: float) -> int:
    """Calculates the Navamsha sign (0-11) based on elemental triplicity."""
    normalized_lon = longitude % 360.0
    rashi_idx = int(normalized_lon // 30)
    element = rashi_idx % 4
    
    if element == 0:    # Fiery (Aries, Leo, Sag) -> starts at Aries
        start_sign = 0
    elif element == 1:  # Earthy (Taurus, Virgo, Cap) -> starts at Capricorn
        start_sign = 9
    elif element == 2:  # Airy (Gemini, Libra, Aqua) -> starts at Libra
        start_sign = 6
    else:               # Watery (Cancer, Scorpio, Pisces) -> starts at Cancer
        start_sign = 3
        
    nav_index_in_sign = int((normalized_lon % 30) // (30.0 / 9.0))
    return (start_sign + nav_index_in_sign) % 12


def compute_d10_dashamsha(longitude: float) -> int:
    """Calculates the Dashamsha sign (0-11) for career analysis."""
    normalized_lon = longitude % 360.0
    rashi_idx = int(normalized_lon // 30)
    dashamsha_part = int((normalized_lon % 30) // 3.0)
    
    # Odd signs start from the sign itself; Even signs start from the 9th house from sign
    if (rashi_idx % 2) == 0:  # Odd sign (0-indexed: 0=Aries, 2=Gemini, etc.)
        start_sign = rashi_idx
    else:                     # Even sign
        start_sign = (rashi_idx + 8) % 12
        
    return (start_sign + dashamsha_part) % 12
