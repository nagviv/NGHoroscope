import React from 'react';
import { VarshaphalaResponse } from '../types/astrology';
import { Calendar, Award } from 'lucide-react';

export const VarshaphalaPanel: React.FC<{ data: VarshaphalaResponse }> = ({ data }) => {
  return (
    <div className="bg-slate-900 border border-amber-500/30 rounded-2xl p-6 space-y-6 shadow-xl">
      <div className="flex justify-between items-center">
        <div>
          <h3 className="text-lg font-bold font-cinzel text-amber-300 flex items-center gap-2">
            <Calendar className="w-5 h-5 text-amber-400" /> Tajika Varshaphala ({data?.target_year})
          </h3>
          <p className="text-xs text-slate-400">Solar Return Date: {data?.solar_return_date}</p>
        </div>
        <div className="text-right">
          <span className="text-[10px] text-slate-400 block">Lord of the Year</span>
          <span className="text-xs font-bold text-amber-300 bg-amber-500/10 px-3 py-1 rounded-full border border-amber-500/30">
            {data?.varsheshwara}
          </span>
        </div>
      </div>

      {/* Muntha Details */}
      <div className="grid grid-cols-1 md:grid-cols-2 gap-4 text-xs">
        <div className="bg-slate-950 p-4 rounded-xl border border-slate-800 space-y-2">
          <h4 className="text-xs font-bold text-amber-400 uppercase tracking-wider flex items-center gap-1.5">
            <Award className="w-3.5 h-3.5 text-amber-400" /> Muntha Position
          </h4>
          <div className="space-y-1 text-slate-300">
            <div>Sign: <strong className="text-amber-300">{data?.muntha?.sign}</strong></div>
            <div>Sign Lord: <strong className="text-amber-300">{data?.muntha?.lord}</strong></div>
            <div>Completed Years: <strong className="text-slate-200">{data?.muntha?.completed_years}</strong></div>
          </div>
        </div>

        <div className="bg-slate-950 p-4 rounded-xl border border-slate-800 space-y-2">
          <h4 className="text-xs font-bold text-amber-400 uppercase tracking-wider">Tajika Aspects & Yogas</h4>
          {data?.tajika_yogas?.map((yoga, idx) => (
            <div key={idx} className="space-y-1">
              <div className="font-bold text-emerald-400">{yoga.name} ({yoga.planets})</div>
              <p className="text-[11px] text-slate-400">{yoga.description}</p>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
};