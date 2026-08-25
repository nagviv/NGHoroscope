import React from 'react';
import { VarshaphalaResponse } from '../types/astrology';
import { Calendar } from 'lucide-react';

export const VarshaphalaPanel: React.FC<{ data: VarshaphalaResponse }> = ({ data }) => (
  <div className="bg-slate-900 border border-amber-500/30 rounded-2xl p-6 space-y-4">
    <h3 className="text-lg font-bold font-cinzel text-amber-300 flex items-center gap-2">
      <Calendar className="w-5 h-5 text-amber-400" /> Tajika Varshaphala (Year {data.target_year})
    </h3>
    <div className="bg-slate-950 p-4 rounded-xl border border-slate-800">
      <span className="text-xs text-slate-400 block">Lord of Year (Varsheshwara)</span>
      <span className="text-sm font-bold text-amber-300">{data.varsheshwara}</span>
    </div>
  </div>
);
