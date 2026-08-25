import React from 'react';
import { KakshyaResponse } from '../types/astrology';
import { Target, Zap } from 'lucide-react';

export const KakshyaPanel: React.FC<{ data: KakshyaResponse }> = ({ data }) => {
  return (
    <div className="bg-slate-900 border border-amber-500/30 rounded-2xl p-6 space-y-6 shadow-xl">
      <div className="flex justify-between items-center">
        <div>
          <h3 className="text-lg font-bold font-cinzel text-amber-300 flex items-center gap-2">
            <Target className="w-5 h-5 text-amber-400" /> Ashtakavarga Kakshya Timing
          </h3>
          <p className="text-xs text-slate-400">Transit Date: {data?.transit_date}</p>
        </div>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-3 text-xs">
        {data?.kakshya_transits && Object.entries(data.kakshya_transits).map(([planet, info]) => (
          <div key={planet} className="bg-slate-950 p-4 rounded-xl border border-slate-800 space-y-2">
            <div className="flex justify-between items-center">
              <span className="font-bold text-amber-300 text-sm">{planet}</span>
              <span className="text-[10px] text-amber-400 bg-amber-500/10 px-2.5 py-0.5 rounded-full border border-amber-500/30">
                Kakshya #{info.kakshya_number} ({info.kakshya_lord})
              </span>
            </div>
            <div className="flex justify-between text-slate-400">
              <span>Sign: <strong className="text-slate-200">{info.sign}</strong></span>
              <span>Degree: <strong className="text-slate-200">{info.degree_in_sign}°</strong></span>
            </div>
            <div className="flex justify-between items-center pt-1 border-t border-slate-900 text-[11px]">
              <span className="text-slate-400">Span: {info.kakshya_span}</span>
              <span className="font-semibold text-emerald-400">{info.fructification_status}</span>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};