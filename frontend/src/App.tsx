import React, { useState, useEffect } from 'react';
import { NatalChartResponse } from './types/astrology';
import { NorthIndianChart } from './components/NorthIndianChart';
import { SouthIndianChart } from './components/SouthIndianChart';
import { AIQuestionPanel } from './components/AIQuestionPanel';
import { Sparkles, Calendar, Clock, MapPin, Orbit, ShieldAlert, Award } from 'lucide-react';

export default function App() {
  const [formData, setFormData] = useState({
    year: 1995,
    month: 8,
    day: 15,
    hour: 14,
    minute: 30,
    second: 0,
    timezone_offset: 5.5,
    latitude: 17.3850,
    longitude: 78.4867
  });

  const [chartStyle, setChartStyle] = useState<'North' | 'South'>('North');
  const [vargaType, setVargaType] = useState<'D1_Rashi' | 'D9_Navamsha' | 'D10_Dashamsha'>('D1_Rashi');
  const [chartData, setChartData] = useState<NatalChartResponse | null>(null);
  const [loading, setLoading] = useState(false);

  const fetchChart = async () => {
    setLoading(true);
    try {
      const res = await fetch('/api/v1/chart/natal', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(formData)
      });
      const data = await res.json();
      setChartData(data);
    } catch (err) {
      console.error('Failed to load chart data:', err);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchChart();
  }, []);

  return (
    <div className="min-h-screen bg-slate-950 text-slate-100 p-4 md:p-8">
      {/* Navigation Header */}
      <header className="max-w-7xl mx-auto flex flex-col md:flex-row justify-between items-center pb-8 border-b border-slate-800 gap-4">
        <div>
          <h1 className="text-3xl font-cinzel font-bold tracking-wide text-transparent bg-clip-text bg-gradient-to-r from-amber-200 via-amber-400 to-amber-500">
            JYOTISH AI
          </h1>
          <p className="text-xs text-slate-400 mt-1">High-Precision Vedic Astrological Calculations & Interpretations</p>
        </div>
        <div className="flex gap-2 bg-slate-900 p-1.5 rounded-xl border border-slate-800 text-xs font-semibold">
          <button
            onClick={() => setChartStyle('North')}
            className={`px-4 py-2 rounded-lg transition ${chartStyle === 'North' ? 'bg-amber-500 text-slate-950 font-bold' : 'text-slate-400 hover:text-white'}`}
          >
            North Indian Style
          </button>
          <button
            onClick={() => setChartStyle('South')}
            className={`px-4 py-2 rounded-lg transition ${chartStyle === 'South' ? 'bg-amber-500 text-slate-950 font-bold' : 'text-slate-400 hover:text-white'}`}
          >
            South Indian Style
          </button>
        </div>
      </header>

      {/* Main Grid */}
      <main className="max-w-7xl mx-auto grid grid-cols-1 lg:grid-cols-12 gap-8 mt-8">
        {/* Left Column: Birth Controls & Charts */}
        <div className="lg:col-span-6 space-y-6">
          {/* Chart Display Container */}
          <div className="bg-slate-900 border border-slate-800 rounded-2xl p-6 shadow-xl space-y-4">
            <div className="flex justify-between items-center">
              <div className="flex gap-2 text-xs font-semibold">
                {(['D1_Rashi', 'D9_Navamsha', 'D10_Dashamsha'] as const).map((v) => (
                  <button
                    key={v}
                    onClick={() => setVargaType(v)}
                    className={`px-3 py-1.5 rounded-lg border transition ${vargaType === v ? 'bg-amber-500/20 border-amber-500 text-amber-300' : 'border-slate-800 text-slate-400'}`}
                  >
                    {v.replace('_', ' ')}
                  </button>
                ))}
              </div>
              <span className="text-[11px] text-amber-400 bg-amber-500/10 px-2.5 py-1 rounded-md border border-amber-500/20">
                Lahiri Ayanamsa
              </span>
            </div>

            {chartData ? (
              chartStyle === 'North' ? (
                <NorthIndianChart chart={chartData} vargaType={vargaType} />
              ) : (
                <SouthIndianChart chart={chartData} />
              )
            ) : (
              <div className="h-[380px] flex items-center justify-center text-slate-500">Calculating Kundli...</div>
            )}
          </div>

          {/* Dasha Timeline */}
          {chartData && (
            <div className="bg-slate-900 border border-slate-800 rounded-2xl p-6 space-y-3">
              <h3 className="text-sm font-bold font-cinzel text-amber-300 flex items-center gap-2">
                <Orbit className="w-4 h-4 text-amber-400" />
                Vimshottari Dasha Timeline (120 Years)
              </h3>
              <div className="grid grid-cols-3 gap-2 text-xs">
                {chartData.vimshottari_dasha.slice(0, 6).map((d, i) => (
                  <div key={i} className="bg-slate-950/80 border border-slate-800 p-2.5 rounded-xl flex flex-col justify-between">
                    <span className="font-bold text-amber-400">{d.lord} Dasha</span>
                    <span className="text-[10px] text-slate-400">{d.start_date.slice(0, 4)} - {d.end_date.slice(0, 4)}</span>
                  </div>
                ))}
              </div>
            </div>
          )}
        </div>

        {/* Right Column: AI Astrologer, Yogas, & Doshas */}
        <div className="lg:col-span-6 space-y-6">
          {/* AI Panel */}
          <AIQuestionPanel birthDetails={formData} />

          {/* Yogas & Doshas Summary */}
          {chartData && (
            <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
              {/* Yogas */}
              <div className="bg-slate-900 border border-slate-800 rounded-2xl p-5 space-y-3">
                <h4 className="text-xs font-bold uppercase tracking-wider text-amber-400 flex items-center gap-2">
                  <Award className="w-4 h-4" />
                  Active Auspicious Yogas
                </h4>
                <div className="space-y-2">
                  {chartData.yogas.map((y, i) => (
                    <div key={i} className="bg-slate-950/60 p-2.5 rounded-lg border border-slate-800/80 text-xs">
                      <div className="font-bold text-amber-200">{y.name}</div>
                      <div className="text-[11px] text-slate-400 mt-0.5">{y.description}</div>
                    </div>
                  ))}
                </div>
              </div>

              {/* Doshas */}
              <div className="bg-slate-900 border border-slate-800 rounded-2xl p-5 space-y-3">
                <h4 className="text-xs font-bold uppercase tracking-wider text-red-400 flex items-center gap-2">
                  <ShieldAlert className="w-4 h-4" />
                  Dosha & Sade Sati Analysis
                </h4>
                <div className="space-y-2 text-xs">
                  <div className="bg-slate-950/60 p-2.5 rounded-lg border border-slate-800/80">
                    <div className="font-bold text-slate-200">Mangal Dosha</div>
                    <div className="text-[11px] text-slate-400">
                      Status: {chartData.doshas.mangal_dosha.is_present ? 'Present' : 'Clear / Cancelled'} ({chartData.doshas.mangal_dosha.severity})
                    </div>
                  </div>
                  <div className="bg-slate-950/60 p-2.5 rounded-lg border border-slate-800/80">
                    <div className="font-bold text-slate-200">Shani Sade Sati</div>
                    <div className="text-[11px] text-slate-400">
                      {chartData.doshas.sade_sati.phase}
                    </div>
                  </div>
                </div>
              </div>
            </div>
          )}
        </div>
      </main>
    </div>
  );
}
