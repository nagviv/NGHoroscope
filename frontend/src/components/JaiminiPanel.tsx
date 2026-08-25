import React from 'react';
import { JaiminiResponse } from '../types/astrology';
import { Compass } from 'lucide-react';

export const JaiminiPanel: React.FC<{ data: JaiminiResponse }> = ({ data }) => (
  <div className="bg-slate-900 border border-amber-500/30 rounded-2xl p-6 space-y-4">
    <h3 className="text-lg font-bold font-cinzel text-amber-300 flex items-center gap-2"><Compass className="w-5 h-5 text-amber-400" /> Jaimini Karakas</h3>
    <div className="grid grid-cols-2 gap-2 text-xs">
      {Object.entries(data.karakas).map(([k, v]) => (
        <div key={k} className="bg-slate-950 p-2 rounded-lg border border-slate-800 flex justify-between"><span className="text-amber-400">{k}</span><span className="text-slate-200">{v.planet}</span></div>
      ))}
    </div>
  </div>
);
