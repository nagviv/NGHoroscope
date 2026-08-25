import React from 'react';
import { NatalChartResponse } from '../types/astrology';

interface Props {
  chart: NatalChartResponse;
}

const RASHIS = [
  "Pisces", "Aries", "Taurus", "Gemini",
  "Cancer", "Leo", "Virgo", "Libra",
  "Scorpio", "Sagittarius", "Capricorn", "Aquarius"
];

// Fixed 4x4 Grid coordinates for South Indian chart signs
const BOX_POSITIONS: Record<string, { col: number; row: number }> = {
  Pisces: { col: 0, row: 0 },
  Aries: { col: 1, row: 0 },
  Taurus: { col: 2, row: 0 },
  Gemini: { col: 3, row: 0 },
  Cancer: { col: 3, row: 1 },
  Leo: { col: 3, row: 2 },
  Virgo: { col: 3, row: 3 },
  Libra: { col: 2, row: 3 },
  Scorpio: { col: 1, row: 3 },
  Sagittarius: { col: 0, row: 3 },
  Capricorn: { col: 0, row: 2 },
  Aquarius: { col: 0, row: 1 }
};

export const SouthIndianChart: React.FC<Props> = ({ chart }) => {
  const signPlanets: Record<string, string[]> = {};
  RASHIS.forEach(r => { signPlanets[r] = []; });

  // Mark Lagna
  signPlanets[chart.ascendant.sign]?.push('Asc / Lag');

  Object.entries(chart.planets).forEach(([pName, pData]) => {
    const label = `${pName.slice(0, 2)}${pData.is_retrograde ? '(R)' : ''}`;
    signPlanets[pData.sign]?.push(label);
  });

  return (
    <div className="w-full max-w-[420px] aspect-square mx-auto bg-slate-900/90 rounded-xl p-2 border border-amber-500/30 grid grid-cols-4 grid-rows-4 gap-1 shadow-2xl">
      {Object.entries(BOX_POSITIONS).map(([rashiName, pos]) => (
        <div
          key={rashiName}
          style={{ gridColumn: pos.col + 1, gridRow: pos.row + 1 }}
          className="border border-amber-500/40 rounded p-1 flex flex-col justify-between bg-slate-950/60 min-h-[85px] hover:border-amber-400 transition"
        >
          <div className="text-[10px] font-bold text-amber-400 uppercase tracking-tighter">
            {rashiName.slice(0, 3)}
          </div>
          <div className="flex flex-wrap gap-1 text-xs text-slate-100 font-medium">
            {signPlanets[rashiName]?.map((p, idx) => (
              <span key={idx} className={p.includes('Asc') ? 'text-amber-300 font-bold' : 'text-slate-200'}>
                {p}
              </span>
            ))}
          </div>
        </div>
      ))}
      {/* Center Box */}
      <div
        style={{ gridColumn: '2 / 4', gridRow: '2 / 4' }}
        className="border border-dashed border-amber-500/20 rounded flex flex-col items-center justify-center bg-slate-900/40 text-center p-2"
      >
        <span className="text-amber-400 font-cinzel font-bold text-sm">Rashi D1</span>
        <span className="text-slate-400 text-[11px] mt-1">Lahiri Nirayana</span>
      </div>
    </div>
  );
};
