import React from 'react';
import { JaiminiResponse } from '../types/astrology';
import { Compass, Sparkles } from 'lucide-react';

export const JaiminiPanel: React.FC<{ data: JaiminiResponse }> = ({ data }) => {
  return (
    <div className="bg-slate-900 border border-amber-500/30 rounded-2xl p-6 space-y-5">
      <div className="flex justify-between items-center">
        <h3 className="text-lg font-bold font-cinzel text-amber-300 flex items-center gap-2">
          <Compass className="w-5 h-5 text-amber-400" /> Jaimini Sutras Analysis
        </h3>
        <span className="text-xs bg-amber-500/10 border border-amber-500/30 text-amber-400 px-3 py-1 rounded-full">
          Karakamsha: {data.karakamsha_sign}
        </span>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-3">
        {Object.entries(data.karakas).map(([kName, kData]) => (
          <div key={kName} className="bg-slate-950/70 border border-slate-800 p-3 rounded-xl flex flex-col justify-between">
            <div className="flex justify-between items-start">
              <span className="font-bold text-amber-400 text-xs">{kName}</span>
              <span className="text-xs font-bold text-slate-200">{kData.planet} ({kData.degree_in_sign}°)</span>
            </div>
            <div className="text-[11px] text-slate-400 mt-1">{kData.signification}</div>
          </div>
        ))}
      </div>

      <div className="space-y-2 pt-2 border-t border-slate-800">
        <h4 className="text-xs font-bold text-amber-300 uppercase tracking-wider flex items-center gap-1.5">
          <Sparkles className="w-3.5 h-3.5" /> Chara Dasha Timeline (Sign Periods)
        </h4>
        <div className="grid grid-cols-3 md:grid-cols-4 gap-2 text-xs">
          {data.chara_dasha.map((cd, idx) => (
            <div key={idx} className="bg-slate-950 p-2 rounded-lg border border-slate-800 text-center">
              <div className="font-bold text-slate-200">{cd.sign} ({cd.duration_years}y)</div>
              <div className="text-[10px] text-slate-500 mt-0.5">{cd.start_date.slice(0,4)} - {cd.end_date.slice(0,4)}</div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
};
