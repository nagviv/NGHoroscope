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

export interface AIAnswerResponse {
  question: string;
  category: string;
  active_dasha: { mahadasha: string; antardasha: string };
  astrological_factors: string[];
  analysis: string;
  practical_remedies: string[];
}
