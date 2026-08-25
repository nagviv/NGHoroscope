export type Language = 'en' | 'hi' | 'te' | 'ta' | 'sa';

export const translations: Record<Language, Record<string, string>> = {
  en: {
    appTitle: "JYOTISH PLATFORM",
    subtitle: "Parashara, Jaimini, KP, Tajika Varshaphala & Synastry",
    exportPdf: "Export PDF",
    exportMatchPdf: "Export Synastry PDF",
    parashara: "Parashara",
    kp: "KP System",
    jaimini: "Jaimini",
    muhurta: "Muhurta",
    kakshya: "Kakshya",
    synastry: "Matchmaking",
    varshaphala: "Varshaphala"
  },
  hi: {
    appTitle: "ज्योतिष मंच",
    subtitle: "पाराशरी, जैमिनी, केपी, ताजिक वर्षफल एवं मिलान",
    exportPdf: "पीडीएफ निर्यात",
    exportMatchPdf: "मिलान रिपोर्ट निर्यात",
    parashara: "पाराशरी",
    kp: "केपी पद्धति",
    jaimini: "जैमिनी",
    muhurta: "मुहूर्त",
    kakshya: "कक्षा",
    synastry: "कुंडली मिलान",
    varshaphala: "वर्षफल"
  },
  te: {
    appTitle: "జ్యోతిష వేదిక",
    subtitle: "పరాశర, జైమిని, కేపీ, తాజిక వర్షఫలం మరియు పొంతన",
    exportPdf: "పీడీఎఫ్ డౌన్‌లోడ్",
    exportMatchPdf: "పొంతన పీడీఎఫ్",
    parashara: "పరాశర",
    kp: "కేపీ పద్ధతి",
    jaimini: "జైమిని",
    muhurta: "ముహూర్తం",
    kakshya: "కక్ష్య",
    synastry: "పొంతన",
    varshaphala: "వర్షఫలం"
  },
  ta: {
    appTitle: "ஜோதிட தளம்",
    subtitle: "வேத, ஜைமினி, கேபி மற்றும் ஆண்டு பலன்",
    exportPdf: "பிடிஎஃப் பதிவிறக்கம்",
    exportMatchPdf: "பொருத்தம் பிடிஎஃப்",
    parashara: "பராசர",
    kp: "கேபி முறை",
    jaimini: "ஜைமினி",
    muhurta: "முகூர்த்தம்",
    kakshya: "கக்ஷியா",
    synastry: "பொருத்தம்",
    varshaphala: "வருட பலன்"
  },
  sa: {
    appTitle: "ज्योतिषशास्त्रम्",
    subtitle: "पाराशरीय-जैमिनीय-केपी-ताजिकवर्षफलविधानम्",
    exportPdf: "विवरणपत्रम्",
    exportMatchPdf: "मेलनपत्रम्",
    parashara: "पाराशरी",
    kp: "केपीपद्धतिः",
    jaimini: "जैमिनी",
    muhurta: "शुभमुहूर्तः",
    kakshya: "कक्ष्या",
    synastry: "गुणमेलनम्",
    varshaphala: "वर्षफलम्"
  }
};
