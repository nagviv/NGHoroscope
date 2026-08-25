export interface EntityPosition {
  longitude: number;
  sign: string;
  sign_index: number;
  degree_in_sign: number;
  nakshatra: string;
  pada: number;
  d9_sign: string;
  d10_sign: string;
}

export interface PlanetPosition extends EntityPosition {
  is_retrograde: boolean;
  speed: number;
  house: number;
}

export interface MahadashaItem {
  lord: string;
  start_date: string;
  end_date: string;
  duration_years: number;
  is_balance: boolean;
}

export interface NatalChartResponse {
  ascendant: EntityPosition;
  planets: Record<string, PlanetPosition>;
  vargas: Record<string, Record<string, string>>;
  vimshottari_dasha: MahadashaItem[];
  yogas: { name: string; category: string; description: string }[];
  doshas: {
    mangal_dosha: { is_present: boolean; severity: string };
    sade_sati: { is_active: boolean; phase: string };
    kaal_sarp: { is_present: boolean; type: string };
  };
  ashtakavarga: { total_bindus: number; sav_by_rashi: Record<string, number> };
  shadbala: Record<string, { total_virupas: number; total_rupas: number; strength_ratio: number; is_strong: boolean }>;
}

export interface JaiminiResponse {
  karakas: Record<string, { planet: string; degree_in_sign: number; sign: string; d9_sign: string; house: number; signification: string }>;
  atmakaraka_planet: string;
  karakamsha_sign: string;
  arudha_lagna: { house: number; sign: string };
  chara_dasha: { sign: string; lord: string; duration_years: number; start_date: string; end_date: string }[];
}

export interface KPCusp {
  cusp: number;
  longitude: number;
  degree_in_sign: number;
  sign: string;
  sign_lord: string;
  star_lord: string;
  sub_lord: string;
}

export interface KPPlanet {
  longitude: number;
  degree_in_sign: number;
  sign: string;
  sign_lord: string;
  star_lord: string;
  sub_lord: string;
  kp_house: number;
}

export interface KPResponse {
  cusps: KPCusp[];
  planets: Record<string, KPPlanet>;
  ruling_planets: Record<string, string>;
}

export interface MuhurtaResponse {
  target_date: string;
  choghadiya_day: { name: string; nature: string; quality: string; start_time: string; end_time: string }[];
  horas: { hora_number: number; lord: string; start_time: string; end_time: string; suitability: string }[];
  special_spans: Record<string, any>;
  activity_suitability: Record<string, { score: number; verdict: string }>;
}

export interface KakshyaResponse {
  transit_date: string;
  kakshya_transits: Record<string, {
    sign: string;
    degree_in_sign: number;
    kakshya_number: number;
    kakshya_lord: string;
    kakshya_span: string;
    fructification_status: string;
  }>;
}

export interface VarshaphalaResponse {
  target_year: number;
  solar_return_date: string;
  varsha_ascendant: EntityPosition;
  varsha_planets: Record<string, PlanetPosition>;
  muntha: { sign: string; lord: string; completed_years: number };
  varsheshwara: string;
  tajika_yogas: { name: string; planets: string; nature: string; description: string }[];
}

export interface SBCResponse {
  transit_date: string;
  sensitive_nakshatras: Record<string, string>;
  active_vedhas: { planet: string; transit_nakshatra: string; target: string; vedha_type: string }[];
  defense_verdict: string;
}

export interface KotaResponse {
  transit_date: string;
  kota_swami: string;
  fortress_zones: Record<string, string[]>;
  defense_status: string;
}

export interface ProgressionResponse {
  target_year: number;
  progressed_age: number;
  solar_arc_degrees: number;
  progressed_planets: Record<string, PlanetPosition>;
  solar_arc_planets: Record<string, { longitude: number; sign: string; degree_in_sign: number }>;
  progressed_aspects: { progressed_planet: string; natal_planet: string; aspect: string; angle: number; orb: number; signification: string }[];
}

export interface MatchMakingResponse {
  ashtakoota: {
    total_score: number;
    maximum_score: number;
    is_recommended: boolean;
    breakdown: Record<string, { obtained: number; max: number }>;
  };
  bride_mangal_dosha: Record<string, any>;
  groom_mangal_dosha: Record<string, any>;
  overall_compatibility: string;
}

export interface SavedProfile {
  id: number;
  name: string;
  relationship_label: string;
  year: number;
  month: number;
  day: number;
  hour: number;
  minute: number;
  second: number;
  timezone_offset: number;
  latitude: number;
  longitude: number;
  location_name: string;
}

export interface AIAnswerResponse {
  question: string;
  category: string;
  active_dasha: { mahadasha: string; antardasha: string };
  astrological_factors: string[];
  analysis: string;
  practical_remedies: string[];
}
