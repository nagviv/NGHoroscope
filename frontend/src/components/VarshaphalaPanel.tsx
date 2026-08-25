import React from 'react';
import { VarshaphalaResponse } from '../types/astrology';
import { Calendar, Crown } from 'lucide-react';

export const VarshaphalaPanel: React.FC<{ data: VarshaphalaResponse }> = ({ data }) => {
  return (
    <div className="bg-slate-900 border border-amber-500/30 rounded-2xl p-6 space-y-4">
      <div className="flex justify-between items-center">
        <h3 className="text-lg font-bold font-cinzel text-amber-300 flex items-center gap-2">
          <Calendar className="w-5 h-5 text-amber-400" /> Tajika Varshaphala
        </h3>
        <span className="text-xs text-amber-400">{data.solar_return_date}</span>
      </div>
      <div className="grid grid-cols-2 gap-3 text-xs">
        <div className="bg-slate-950 p-3 rounded-xl border border-slate-800">
          <span className="text-slate-400 block">Lord of Year</span>
          <span className="font-bold text-amber-300 text-sm">{data.varsheshwara}</span>
        </div>
        <div className="bg-slate-950 p-3 rounded-xl border border-slate-800">
          <span className="text-slate-400 block">Muntha Sign</span>
          <span className="font-bold text-amber-300 text-sm">{data.muntha.sign}</span>
        </div>
      </div>
    </div>
  );
};
