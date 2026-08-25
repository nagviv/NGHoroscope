def compute_d9_navamsha(longitude: float) -> int:
    return int((longitude % 360.0) // 3.3333333) % 12
def compute_d10_dashamsha(longitude: float) -> int:
    return int((longitude % 360.0) // 3.0) % 12
