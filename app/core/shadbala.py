from typing import Dict, Any

# Minimum required Shadbala in Rupas for planets to be deemed strong
MIN_SHADBALA_RUPAS = {
    "Sun": 6.5,
    "Moon": 6.0,
    "Mars": 5.0,
    "Mercury": 7.0,
    "Jupiter": 6.5,
    "Venus": 5.5,
    "Saturn": 5.0
}

def calculate_shadbala_summary(chart: Dict[str, Any]) -> Dict[str, Any]:
    """Calculates planetary Shadbala strengths (in Virupas and Rupas)."""
    planets = chart["planets"]
    results = {}
    
    for p_name in ["Sun", "Moon", "Mars", "Mercury", "Jupiter", "Venus", "Saturn"]:
        p_data = planets[p_name]
        house = p_data["house"]
        
        # 1. Sthana Bala (Positional Strength proxy)
        sthana = 120.0
        if house in [1, 4, 7, 10]:
            sthana += 60.0
        elif house in [5, 9]:
            sthana += 45.0
            
        # 2. Dig Bala (Directional Strength proxy)
        dig_bala_best = {"Sun": 10, "Mars": 10, "Jupiter": 1, "Mercury": 1, "Moon": 4, "Venus": 4, "Saturn": 7}
        dig = 60.0 if house == dig_bala_best.get(p_name) else 30.0
        
        # 3. Cheshta Bala (Motional Strength proxy)
        cheshta = 60.0 if p_data.get("is_retrograde", False) else 30.0
        
        # 4. Naisargika Bala (Natural Strength constant)
        naisargika_values = {"Sun": 60.0, "Moon": 51.4, "Venus": 42.8, "Jupiter": 34.3, "Mercury": 25.7, "Mars": 17.1, "Saturn": 8.6}
        naisargika = naisargika_values.get(p_name, 20.0)
        
        total_virupas = sthana + dig + cheshta + naisargika + 100.0  # adding base Kaala/Drik proxy
        total_rupas = round(total_virupas / 60.0, 2)
        required_rupas = MIN_SHADBALA_RUPAS.get(p_name, 5.0)
        
        results[p_name] = {
            "total_virupas": round(total_virupas, 1),
            "total_rupas": total_rupas,
            "required_rupas": required_rupas,
            "strength_ratio": round(total_rupas / required_rupas, 2),
            "is_strong": total_rupas >= required_rupas
        }
        
    return results
