export type Language = 'en' | 'hi' | 'te' | 'ta' | 'sa';

export const translations: Record<Language, Record<string, string>> = {
  en: {
    appTitle: "JYOTISH PLATFORM",
    subtitle: "Parashara, Jaimini, KP, Tajika, Sarvatobhadra & Kota Chakra",
    exportPdf: "Export PDF",
    parashara: "Parashara",
    kp: "KP System",
    jaimini: "Jaimini",
    muhurta: "Muhurta",
    kakshya: "Kakshya",
    synastry: "Matchmaking",
    varshaphala: "Varshaphala",
    chakras: "Chakras (SBC/Kota)"
  },
  hi: {
    appTitle: "ज्योतिष मंच",
    subtitle: "पाराशरी, जैमिनी, केपी, ताजिक एवं सर्वतोभद्र चक्र",
    exportPdf: "पीडीएफ निर्यात",
    parashara: "पाराशरी",
    kp: "केपी पद्धति",
    jaimini: "जैमिनी",
    muhurta: "मुहूर्त",
    kakshya: "कक्षा",
    synastry: "कुंडली मिलान",
    varshaphala: "वर्षफल",
    chakras: "सर्वतोभद्र चक्र"
  },
  te: {
    appTitle: "జ్యోతిష వేదిక",
    subtitle: "పరాశర, జైమిని, కేపీ మరియు సర్వతోభద్ర చక్రం",
    exportPdf: "పీడీఎఫ్ డౌన్‌లోడ్",
    parashara: "పరాశర",
    kp: "కేపీ పద్ధతి",
    jaimini: "జైమిని",
    muhurta: "ముహూర్తం",
    kakshya: "కక్ష్య",
    synastry: "పొంతన",
    varshaphala: "వర్షఫలం",
    chakras: "చక్రములు"
  },
  ta: {
    appTitle: "ஜோதிட தளம்",
    subtitle: "வேத, ஜைமினி, கேபி மற்றும் சக்கரங்கள்",
    exportPdf: "பிடிஎஃப் பதிவிறக்கம்",
    parashara: "பராசர",
    kp: "கேபி முறை",
    jaimini: "ஜைமினி",
    muhurta: "முகூர்த்தம்",
    kakshya: "கக்ஷியா",
    synastry: "பொருத்தம்",
    varshaphala: "வருட பலன்",
    chakras: "சக்கரங்கள்"
  },
  sa: {
    appTitle: "ज्योतिषशास्त्रम्",
    subtitle: "पाराशरीय-जैमिनीय-सर्वतोभद्रचक्रविधानम्",
    exportPdf: "विवरणपत्रम्",
    parashara: "पाराशरी",
    kp: "केपीपद्धतिः",
    jaimini: "जैमिनी",
    muhurta: "शुभमुहूर्तः",
    kakshya: "कक्ष्या",
    synastry: "गुणमेलनम्",
    varshaphala: "वर्षफलम्",
    chakras: "चक्रविधानम्"
  }
};
