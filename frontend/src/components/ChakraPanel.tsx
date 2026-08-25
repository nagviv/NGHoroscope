import React from 'react';
import { SBCResponse, KotaResponse } from '../types/astrology';
import { Compass, ShieldAlert, ShieldCheck } from 'lucide-react';

export const ChakraPanel: React.FC<{ sbcData: SBCResponse; kotaData: KotaResponse }> = ({ sbcData, kotaData }) => {
  return (
    <div className="bg-slate-900 border border-amber-500/30 rounded-2xl p-6 space-y-6 shadow-xl">
      <div className="flex justify-between items-center">
        <h3 className="text-lg font-bold font-cinzel text-amber-300 flex items-center gap-2">
          <Compass className="w-5 h-5 text-amber-400" /> Sarvatobhadra & Kota Chakra Defense
        </h3>
        <span className="text-xs text-slate-400">Transit Date: {sbcData?.transit_date}</span>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-4 text-xs">
        {/* SBC Verdict */}
        <div className="bg-slate-950 p-4 rounded-xl border border-slate-800 space-y-3">
          <h4 className="text-xs font-bold text-amber-400 uppercase tracking-wider flex items-center gap-1.5">
            <ShieldCheck className="w-4 h-4 text-emerald-400" /> Sarvatobhadra Chakra (SBC)
          </h4>
          <div className="space-y-2">
            <div className="flex justify-between bg-slate-900 p-2.5 rounded border border-slate-800">
              <span className="text-slate-400">Defense Verdict:</span>
              <strong className="text-emerald-400">{sbcData?.defense_verdict}</strong>
            </div>
            {sbcData?.active_vedhas?.map((v, idx) => (
              <div key={idx} className="bg-slate-900 p-2 rounded border border-slate-800 text-[11px] text-slate-300">
                <span className="text-amber-300 font-bold">{v.planet}</span> impacting {v.target} ({v.vedha_type})
              </div>
            ))}
          </div>
        </div>

        {/* Kota Chakra */}
        <div className="bg-slate-950 p-4 rounded-xl border border-slate-800 space-y-3">
          <h4 className="text-xs font-bold text-amber-400 uppercase tracking-wider flex items-center gap-1.5">
            <ShieldAlert className="w-4 h-4 text-amber-400" /> Kota Chakra Fortress
          </h4>
          <div className="space-y-2 text-slate-300">
            <div className="flex justify-between bg-slate-900 p-2.5 rounded border border-slate-800">
              <span className="text-slate-400">Fortress Status:</span>
              <strong className="text-amber-300">{kotaData?.defense_status}</strong>
            </div>
            <div className="flex justify-between bg-slate-900 p-2.5 rounded border border-slate-800">
              <span className="text-slate-400">Kota Swami:</span>
              <strong className="text-slate-200">{kotaData?.kota_swami}</strong>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};