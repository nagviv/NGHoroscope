import React from 'react';
import { KPResponse } from '../types/astrology';
import { Layers, ShieldCheck } from 'lucide-react';

export const KPPanel: React.FC<{ data: KPResponse }> = ({ data }) => {
  return (
    <div className="bg-slate-900 border border-amber-500/30 rounded-2xl p-6 space-y-6">
      <div className="flex justify-between items-center">
        <h3 className="text-lg font-bold font-cinzel text-amber-300 flex items-center gap-2">
          <Layers className="w-5 h-5 text-amber-400" /> Krishnamurti Paddhati (KP System)
        </h3>
      </div>

      <div className="bg-slate-950 p-4 rounded-xl border border-slate-800 space-y-2">
        <h4 className="text-xs font-bold text-amber-400 uppercase tracking-wider flex items-center gap-1.5">
          <ShieldCheck className="w-4 h-4 text-amber-400" /> KP Ruling Planets (RP)
        </h4>
        <div className="grid grid-cols-2 md:grid-cols-5 gap-2 text-xs">
          <div className="bg-slate-900 p-2 rounded-lg border border-slate-800/80">
            <span className="text-[10px] text-slate-400 block">Lagna Sign Lord</span>
            <span className="font-bold text-amber-200">{data.ruling_planets.lagna_sign_lord}</span>
          </div>
          <div className="bg-slate-900 p-2 rounded-lg border border-slate-800/80">
            <span className="text-[10px] text-slate-400 block">Lagna Star Lord</span>
            <span className="font-bold text-amber-200">{data.ruling_planets.lagna_star_lord}</span>
          </div>
          <div className="bg-slate-900 p-2 rounded-lg border border-slate-800/80">
            <span className="text-[10px] text-slate-400 block">Moon Sign Lord</span>
            <span className="font-bold text-amber-200">{data.ruling_planets.moon_sign_lord}</span>
          </div>
          <div className="bg-slate-900 p-2 rounded-lg border border-slate-800/80">
            <span className="text-[10px] text-slate-400 block">Moon Star Lord</span>
            <span className="font-bold text-amber-200">{data.ruling_planets.moon_star_lord}</span>
          </div>
          <div className="bg-slate-900 p-2 rounded-lg border border-slate-800/80">
            <span className="text-[10px] text-slate-400 block">Day Lord</span>
            <span className="font-bold text-amber-200">{data.ruling_planets.day_lord}</span>
          </div>
        </div>
      </div>
    </div>
  );
};
