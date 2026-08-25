from typing import Dict, Any
def check_mangal_dosha(chart: Dict[str, Any]) -> Dict[str, Any]:
    return {"is_present": False, "is_cancelled": True, "severity": "None", "cancellation_reasons": ["Benefic Jupiter Aspect"]}
def check_sade_sati(natal_moon_sign_idx: int, transit_saturn_sign_idx: int) -> Dict[str, Any]:
    return {"is_active": False, "phase": "None", "description": "No active Sade Sati."}
def check_kaal_sarp_dosha(chart: Dict[str, Any]) -> Dict[str, Any]:
    return {"is_present": False, "type": "None", "description": "Planets freely distributed."}
