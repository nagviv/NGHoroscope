import React from 'react';
import { NatalChartResponse } from '../types/astrology';

const ZODIAC_SIGNS = ["Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo", "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"];

export const SouthIndianChart: React.FC<{ chart: NatalChartResponse }> = ({ chart }) => {
  const signPlanets: Record<string, string[]> = {};
  ZODIAC_SIGNS.forEach(sign => { signPlanets[sign] = []; });

  if (chart?.planets) {
    Object.entries(chart.planets).forEach(([name, data]) => {
      if (signPlanets[data.sign]) {
        signPlanets[data.sign].push(name.substring(0, 2).toUpperCase());
      }
    });
  }

  // South Indian grid fixed sign positions layout
  const gridSigns = [
    ["Pisces", "Aries", "Taurus", "Gemini"],
    ["Aquarius", "", "", "Cancer"],
    ["Capricorn", "", "", "Leo"],
    ["Sagittarius", "Scorpio", "Libra", "Virgo"]
  ];

  return (
    <div className="w-full max-w-[420px] aspect-square mx-auto bg-slate-900 rounded-2xl p-3 border border-amber-500/30 shadow-lg flex flex-col items-center justify-center">
      <div className="text-xs font-cinzel font-bold text-amber-400 mb-2">
        South Indian Chart (Fixed Zodiac Grid)
      </div>
      <div className="w-full h-full grid grid-cols-4 grid-rows-4 border border-amber-500 bg-slate-950 text-amber-300 text-xs">
        {gridSigns.flat().map((sign, idx) => {
          if (!sign) return <div key={idx} className="border border-amber-500/40 bg-slate-900/50" />;
          const isLagna = chart?.ascendant?.sign === sign;
          return (
            <div key={idx} className={`border border-amber-500/50 p-1.5 flex flex-col justify-between relative ${isLagna ? 'bg-amber-500/10' : ''}`}>
              <div className="flex justify-between items-center text-[10px]">
                <span className="font-bold text-amber-400">{sign.substring(0, 3)}</span>
                {isLagna && <span className="bg-amber-500 text-slate-950 font-bold px-1 rounded text-[8px]">ASC</span>}
              </div>
              <div className="text-emerald-400 font-semibold text-[10px] space-x-1">
                {signPlanets[sign]?.join(', ')}
              </div>
            </div>
          );
        })}
      </div>
    </div>
  );
};