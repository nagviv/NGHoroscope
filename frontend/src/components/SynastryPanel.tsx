import React from 'react';
import { MatchMakingResponse } from '../types/astrology';
import { HeartHandshake } from 'lucide-react';

export const SynastryPanel: React.FC<{ data: MatchMakingResponse }> = ({ data }) => {
  return (
    <div className="bg-slate-900 border border-amber-500/30 rounded-2xl p-6 space-y-4">
      <h3 className="text-lg font-bold font-cinzel text-amber-300 flex items-center gap-2">
        <HeartHandshake className="w-5 h-5 text-amber-400" /> Ashtakoota Matchmaking
      </h3>
      <div className="bg-slate-950 p-4 rounded-xl border border-slate-800">
        <span className="text-2xl font-bold text-amber-300 font-cinzel">{data.ashtakoota.total_score} / 36.0</span>
        <span className="text-xs text-emerald-400 block mt-1">{data.overall_compatibility}</span>
      </div>
    </div>
  );
};
