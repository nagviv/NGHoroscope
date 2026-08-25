import React from 'react';
import { MuhurtaResponse } from '../types/astrology';
import { Sun } from 'lucide-react';

export const MuhurtaPanel: React.FC<{ data: MuhurtaResponse }> = ({ data }) => {
  return (
    <div className="bg-slate-900 border border-amber-500/30 rounded-2xl p-6 space-y-4">
      <h3 className="text-lg font-bold font-cinzel text-amber-300 flex items-center gap-2">
        <Sun className="w-5 h-5 text-amber-400" /> Elective Muhurta
      </h3>
      <div className="grid grid-cols-2 gap-2 text-xs">
        {data.choghadiya_day.slice(0, 4).map((c, i) => (
          <div key={i} className="bg-slate-950 p-2 rounded-lg border border-slate-800 flex justify-between">
            <span className="font-bold text-slate-200">{c.name}</span>
            <span className="text-slate-400">{c.start_time}-{c.end_time}</span>
          </div>
        ))}
      </div>
    </div>
  );
};
