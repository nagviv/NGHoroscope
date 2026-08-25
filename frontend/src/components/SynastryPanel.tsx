import React from 'react';
import { MatchMakingResponse } from '../types/astrology';
import { HeartHandshake, CheckCircle2 } from 'lucide-react';

export const SynastryPanel: React.FC<{ data: MatchMakingResponse }> = ({ data }) => {
  const score = data?.ashtakoota?.total_score ?? 0;
  const maxScore = data?.ashtakoota?.maximum_score ?? 36;

  return (
    <div className="bg-slate-900 border border-amber-500/30 rounded-2xl p-6 space-y-6 shadow-xl">
      <div className="flex justify-between items-center">
        <div>
          <h3 className="text-lg font-bold font-cinzel text-amber-300 flex items-center gap-2">
            <HeartHandshake className="w-5 h-5 text-amber-400" /> Ashtakoota Matchmaking & Synastry
          </h3>
          <p className="text-xs text-slate-400">Bride & Groom Astrological Compatibility Analysis</p>
        </div>
        <div className="text-right">
          <span className="text-2xl font-bold font-cinzel text-amber-300">{score} / {maxScore}</span>
          <span className="text-[10px] text-emerald-400 block font-semibold flex items-center gap-1 justify-end">
            <CheckCircle2 className="w-3 h-3" /> {data?.overall_compatibility}
          </span>
        </div>
      </div>

      {/* Breakdown Grid */}
      <div className="space-y-2">
        <h4 className="text-xs font-bold text-amber-300 uppercase tracking-wider">Koota Score Breakdown</h4>
        <div className="grid grid-cols-2 md:grid-cols-4 gap-2 text-xs">
          {data?.ashtakoota?.breakdown && Object.entries(data.ashtakoota.breakdown).map(([koota, details]) => (
            <div key={koota} className="bg-slate-950 p-3 rounded-xl border border-slate-800 space-y-1">
              <span className="text-slate-400 block">{koota}</span>
              <div className="font-bold text-amber-300 text-sm">
                {details.obtained} <span className="text-[10px] text-slate-500 font-normal">/ {details.max}</span>
              </div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
};