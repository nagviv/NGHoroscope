import React from 'react';
import { NatalChartResponse } from '../types/astrology';

export const NorthIndianChart: React.FC<{ chart: NatalChartResponse }> = ({ chart }) => {
  const housePlanets: Record<number, string[]> = {};
  for (let i = 1; i <= 12; i++) housePlanets[i] = [];

  if (chart?.planets) {
    Object.entries(chart.planets).forEach(([name, data]) => {
      if (data.house >= 1 && data.house <= 12) {
        housePlanets[data.house].push(name.substring(0, 2).toUpperCase());
      }
    });
  }

  const ascSignIndex = chart?.ascendant?.sign_index ?? 0;

  return (
    <div className="w-full max-w-[420px] aspect-square mx-auto bg-slate-900 rounded-2xl p-3 border border-amber-500/30 shadow-lg flex flex-col items-center justify-center">
      <div className="text-xs font-cinzel font-bold text-amber-400 mb-2">
        North Indian Chart (Lagna: {chart?.ascendant?.sign})
      </div>
      <svg viewBox="0 0 400 400" className="w-full h-full stroke-amber-400 stroke-1.5 fill-none">
        <rect x="10" y="10" width="380" height="380" className="stroke-amber-500 stroke-2" />
        <line x1="10" y1="10" x2="390" y2="390" />
        <line x1="390" y1="10" x2="10" y2="390" />
        <polygon points="200,10 390,200 200,390 10,200" className="stroke-amber-400 stroke-2" />

        {/* House 1 */}
        <text x="200" y="80" className="fill-amber-300 text-[10px] font-bold" textAnchor="middle">{((ascSignIndex) % 12) + 1}</text>
        <text x="200" y="98" className="fill-emerald-400 text-[9px] font-semibold" textAnchor="middle">{housePlanets[1]?.join(', ')}</text>

        {/* House 2 */}
        <text x="110" y="45" className="fill-amber-300 text-[10px] font-bold" textAnchor="middle">{((ascSignIndex + 1) % 12) + 1}</text>
        <text x="110" y="62" className="fill-emerald-400 text-[9px] font-semibold" textAnchor="middle">{housePlanets[2]?.join(', ')}</text>

        {/* House 3 */}
        <text x="45" y="110" className="fill-amber-300 text-[10px] font-bold" textAnchor="middle">{((ascSignIndex + 2) % 12) + 1}</text>
        <text x="45" y="128" className="fill-emerald-400 text-[9px] font-semibold" textAnchor="middle">{housePlanets[3]?.join(', ')}</text>

        {/* House 4 */}
        <text x="80" y="200" className="fill-amber-300 text-[10px] font-bold" textAnchor="middle">{((ascSignIndex + 3) % 12) + 1}</text>
        <text x="80" y="218" className="fill-emerald-400 text-[9px] font-semibold" textAnchor="middle">{housePlanets[4]?.join(', ')}</text>

        {/* House 5 */}
        <text x="45" y="290" className="fill-amber-300 text-[10px] font-bold" textAnchor="middle">{((ascSignIndex + 4) % 12) + 1}</text>
        <text x="45" y="308" className="fill-emerald-400 text-[9px] font-semibold" textAnchor="middle">{housePlanets[5]?.join(', ')}</text>

        {/* House 6 */}
        <text x="110" y="355" className="fill-amber-300 text-[10px] font-bold" textAnchor="middle">{((ascSignIndex + 5) % 12) + 1}</text>
        <text x="110" y="373" className="fill-emerald-400 text-[9px] font-semibold" textAnchor="middle">{housePlanets[6]?.join(', ')}</text>

        {/* House 7 */}
        <text x="200" y="325" className="fill-amber-300 text-[10px] font-bold" textAnchor="middle">{((ascSignIndex + 6) % 12) + 1}</text>
        <text x="200" y="343" className="fill-emerald-400 text-[9px] font-semibold" textAnchor="middle">{housePlanets[7]?.join(', ')}</text>

        {/* House 8 */}
        <text x="290" y="355" className="fill-amber-300 text-[10px] font-bold" textAnchor="middle">{((ascSignIndex + 7) % 12) + 1}</text>
        <text x="290" y="373" className="fill-emerald-400 text-[9px] font-semibold" textAnchor="middle">{housePlanets[8]?.join(', ')}</text>

        {/* House 9 */}
        <text x="355" y="290" className="fill-amber-300 text-[10px] font-bold" textAnchor="middle">{((ascSignIndex + 8) % 12) + 1}</text>
        <text x="355" y="308" className="fill-emerald-400 text-[9px] font-semibold" textAnchor="middle">{housePlanets[9]?.join(', ')}</text>

        {/* House 10 */}
        <text x="320" y="200" className="fill-amber-300 text-[10px] font-bold" textAnchor="middle">{((ascSignIndex + 9) % 12) + 1}</text>
        <text x="320" y="218" className="fill-emerald-400 text-[9px] font-semibold" textAnchor="middle">{housePlanets[10]?.join(', ')}</text>

        {/* House 11 */}
        <text x="355" y="110" className="fill-amber-300 text-[10px] font-bold" textAnchor="middle">{((ascSignIndex + 10) % 12) + 1}</text>
        <text x="355" y="128" className="fill-emerald-400 text-[9px] font-semibold" textAnchor="middle">{housePlanets[11]?.join(', ')}</text>

        {/* House 12 */}
        <text x="290" y="45" className="fill-amber-300 text-[10px] font-bold" textAnchor="middle">{((ascSignIndex + 11) % 12) + 1}</text>
        <text x="290" y="62" className="fill-emerald-400 text-[9px] font-semibold" textAnchor="middle">{housePlanets[12]?.join(', ')}</text>
      </svg>
    </div>
  );
};