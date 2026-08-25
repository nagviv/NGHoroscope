import React from 'react';
import { ProgressionResponse } from '../types/astrology';
import { Orbit, Zap } from 'lucide-react';

export const ProgressionsPanel: React.FC<{ data: ProgressionResponse }> = ({ data }) => {
  return (
    <div className="bg-slate-900 border border-amber-500/30 rounded-2xl p-6 space-y-6">
      <div className="flex justify-between items-center">
        <div>
          <h3 className="text-lg font-bold font-cinzel text-amber-300 flex items-center gap-2">
            <Orbit className="w-5 h-5 text-amber-400" /> Secondary Progressions & Solar Arc
          </h3>
          <p className="text-xs text-slate-400">Day-for-a-Year Progressed Positions & Major Life Milestone Aspects</p>
        </div>
        <span className="text-xs text-amber-300 bg-amber-500/10 px-3 py-1 rounded-full border border-amber-500/30">
          Age: {data.progressed_age}y | Solar Arc: +{data.solar_arc_degrees}°
        </span>
      </div>

      <div className="space-y-3">
        <h4 className="text-xs font-bold text-amber-300 uppercase tracking-wider flex items-center gap-1.5">
          <Zap className="w-3.5 h-3.5 text-amber-400" /> Active Progressed-to-Natal Aspects (1° Orb)
        </h4>

        {data.progressed_aspects.length === 0 ? (
          <div className="bg-slate-950 p-4 rounded-xl border border-slate-800 text-xs text-slate-400">
            No exact major progressed aspects active for this year.
          </div>
        ) : (
          <div className="grid grid-cols-1 md:grid-cols-2 gap-2 text-xs">
            {data.progressed_aspects.map((a, idx) => (
              <div key={idx} className="bg-slate-950 p-3 rounded-xl border border-slate-800 space-y-1">
                <div className="flex justify-between items-center">
                  <span className="font-bold text-amber-300">
                    Prog. {a.progressed_planet} {a.aspect} Natal {a.natal_planet}
                  </span>
                  <span className="text-[10px] font-mono text-slate-400">Orb: {a.orb}°</span>
                </div>
                <p className="text-[11px] text-slate-400">{a.signification}</p>
              </div>
            ))}
          </div>
        )}
      </div>
    </div>
  );
};
