import React, { useState, useEffect } from 'react';
import { NatalChartResponse, JaiminiResponse, KPResponse, MuhurtaResponse } from './types/astrology';
import { translations, Language } from './utils/i18n';
import { NorthIndianChart } from './components/NorthIndianChart';
import { SouthIndianChart } from './components/SouthIndianChart';
import { EastIndianChart } from './components/EastIndianChart';
import { JaiminiPanel } from './components/JaiminiPanel';
import { KPPanel } from './components/KPPanel';
import { MuhurtaPanel } from './components/MuhurtaPanel';
import { AIQuestionPanel } from './components/AIQuestionPanel';
import { Download, Loader2, Globe } from 'lucide-react';

export default function App() {
  const [lang, setLang] = useState<Language>('en');
  const t = translations[lang];

  const [formData] = useState({
    year: 1995, month: 8, day: 15, hour: 14, minute: 30, second: 0,
    timezone_offset: 5.5, latitude: 17.3850, longitude: 78.4867
  });

  const [activeTab, setActiveTab] = useState<'Parashara' | 'KP' | 'Jaimini' | 'Muhurta'>('Parashara');
  const [chartStyle, setChartStyle] = useState<'North' | 'South' | 'East'>('North');
  const [chartData, setChartData] = useState<NatalChartResponse | null>(null);
  const [jaiminiData, setJaiminiData] = useState<JaiminiResponse | null>(null);
  const [kpData, setKpData] = useState<KPResponse | null>(null);
  const [muhurtaData, setMuhurtaData] = useState<MuhurtaResponse | null>(null);
  const [downloading, setDownloading] = useState(false);

  useEffect(() => {
    fetch('/api/v1/chart/natal', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(formData) })
      .then(res => res.json()).then(data => setChartData(data));
      
    fetch('/api/v1/chart/jaimini', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(formData) })
      .then(res => res.json()).then(data => setJaiminiData(data));

    fetch('/api/v1/chart/kp', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(formData) })
      .then(res => res.json()).then(data => setKpData(data));

    fetch('/api/v1/muhurta/calculate', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify({ year: 2026, month: 8, day: 25, latitude: 17.3850, longitude: 78.4867 }) })
      .then(res => res.json()).then(data => setMuhurtaData(data));
  }, []);

  const downloadPDF = async () => {
    setDownloading(true);
    try {
      const res = await fetch('/api/v1/chart/pdf', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(formData) });
      const blob = await res.blob();
      const url = window.URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.href = url;
      a.download = `Kundli_Report.pdf`;
      document.body.appendChild(a);
      a.click();
      a.remove();
    } finally {
      setDownloading(false);
    }
  };

  return (
    <div className="min-h-screen bg-slate-950 text-slate-100 p-6 max-w-7xl mx-auto space-y-8">
      <header className="flex flex-col md:flex-row justify-between items-center pb-6 border-b border-slate-800 gap-4">
        <div>
          <h1 className="text-3xl font-cinzel font-bold text-amber-400">{t.appTitle}</h1>
          <p className="text-xs text-slate-400 mt-0.5">{t.subtitle}</p>
        </div>
        <div className="flex items-center gap-3">
          {/* Language Selector */}
          <div className="flex items-center gap-1.5 bg-slate-900 border border-slate-800 p-1.5 rounded-xl text-xs">
            <Globe className="w-3.5 h-3.5 text-amber-400 ml-1" />
            <select
              value={lang}
              onChange={(e) => setLang(e.target.value as Language)}
              className="bg-transparent text-slate-200 text-xs focus:outline-none cursor-pointer pr-1"
            >
              <option value="en" className="bg-slate-950">English</option>
              <option value="hi" className="bg-slate-950">हिंदी (Hindi)</option>
              <option value="te" className="bg-slate-950">తెలుగు (Telugu)</option>
              <option value="ta" className="bg-slate-950">தமிழ் (Tamil)</option>
              <option value="sa" className="bg-slate-950">संस्कृतम् (Sanskrit)</option>
            </select>
          </div>

          <button
            onClick={downloadPDF}
            disabled={downloading}
            className="bg-amber-500/20 border border-amber-500/40 hover:bg-amber-500/30 text-amber-300 px-4 py-2 rounded-xl text-xs font-semibold flex items-center gap-2 transition"
          >
            {downloading ? <Loader2 className="w-4 h-4 animate-spin" /> : <Download className="w-4 h-4" />}
            {t.exportPdf}
          </button>
          
          <div className="flex gap-1 bg-slate-900 p-1 rounded-xl border border-slate-800 text-xs">
            {(['Parashara', 'KP', 'Jaimini', 'Muhurta'] as const).map(tab => (
              <button key={tab} onClick={() => setActiveTab(tab)} className={`px-3 py-1.5 rounded-lg ${activeTab === tab ? 'bg-amber-500 text-slate-950 font-bold' : 'text-slate-400'}`}>
                {t[tab.toLowerCase() as keyof typeof t] || tab}
              </button>
            ))}
          </div>
        </div>
      </header>

      <main className="grid grid-cols-1 lg:grid-cols-12 gap-8">
        <div className="lg:col-span-6 space-y-6">
          {activeTab === 'Parashara' && chartData && (
            <div className="bg-slate-900 border border-slate-800 rounded-2xl p-6 space-y-4">
              <div className="flex justify-end gap-1 text-xs">
                {(['North', 'South', 'East'] as const).map(s => (
                  <button key={s} onClick={() => setChartStyle(s)} className={`px-2.5 py-1 rounded ${chartStyle === s ? 'bg-amber-500 text-slate-950 font-bold' : 'text-slate-400'}`}>{s}</button>
                ))}
              </div>
              {chartStyle === 'North' ? <NorthIndianChart chart={chartData} /> : chartStyle === 'South' ? <SouthIndianChart chart={chartData} /> : <EastIndianChart chart={chartData} />}
            </div>
          )}

          {activeTab === 'KP' && kpData && <KPPanel data={kpData} />}
          {activeTab === 'Jaimini' && jaiminiData && <JaiminiPanel data={jaiminiData} />}
          {activeTab === 'Muhurta' && muhurtaData && <MuhurtaPanel data={muhurtaData} />}
        </div>
        <div className="lg:col-span-6 space-y-6">
          <AIQuestionPanel birthDetails={formData} />
        </div>
      </main>
    </div>
  );
}
