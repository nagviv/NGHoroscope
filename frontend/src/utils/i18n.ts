export type Language = 'en' | 'hi' | 'te' | 'ta' | 'sa';

export const translations: Record<Language, Record<string, string>> = {
  en: {
    appTitle: "JYOTISH PLATFORM",
    subtitle: "Enterprise Vedic, KP, Jaimini, Tajika & Western Progressions Suite",
    exportPdf: "Export PDF",
    parashara: "Parashara",
    kp: "KP System",
    jaimini: "Jaimini",
    muhurta: "Muhurta",
    kakshya: "Kakshya",
    synastry: "Matchmaking",
    varshaphala: "Varshaphala",
    chakras: "Chakras",
    progressions: "Progressions"
  },
  hi: {
    appTitle: "ज्योतिष मंच",
    subtitle: "पाराशरी, जैमिनी, केपी, ताजिक एवं प्रोग्रेशन",
    exportPdf: "पीडीएफ निर्यात",
    parashara: "पाराशरी",
    kp: "केपी पद्धति",
    jaimini: "जैमिनी",
    muhurta: "मुहूर्त",
    kakshya: "कक्षा",
    synastry: "कुंडली मिलान",
    varshaphala: "वर्षफल",
    chakras: "सर्वतोभद्र चक्र",
    progressions: "प्रोग्रेशन"
  },
  te: {
    appTitle: "జ్యోతిష వేదిక",
    subtitle: "పరాశర, జైమిని, కేపీ మరియు ప్రోగ్రెషన్స్",
    exportPdf: "పీడీఎఫ్ డౌన్‌లోడ్",
    parashara: "పరాశర",
    kp: "కేపీ పద్ధతి",
    jaimini: "జైమిని",
    muhurta: "ముహూర్తం",
    kakshya: "కక్ష్య",
    synastry: "పొంతన",
    varshaphala: "వర్షఫలం",
    chakras: "చక్రములు",
    progressions: "ప్రోగ్రెషన్స్"
  },
  ta: {
    appTitle: "ஜோதிட தளம்",
    subtitle: "வேத, ஜைமினி, கேபி மற்றும் முன்னேற்றங்கள்",
    exportPdf: "பிடிஎஃப் பதிவிறக்கம்",
    parashara: "பராசர",
    kp: "கேபி முறை",
    jaimini: "ஜைமினி",
    muhurta: "முகூர்த்தம்",
    kakshya: "கக்ஷியா",
    synastry: "பொருத்தம்",
    varshaphala: "வருட பலன்",
    chakras: "சக்கரங்கள்",
    progressions: "முன்னேற்றங்கள்"
  },
  sa: {
    appTitle: "ज्योतिषशास्त्रम्",
    subtitle: "पाराशरीय-जैमिनीय-प्रगतिविधानम्",
    exportPdf: "विवरणपत्रम्",
    parashara: "पाराशरी",
    kp: "केपीपद्धतिः",
    jaimini: "जैमिनी",
    muhurta: "शुभमुहूर्तः",
    kakshya: "कक्ष्या",
    synastry: "गुणमेलनम्",
    varshaphala: "वर्षफलम्",
    chakras: "चक्रविधानम्",
    progressions: "प्रगतिः"
  }
};
