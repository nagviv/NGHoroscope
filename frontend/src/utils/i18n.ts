export type Language = 'en' | 'hi' | 'te' | 'ta' | 'sa';

export const translations: Record<Language, Record<string, string>> = {
  en: {
    appTitle: "JYOTISH PLATFORM",
    subtitle: "Vedic, Jaimini, KP & Muhurta Suite",
    exportPdf: "Export PDF",
    parashara: "Parashara",
    kp: "KP System",
    jaimini: "Jaimini",
    muhurta: "Muhurta"
  },
  hi: {
    appTitle: "ज्योतिष मंच",
    subtitle: "वैदिक, जैमिनी, केपी एवं मुहूर्त प्रणाली",
    exportPdf: "पीडीएफ निर्यात",
    parashara: "पाराशरी",
    kp: "केपी पद्धति",
    jaimini: "जैमिनी",
    muhurta: "मुहूर्त"
  },
  te: {
    appTitle: "జ్యోతిష వేదిక",
    subtitle: "పరాశర, జైమిని, కేపీ మరియు ముహూర్త విధానం",
    exportPdf: "పీడీఎఫ్ డౌన్‌లోడ్",
    parashara: "పరాశర",
    kp: "కేపీ పద్ధతి",
    jaimini: "జైమిని",
    muhurta: "ముహూర్తం"
  },
  ta: {
    appTitle: "ஜோதிட தளம்",
    subtitle: "வேத, ஜைமினி, கேபி மற்றும் முகூர்த்தம்",
    exportPdf: "பிடிஎஃப் பதிவிறக்கம்",
    parashara: "பராசர",
    kp: "கேபி முறை",
    jaimini: "ஜைமினி",
    muhurta: "முகூர்த்தம்"
  },
  sa: {
    appTitle: "ज्योतिषशास्त्रम्",
    subtitle: "पाराशरीय-जैमिनीय-केपी-मुहूर्तविधानम्",
    exportPdf: "विवरणपत्रम्",
    parashara: "पाराशरी",
    kp: "केपीपद्धतिः",
    jaimini: "जैमिनी",
    muhurta: "शुभमुहूर्तः"
  }
};
