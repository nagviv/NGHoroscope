import React from 'react';
import { KakshyaResponse } from '../types/astrology';
import { Target } from 'lucide-react';

export const KakshyaPanel: React.FC<{ data: KakshyaResponse }> = ({ data }) => {
  return (
    <div className="bg-slate-900 border border-amber-500/30 rounded-2xl p-6 space-y-4">
      <h3 className="text-lg font-bold font-cinzel text-amber-300 flex items-center gap-2">
        <Target className="w-5 h-5 text-amber-400" /> Ashtakavarga Kakshya Timing
      </h3>
      <div className="grid grid-cols-2 gap-2 text-xs">
        {Object.entries(data.kakshya_transits).map(([p, d]) => (
          <div key={p} className="bg-slate-950 p-2.5 rounded-lg border border-slate-800 flex justify-between">
            <span className="font-bold text-slate-200">{p}</span>
            <span className="text-amber-300">{d.kakshya_lord}</span>
          </div>
        ))}
      </div>
    </div>
  );
};
