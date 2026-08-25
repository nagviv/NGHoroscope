import React from 'react';
import { KPResponse } from '../types/astrology';
import { Layers } from 'lucide-react';

export const KPPanel: React.FC<{ data: KPResponse }> = ({ data }) => (
  <div className="bg-slate-900 border border-amber-500/30 rounded-2xl p-6 space-y-4">
    <h3 className="text-lg font-bold font-cinzel text-amber-300 flex items-center gap-2">
      <Layers className="w-5 h-5 text-amber-400" /> KP Sub-Lords
    </h3>
  </div>
);
