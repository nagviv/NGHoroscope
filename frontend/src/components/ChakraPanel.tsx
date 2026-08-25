import React from 'react';
import { SBCResponse, KotaResponse } from '../types/astrology';
import { Compass } from 'lucide-react';

export const ChakraPanel: React.FC<{ sbcData: SBCResponse; kotaData: KotaResponse }> = ({ sbcData, kotaData }) => (
  <div className="bg-slate-900 border border-amber-500/30 rounded-2xl p-6 space-y-4">
    <h3 className="text-lg font-bold font-cinzel text-amber-300 flex items-center gap-2">
      <Compass className="w-5 h-5 text-amber-400" /> Sarvatobhadra & Kota Chakra Defense
    </h3>
    <div className="bg-slate-950 p-4 rounded-xl border border-slate-800">
      <span className="text-xs text-slate-400 block">SBC Defense Verdict</span>
      <span className="text-sm font-bold text-emerald-400">{sbcData.defense_verdict}</span>
    </div>
  </div>
);
