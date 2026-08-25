import React from 'react';
import { NatalChartResponse } from '../types/astrology';

export const EastIndianChart: React.FC<{ chart: NatalChartResponse }> = ({ chart }) => {
  return (
    <div className="w-full max-w-[400px] aspect-square mx-auto bg-slate-900 rounded-xl p-2 border border-amber-500/30 flex items-center justify-center">
      <span className="text-amber-400 font-cinzel text-sm">East Indian Chart</span>
    </div>
  );
};
