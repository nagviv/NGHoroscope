export type Language = 'en' | 'hi' | 'te' | 'ta' | 'sa';

export const translations: Record<Language, Record<string, string>> = {
  en: {
    appTitle: "JYOTISH PLATFORM",
    subtitle: "Parashara, Jaimini, KP, Muhurta & Kakshya Timing",
    exportPdf: "Export PDF",
    parashara: "Parashara",
    kp: "KP System",
    jaimini: "Jaimini",
    muhurta: "Muhurta",
    kakshya: "Kakshya Transits"
  },
  hi: {
    appTitle: "ज्योतिष मंच",
    subtitle: "पाराशरी, जैमिनी, केपी, मुहूर्त एवं कक्षक गोचर",
    exportPdf: "पीडीएफ निर्यात",
    parashara: "पाराशरी",
    kp: "केपी पद्धति",
    jaimini: "जैमिनी",
    muhurta: "मुहूर्त",
    kakshya: "कक्षा गोचर"
  },
  te: {
    appTitle: "జ్యోతిష వేదిక",
    subtitle: "పరాశర, జైమిని, కేపీ, ముహూర్తం మరియు కక్ష్య గోచారం",
    exportPdf: "పీడీఎఫ్ డౌన్‌లోడ్",
    parashara: "పరాశర",
    kp: "కేపీ పద్ధతి",
    jaimini: "జైమిని",
    muhurta: "ముహూర్తం",
    kakshya: "కక్ష్య"
  },
  ta: {
    appTitle: "ஜோதிட தளம்",
    subtitle: "பராசர, ஜைமினி, கேபி மற்றும் கக்ஷியா",
    exportPdf: "பிடிஎஃப் பதிவிறக்கம்",
    parashara: "பராசர",
    kp: "கேபி முறை",
    jaimini: "ஜைமினி",
    muhurta: "முகூர்த்தம்",
    kakshya: "கக்ஷியா"
  },
  sa: {
    appTitle: "ज्योतिषशास्त्रम्",
    subtitle: "पाराशरीय-जैमिनीय-केपी-कक्षाविधानम्",
    exportPdf: "विवरणपत्रम्",
    parashara: "पाराशरी",
    kp: "केपीपद्धतिः",
    jaimini: "जैमिनी",
    muhurta: "शुभमुहूर्तः",
    kakshya: "कक्ष्यागोचरः"
  }
};
