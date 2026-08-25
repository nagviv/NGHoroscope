export type Language = 'en' | 'hi' | 'te' | 'ta' | 'sa';

export const translations: Record<Language, Record<string, string>> = {
  en: {
    appTitle: "JYOTISH PLATFORM",
    subtitle: "Parashara, Jaimini, KP, Muhurta & Synastry Matchmaking",
    exportPdf: "Export PDF",
    exportMatchPdf: "Export Synastry PDF",
    parashara: "Parashara",
    kp: "KP System",
    jaimini: "Jaimini",
    muhurta: "Muhurta",
    kakshya: "Kakshya",
    synastry: "Matchmaking"
  },
  hi: {
    appTitle: "ज्योतिष मंच",
    subtitle: "पाराशरी, जैमिनी, केपी, मुहूर्त एवं कुंडली मिलान",
    exportPdf: "पीडीएफ निर्यात",
    exportMatchPdf: "मिलान रिपोर्ट निर्यात",
    parashara: "पाराशरी",
    kp: "केपी पद्धति",
    jaimini: "जैमिनी",
    muhurta: "मुहूर्त",
    kakshya: "कक्षा",
    synastry: "कुंडली मिलान"
  },
  te: {
    appTitle: "జ్యోతిష వేదిక",
    subtitle: "పరాశర, జైమిని, కేపీ, ముహూర్తం మరియు జాతక పొంతన",
    exportPdf: "పీడీఎఫ్ డౌన్‌లోడ్",
    exportMatchPdf: "పొంతన పీడీఎఫ్",
    parashara: "పరాశర",
    kp: "కేపీ పద్ధతి",
    jaimini: "జైమిని",
    muhurta: "ముహూర్తం",
    kakshya: "కక్ష్య",
    synastry: "పొంతన"
  },
  ta: {
    appTitle: "ஜோதிட தளம்",
    subtitle: "வேத, ஜைமினி, கேபி மற்றும் திருமண பொருத்தம்",
    exportPdf: "பிடிஎஃப் பதிவிறக்கம்",
    exportMatchPdf: "பொருத்தம் பிடிஎஃப்",
    parashara: "பராசர",
    kp: "கேபி முறை",
    jaimini: "ஜைமினி",
    muhurta: "முகூர்த்தம்",
    kakshya: "கக்ஷியா",
    synastry: "பொருத்தம்"
  },
  sa: {
    appTitle: "ज्योतिषशास्त्रम्",
    subtitle: "पाराशरीय-जैमिनीय-केपी-गुणमेलनविधानम्",
    exportPdf: "विवरणपत्रम्",
    exportMatchPdf: "मेलनपत्रम्",
    parashara: "पाराशरी",
    kp: "केपीपद्धतिः",
    jaimini: "जैमिनी",
    muhurta: "शुभमुहूर्तः",
    kakshya: "कक्ष्या",
    synastry: "गुणमेलनम्"
  }
};
