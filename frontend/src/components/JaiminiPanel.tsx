import React from 'react';
import { JaiminiResponse } from '../types/astrology';
import { Compass } from 'lucide-react';

export const JaiminiPanel: React.FC<{ data: JaiminiResponse }> = ({ data }) => {
  return (
    <div className="bg-slate-900 border border-amber-500/30 rounded-2xl p-6 space-y-6 shadow-xl">
      <div className="flex justify-between items-center">
        <h3 className="text-lg font-bold font-cinzel text-amber-300 flex items-center gap-2">
          <Compass className="w-5 h-5 text-amber-400" /> Jaimini System & Chara Karakas
        </h3>
        <span className="text-xs text-amber-300 bg-amber-500/10 px-3 py-1 rounded-full border border-amber-500/30">
          Atmakaraka: {data?.atmakaraka_planet}
        </span>
      </div>

      {/* Karakas Grid */}
      <div className="grid grid-cols-1 md:grid-cols-2 gap-3 text-xs">
        {data?.karakas && Object.entries(data.karakas).map(([karakaName, info]) => (
          <div key={karakaName} className="bg-slate-950 p-3.5 rounded-xl border border-slate-800 space-y-1">
            <div className="font-bold text-amber-300">{karakaName}</div>
            <div className="flex justify-between text-slate-400">
              <span>Planet: <strong className="text-slate-200">{info.planet}</strong></span>
              <span>Sign: <strong className="text-slate-200">{info.sign}</strong></span>
            </div>
            <p className="text-[11px] text-slate-400 pt-1 border-t border-slate-900">Signification: {info.signification}</p>
          </div>
        ))}
      </div>

      {/* Chara Dasha Timeline */}
      <div className="space-y-2">
        <h4 className="text-xs font-bold text-amber-300 uppercase tracking-wider">Chara Dasha Sequence</h4>
        <div className="max-h-60 overflow-y-auto space-y-1.5 pr-1">
          {data?.chara_dasha?.map((d, idx) => (
            <div key={idx} className="bg-slate-950 p-2.5 rounded-xl border border-slate-800 flex justify-between items-center text-xs">
              <span className="font-bold text-amber-300">{d.sign} Rashi (Lord: {d.lord})</span>
              <span className="text-slate-400">{d.duration_years} Years ({d.start_date} to {d.end_date})</span>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
};