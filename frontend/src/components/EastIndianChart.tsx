import React from 'react';
import { NatalChartResponse } from '../types/astrology';

const ZODIAC_SIGNS = ["Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo", "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"];

export const EastIndianChart: React.FC<{ chart: NatalChartResponse }> = ({ chart }) => {
  const signPlanets: Record<string, string[]> = {};
  ZODIAC_SIGNS.forEach(sign => { signPlanets[sign] = []; });

  if (chart?.planets) {
    Object.entries(chart.planets).forEach(([name, data]) => {
      if (signPlanets[data.sign]) {
        signPlanets[data.sign].push(name.substring(0, 2).toUpperCase());
      }
    });
  }

  return (
    <div className="w-full max-w-[420px] aspect-square mx-auto bg-slate-900 rounded-2xl p-3 border border-amber-500/30 shadow-lg flex flex-col items-center justify-center">
      <div className="text-xs font-cinzel font-bold text-amber-400 mb-2">
        East Indian Chart (Diagonal Style)
      </div>
      <div className="w-full h-full border-2 border-amber-500 bg-slate-950 relative grid grid-cols-3 grid-rows-3 text-amber-300 text-xs">
        {/* Center Box */}
        <div className="col-start-2 row-start-2 border border-amber-500/50 flex items-center justify-center text-center p-2">
          <span className="text-[10px] font-bold text-amber-400">EAST<br/>CHART</span>
        </div>
        {/* Render zodiac signs around the corners */}
        {ZODIAC_SIGNS.map((sign, idx) => {
          const isLagna = chart?.ascendant?.sign === sign;
          return (
            <div key={idx} className="border border-amber-500/40 p-1 flex flex-col justify-between">
              <span className="text-[9px] font-bold text-amber-400">{sign.substring(0, 3)} {isLagna ? '(ASC)' : ''}</span>
              <span className="text-[9px] text-emerald-400 font-semibold">{signPlanets[sign]?.join(', ')}</span>
            </div>
          );
        })}
      </div>
    </div>
  );
};