from typing import Dict, Any

MIN_SHADBALA_RUPAS = {"Sun": 6.5, "Moon": 6.0, "Mars": 5.0, "Mercury": 7.0, "Jupiter": 6.5, "Venus": 5.5, "Saturn": 5.0}

def calculate_shadbala_summary(chart: Dict[str, Any]) -> Dict[str, Any]:
    planets = chart["planets"]
    results = {}
    for p_name in ["Sun", "Moon", "Mars", "Mercury", "Jupiter", "Venus", "Saturn"]:
        p_data = planets[p_name]
        house = p_data["house"]
        sthana = 180.0 if house in [1, 4, 7, 10] else 120.0
        dig = 60.0 if house in [1, 4, 7, 10] else 30.0
        cheshta = 60.0 if p_data.get("is_retrograde", False) else 30.0
        naisargika = {"Sun": 60.0, "Moon": 51.4, "Venus": 42.8, "Jupiter": 34.3, "Mercury": 25.7, "Mars": 17.1, "Saturn": 8.6}.get(p_name, 20.0)
        total_virupas = sthana + dig + cheshta + naisargika + 100.0
        total_rupas = round(total_virupas / 60.0, 2)
        required_rupas = MIN_SHADBALA_RUPAS.get(p_name, 5.0)
        results[p_name] = {"total_virupas": round(total_virupas, 1), "total_rupas": total_rupas, "required_rupas": required_rupas, "strength_ratio": round(total_rupas / required_rupas, 2), "is_strong": total_rupas >= required_rupas}
    return results
