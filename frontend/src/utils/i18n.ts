export type Language = 'en' | 'hi' | 'te' | 'ta' | 'sa';

export const translations: Record<Language, Record<string, string>> = {
  en: {
    appTitle: "JYOTISH PLATFORM",
    subtitle: "Vedic, Jaimini, KP & Muhurta Suite",
    exportPdf: "Export PDF",
    parashara: "Parashara",
    kp: "KP System",
    jaimini: "Jaimini",
    muhurta: "Muhurta",
    aiAstrologer: "AI Astrologer Q&A",
    choghadiya: "Choghadiya Timetable",
    horas: "Planetary Horas",
    suitability: "Activity Suitability"
  },
  hi: {
    appTitle: "ज्योतिष मंच",
    subtitle: "वैदिक, जैमिनी, केपी एवं मुहूर्त प्रणाली",
    exportPdf: "पीडीएफ निर्यात",
    parashara: "पाराशरी",
    kp: "केपी पद्धति",
    jaimini: "जैमिनी",
    muhurta: "मुहूर्त",
    aiAstrologer: "एआई ज्योतिषी प्रश्नोत्तर",
    choghadiya: "चौघड़िया समय सारणी",
    horas: "ग्रह होरा",
    suitability: "कार्य अनुकूलता"
  },
  te: {
    appTitle: "జ్యోతిష వేదిక",
    subtitle: "పరాశర, జైమిని, కేపీ మరియు ముహూర్త విధానం",
    exportPdf: "పీడీఎఫ్ డౌన్‌లోడ్",
    parashara: "పరాశర",
    kp: "కేపీ పద్ధతి",
    jaimini: "జైమిని",
    muhurta: "ముహూర్తం",
    aiAstrologer: "ఏఐ జ్యోతిష్యుడు",
    choghadiya: "చోఘడియా",
    horas: "గ్రహ హోర",
    suitability: "కార్య అనుకూలత"
  },
  ta: {
    appTitle: "ஜோதிட தளம்",
    subtitle: "வேத, ஜைமினி, கேபி மற்றும் முகூர்த்தம்",
    exportPdf: "பிடிஎஃப் பதிவிறக்கம்",
    parashara: "பராசர",
    kp: "கேபி முறை",
    jaimini: "ஜைமினி",
    muhurta: "முகூர்த்தம்",
    aiAstrologer: "ஏஐ ஜோதிடர்",
    choghadiya: "சோகடியா",
    horas: "கிரக ஹோரை",
    suitability: "நிகழ்வு பொருத்தம்"
  },
  sa: {
    appTitle: "ज्योतिषशास्त्रम्",
    subtitle: "पाराशरीय-जैमिनीय-केपी-मुहूर्तविधानम्",
    exportPdf: "विवरणपत्रम्",
    parashara: "पाराशरी",
    kp: "केपीपद्धतिः",
    jaimini: "जैमिनी",
    muhurta: "शुभमुहूर्तः",
    aiAstrologer: "दैवज्ञ-सम्भाषणम्",
    choghadiya: "चौघटिका",
    horas: "होराचक्रम्",
    suitability: "कार्ययोग्यता"
  }
};
