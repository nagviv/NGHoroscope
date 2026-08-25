import React from 'react';
import { NatalChartResponse } from '../types/astrology';

const RASHIS = ["Pisces", "Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo", "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius"];
const POS: Record<string, { col: number; row: number }> = {
  Pisces: { col: 0, row: 0 }, Aries: { col: 1, row: 0 }, Taurus: { col: 2, row: 0 }, Gemini: { col: 3, row: 0 },
  Cancer: { col: 3, row: 1 }, Leo: { col: 3, row: 2 }, Virgo: { col: 3, row: 3 }, Libra: { col: 2, row: 3 },
  Scorpio: { col: 1, row: 3 }, Sagittarius: { col: 0, row: 3 }, Capricorn: { col: 0, row: 2 }, Aquarius: { col: 0, row: 1 }
};

export const SouthIndianChart: React.FC<{ chart: NatalChartResponse }> = ({ chart }) => {
  const map: Record<string, string[]> = {};
  RASHIS.forEach(r => { map[r] = []; });
  map[chart.ascendant.sign]?.push('Asc');
  Object.entries(chart.planets).forEach(([p, d]) => map[d.sign]?.push(p.slice(0, 2)));

  return (
    <div className="w-full max-w-[400px] aspect-square mx-auto bg-slate-900 rounded-xl p-2 border border-amber-500/30 grid grid-cols-4 grid-rows-4 gap-1">
      {Object.entries(POS).map(([r, p]) => (
        <div key={r} style={{ gridColumn: p.col + 1, gridRow: p.row + 1 }} className="border border-amber-500/30 rounded p-1 bg-slate-950">
          <div className="text-[10px] font-bold text-amber-400">{r.slice(0, 3)}</div>
          <div className="text-xs text-slate-200">{map[r]?.join(', ')}</div>
        </div>
      ))}
      <div style={{ gridColumn: '2 / 4', gridRow: '2 / 4' }} className="flex items-center justify-center text-amber-400 font-cinzel text-xs">South Indian D1</div>
    </div>
  );
};
