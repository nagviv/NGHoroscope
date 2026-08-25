import React, { useState, useEffect } from 'react';
import { NatalChartResponse } from './types/astrology';
import { NorthIndianChart } from './components/NorthIndianChart';
import { SouthIndianChart } from './components/SouthIndianChart';
import { EastIndianChart } from './components/EastIndianChart';
import { AIQuestionPanel } from './components/AIQuestionPanel';

export default function App() {
  const [formData] = useState({ year: 1995, month: 8, day: 15, hour: 14, minute: 30, second: 0, timezone_offset: 5.5, latitude: 17.3850, longitude: 78.4867 });
  const [chartStyle, setChartStyle] = useState<'North' | 'South' | 'East'>('North');
  const [chartData, setChartData] = useState<NatalChartResponse | null>(null);

  useEffect(() => {
    fetch('/api/v1/chart/natal', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(formData) })
      .then(res => res.json())
      .then(data => setChartData(data));
  }, []);

  return (
    <div className="min-h-screen bg-slate-950 text-slate-100 p-6 max-w-7xl mx-auto space-y-8">
      <header className="flex justify-between items-center pb-6 border-b border-slate-800">
        <h1 className="text-3xl font-cinzel font-bold text-amber-400">JYOTISH AI PLATFORM</h1>
        <div className="flex gap-2 bg-slate-900 p-1 rounded-xl border border-slate-800 text-xs">
          {(['North', 'South', 'East'] as const).map(s => (
            <button key={s} onClick={() => setChartStyle(s)} className={`px-3 py-1.5 rounded-lg ${chartStyle === s ? 'bg-amber-500 text-slate-950 font-bold' : 'text-slate-400'}`}>{s}</button>
          ))}
        </div>
      </header>

      <main className="grid grid-cols-1 lg:grid-cols-12 gap-8">
        <div className="lg:col-span-6 space-y-6">
          <div className="bg-slate-900 border border-slate-800 rounded-2xl p-6">
            {chartData ? (
              chartStyle === 'North' ? <NorthIndianChart chart={chartData} /> : chartStyle === 'South' ? <SouthIndianChart chart={chartData} /> : <EastIndianChart chart={chartData} />
            ) : <div>Loading Chart...</div>}
          </div>
        </div>
        <div className="lg:col-span-6">
          <AIQuestionPanel birthDetails={formData} />
        </div>
      </main>
    </div>
  );
}
