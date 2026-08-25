def compute_d9_navamsha(longitude: float) -> int:
    normalized_lon = longitude % 360.0
    rashi_idx = int(normalized_lon // 30)
    element = rashi_idx % 4
    start_sign = [0, 9, 6, 3][element]
    nav_index_in_sign = int((normalized_lon % 30) // (30.0 / 9.0))
    return (start_sign + nav_index_in_sign) % 12

def compute_d10_dashamsha(longitude: float) -> int:
    normalized_lon = longitude % 360.0
    rashi_idx = int(normalized_lon // 30)
    dashamsha_part = int((normalized_lon % 30) // 3.0)
    start_sign = rashi_idx if (rashi_idx % 2 == 0) else (rashi_idx + 8) % 12
    return (start_sign + dashamsha_part) % 12
