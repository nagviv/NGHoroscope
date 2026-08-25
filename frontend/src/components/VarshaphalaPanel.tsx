import React from 'react';
import { VarshaphalaResponse } from '../types/astrology';
import { Calendar, Crown, Award } from 'lucide-react';

export const VarshaphalaPanel: React.FC<{ data: VarshaphalaResponse }> = ({ data }) => {
  return (
    <div className="bg-slate-900 border border-amber-500/30 rounded-2xl p-6 space-y-6">
      <div className="flex flex-col md:flex-row justify-between items-start md:items-center gap-2">
        <div>
          <h3 className="text-lg font-bold font-cinzel text-amber-300 flex items-center gap-2">
            <Calendar className="w-5 h-5 text-amber-400" /> Tajika Varshaphala (Annual Solar Return)
          </h3>
          <p className="text-xs text-slate-400">Year {data.target_year} Solar Return Chart, Muntha & Tajika Yogas</p>
        </div>
        <span className="text-xs bg-amber-500/10 text-amber-300 border border-amber-500/30 px-3 py-1 rounded-full">
          Return: {data.solar_return_date}
        </span>
      </div>

      {/* Year Lord & Muntha Banner */}
      <div className="grid grid-cols-1 md:grid-cols-2 gap-3">
        <div className="bg-slate-950 p-4 rounded-xl border border-amber-500/30 flex justify-between items-center">
          <div>
            <span className="text-[10px] text-amber-400 font-bold uppercase block flex items-center gap-1">
              <Crown className="w-3.5 h-3.5" /> Varsheshwara (Lord of the Year)
            </span>
            <span className="text-xl font-bold font-cinzel text-slate-100">{data.varsheshwara}</span>
          </div>
          <span className="text-xs text-slate-400 bg-slate-900 px-2.5 py-1 rounded-md border border-slate-800">
            Lagna: {data.varsha_ascendant.sign}
          </span>
        </div>

        <div className="bg-slate-950 p-4 rounded-xl border border-slate-800 flex justify-between items-center">
          <div>
            <span className="text-[10px] text-slate-400 uppercase tracking-wider block">Muntha Progression</span>
            <span className="text-xl font-bold font-cinzel text-amber-300">{data.muntha.sign}</span>
          </div>
          <span className="text-xs text-slate-400 bg-slate-900 px-2.5 py-1 rounded-md border border-slate-800">
            Lord: {data.muntha.lord} (Age {data.muntha.completed_years})
          </span>
        </div>
      </div>

      {/* Tajika Yogas */}
      <div className="space-y-3 pt-2 border-t border-slate-800">
        <h4 className="text-xs font-bold text-amber-300 uppercase tracking-wider flex items-center gap-1.5">
          <Award className="w-3.5 h-3.5 text-amber-400" /> Active Tajika Annual Yogas
        </h4>
        <div className="grid grid-cols-1 md:grid-cols-2 gap-2 text-xs">
          {data.tajika_yogas.map((y, idx) => (
            <div key={idx} className="bg-slate-950 p-3 rounded-xl border border-slate-800 space-y-1">
              <div className="flex justify-between items-center">
                <span className="font-bold text-amber-300">{y.name}</span>
                <span className="text-[10px] text-slate-400">{y.planets}</span>
              </div>
              <p className="text-slate-300 text-[11px] leading-relaxed">{y.description}</p>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
};
