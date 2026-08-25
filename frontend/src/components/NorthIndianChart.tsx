import React from 'react';
import { NatalChartResponse } from '../types/astrology';

export const NorthIndianChart: React.FC<{ chart: NatalChartResponse }> = ({ chart }) => (
  <div className="w-full max-w-[400px] aspect-square mx-auto bg-slate-900 rounded-xl p-2 border border-amber-500/30">
    <svg viewBox="0 0 400 400" className="w-full h-full stroke-amber-400 stroke-1.5 fill-none">
      <rect x="10" y="10" width="380" height="380" className="stroke-amber-500 stroke-2" />
      <line x1="10" y1="10" x2="390" y2="390" /><line x1="390" y1="10" x2="10" y2="390" />
      <polygon points="200,10 390,200 200,390 10,200" className="stroke-amber-400 stroke-2" />
    </svg>
  </div>
);
