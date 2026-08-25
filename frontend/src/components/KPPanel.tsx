import React from 'react';
import { KPResponse } from '../types/astrology';
import { Layers } from 'lucide-react';

export const KPPanel: React.FC<{ data: KPResponse }> = ({ data }) => {
  return (
    <div className="bg-slate-900 border border-amber-500/30 rounded-2xl p-6 space-y-4">
      <h3 className="text-lg font-bold font-cinzel text-amber-300 flex items-center gap-2">
        <Layers className="w-5 h-5 text-amber-400" /> KP Sub-Lords
      </h3>
      <div className="grid grid-cols-3 gap-2 text-xs">
        {data.cusps.slice(0, 6).map(c => (
          <div key={c.cusp} className="bg-slate-950 p-2 rounded-lg border border-slate-800">
            <span className="text-slate-400 block">Cusp {c.cusp}</span>
            <span className="font-bold text-amber-300">{c.sub_lord}</span>
          </div>
        ))}
      </div>
    </div>
  );
};
