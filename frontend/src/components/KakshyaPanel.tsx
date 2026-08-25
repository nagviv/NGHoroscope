import React from 'react';
import { KakshyaResponse } from '../types/astrology';
import { Target, CheckCircle2, AlertCircle } from 'lucide-react';

export const KakshyaPanel: React.FC<{ data: KakshyaResponse }> = ({ data }) => {
  return (
    <div className="bg-slate-900 border border-amber-500/30 rounded-2xl p-6 space-y-6">
      <div className="flex justify-between items-center">
        <div>
          <h3 className="text-lg font-bold font-cinzel text-amber-300 flex items-center gap-2">
            <Target className="w-5 h-5 text-amber-400" /> Ashtakavarga Kakshya Transit Timing
          </h3>
          <p className="text-xs text-slate-400">8 Equal Sub-divisions (3°45' each) per Sign for Precision Event Timing</p>
        </div>
        <span className="text-xs text-amber-400 bg-amber-500/10 px-3 py-1 rounded-full border border-amber-500/20">
          {data.transit_date}
        </span>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-3">
        {Object.entries(data.kakshya_transits).map(([planet, details]) => (
          <div key={planet} className={`p-4 rounded-xl border flex flex-col justify-between ${details.has_bindu ? 'bg-slate-950 border-emerald-500/30' : 'bg-slate-950 border-slate-800'}`}>
            <div className="flex justify-between items-start">
              <div>
                <span className="font-bold text-sm text-slate-100">{planet}</span>
                <span className="text-xs text-slate-400 block">{details.sign} ({details.degree_in_sign}°)</span>
              </div>
              <span className={`text-[11px] font-semibold px-2 py-0.5 rounded flex items-center gap-1 ${details.has_bindu ? 'bg-emerald-500/10 text-emerald-400 border border-emerald-500/30' : 'bg-slate-800 text-slate-400'}`}>
                {details.has_bindu ? <CheckCircle2 className="w-3 h-3" /> : <AlertCircle className="w-3 h-3" />}
                {details.fructification_status}
              </span>
            </div>

            <div className="mt-3 pt-2 border-t border-slate-800/80 flex justify-between text-xs">
              <span className="text-slate-400">Kakshya {details.kakshya_number} ({details.kakshya_lord})</span>
              <span className="font-mono text-amber-300">{details.kakshya_span}</span>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};
