import React from 'react';
import { SBCResponse, KotaResponse } from '../types/astrology';
import { ShieldAlert, ShieldCheck, Compass } from 'lucide-react';

export const ChakraPanel: React.FC<{ sbcData: SBCResponse; kotaData: KotaResponse }> = ({ sbcData, kotaData }) => {
  return (
    <div className="bg-slate-900 border border-amber-500/30 rounded-2xl p-6 space-y-6">
      <div className="flex justify-between items-center">
        <div>
          <h3 className="text-lg font-bold font-cinzel text-amber-300 flex items-center gap-2">
            <Compass className="w-5 h-5 text-amber-400" /> Sarvatobhadra & Kota Chakra Defense
          </h3>
          <p className="text-xs text-slate-400">81-Square SBC Grid Vedhas & Fortress Transit Occupancy</p>
        </div>
        <span className="text-xs text-slate-400">Transit: {sbcData.transit_date}</span>
      </div>

      {/* SBC Active Vedhas */}
      <div className="bg-slate-950 p-4 rounded-xl border border-slate-800 space-y-3">
        <div className="flex justify-between items-center">
          <span className="text-xs font-bold uppercase tracking-wider text-amber-300">Sarvatobhadra Active Vedhas</span>
          <span className={`text-[11px] font-bold px-2.5 py-0.5 rounded-full border ${sbcData.active_vedhas.length === 0 ? 'bg-emerald-500/10 text-emerald-400 border-emerald-500/30' : 'bg-amber-500/10 text-amber-400 border-amber-500/30'}`}>
            {sbcData.defense_verdict}
          </span>
        </div>

        {sbcData.active_vedhas.length === 0 ? (
          <p className="text-xs text-slate-400">No harmful direct or frontal Vedhas on sensitive Janma points.</p>
        ) : (
          <div className="grid grid-cols-1 md:grid-cols-2 gap-2 text-xs">
            {sbcData.active_vedhas.map((v, i) => (
              <div key={i} className="bg-slate-900 p-2.5 rounded-lg border border-slate-800">
                <div className="flex justify-between">
                  <span className="font-bold text-amber-200">{v.planet} ({v.nature})</span>
                  <span className="text-[10px] text-slate-400">{v.vedha_type}</span>
                </div>
                <span className="text-[11px] text-slate-300 block mt-0.5">Target: {v.target_sensitive_point}</span>
              </div>
            ))}
          </div>
        )}
      </div>

      {/* Kota Chakra Fortress */}
      <div className="bg-slate-950 p-4 rounded-xl border border-slate-800 space-y-3">
        <div className="flex justify-between items-center">
          <span className="text-xs font-bold uppercase tracking-wider text-amber-300">Kota Chakra (Fort Defense)</span>
          <span className={`text-[11px] font-bold px-2.5 py-0.5 rounded-full border ${kotaData.stambha_siege_malefics.length === 0 ? 'bg-emerald-500/10 text-emerald-400 border-emerald-500/30' : 'bg-red-500/10 text-red-400 border-red-500/30'}`}>
            {kotaData.defense_status}
          </span>
        </div>

        <div className="grid grid-cols-2 md:grid-cols-4 gap-2 text-xs">
          {Object.entries(kotaData.fortress_zones).map(([zone, planets]) => (
            <div key={zone} className="bg-slate-900 p-2.5 rounded-lg border border-slate-800">
              <span className="text-[10px] text-slate-400 block font-semibold">{zone}</span>
              <span className="font-bold text-slate-200 mt-1 block">
                {planets.length > 0 ? planets.join(', ') : 'Empty'}
              </span>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
};
