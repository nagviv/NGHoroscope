import React from 'react';
import { KPResponse } from '../types/astrology';
import { Layers, ShieldCheck } from 'lucide-react';

export const KPPanel: React.FC<{ data: KPResponse }> = ({ data }) => {
  return (
    <div className="bg-slate-900 border border-amber-500/30 rounded-2xl p-6 space-y-6">
      <div className="flex flex-col md:flex-row justify-between items-start md:items-center gap-2">
        <div>
          <h3 className="text-lg font-bold font-cinzel text-amber-300 flex items-center gap-2">
            <Layers className="w-5 h-5 text-amber-400" /> Krishnamurti Paddhati (KP System)
          </h3>
          <p className="text-xs text-slate-400">Placidus House Cusps, 249 Sub-Lords & Ruling Planets</p>
        </div>
      </div>

      {/* Ruling Planets Banner */}
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

      {/* 12 Cusps Table */}
      <div className="overflow-x-auto">
        <table className="w-full text-xs text-left border-collapse">
          <thead>
            <tr className="bg-slate-950 text-amber-400 border-b border-slate-800">
              <th className="p-2.5">Cusp</th>
              <th className="p-2.5">Sign</th>
              <th className="p-2.5">Degree</th>
              <th className="p-2.5">Sign Lord</th>
              <th className="p-2.5">Star Lord</th>
              <th className="p-2.5 text-amber-300 font-bold">Sub Lord</th>
            </tr>
          </thead>
          <tbody className="divide-y divide-slate-800/60">
            {data.cusps.map((c) => (
              <tr key={c.cusp} className="hover:bg-slate-950/40">
                <td className="p-2.5 font-bold text-slate-300">{c.cusp}</td>
                <td className="p-2.5 text-slate-200">{c.sign}</td>
                <td className="p-2.5 text-slate-400">{c.degree_in_sign}°</td>
                <td className="p-2.5 text-slate-300">{c.sign_lord}</td>
                <td className="p-2.5 text-slate-300">{c.star_lord}</td>
                <td className="p-2.5 font-bold text-amber-300">{c.sub_lord}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
};
