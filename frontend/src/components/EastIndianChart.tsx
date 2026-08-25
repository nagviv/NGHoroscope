import React from 'react';
import { NatalChartResponse } from '../types/astrology';

// East Indian (Bengali/Odia style) Chart Renderer with diagonal quadrant layout
export const EastIndianChart: React.FC<{ chart: NatalChartResponse }> = ({ chart }) => {
  const ascSignIdx = chart.ascendant.sign_index;
  const housePlanets: Record<number, string[]> = { 1:[],2:[],3:[],4:[],5:[],6:[],7:[],8:[],9:[],10:[],11:[],12:[] };

  Object.entries(chart.planets).forEach(([pName, pData]) => {
    housePlanets[pData.house]?.push(pName.slice(0, 2));
  });

  const getSign = (h: number) => ((ascSignIdx + (h - 1)) % 12) + 1;

  return (
    <div className="w-full max-w-[400px] aspect-square mx-auto bg-slate-900 rounded-xl p-2 border border-amber-500/30">
      <svg viewBox="0 0 400 400" className="w-full h-full stroke-amber-400 stroke-1.5 fill-none">
        <rect x="10" y="10" width="380" height="380" className="stroke-amber-500 stroke-2" />
        {/* Diagonal Cross */}
        <line x1="10" y1="10" x2="390" y2="390" />
        <line x1="390" y1="10" x2="10" y2="390" />
        {/* Inner Square */}
        <rect x="110" y="110" width="180" height="180" className="stroke-amber-400 stroke-2" />
        
        {/* Top House */}
        <text x="200" y="60" className="fill-amber-400 text-xs font-bold" textAnchor="middle">{getSign(1)}</text>
        <text x="200" y="85" className="fill-amber-200 text-xs" textAnchor="middle">{housePlanets[1].join(' ')}</text>

        {/* Left House */}
        <text x="60" y="205" className="fill-amber-400 text-xs font-bold" textAnchor="middle">{getSign(4)}</text>
        <text x="60" y="225" className="fill-amber-200 text-xs" textAnchor="middle">{housePlanets[4].join(' ')}</text>

        {/* Bottom House */}
        <text x="200" y="340" className="fill-amber-400 text-xs font-bold" textAnchor="middle">{getSign(7)}</text>
        <text x="200" y="360" className="fill-amber-200 text-xs" textAnchor="middle">{housePlanets[7].join(' ')}</text>

        {/* Right House */}
        <text x="340" y="205" className="fill-amber-400 text-xs font-bold" textAnchor="middle">{getSign(10)}</text>
        <text x="340" y="225" className="fill-amber-200 text-xs" textAnchor="middle">{housePlanets[10].join(' ')}</text>
      </svg>
    </div>
  );
};
