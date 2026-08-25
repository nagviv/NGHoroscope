import React from 'react';
import { MuhurtaResponse } from '../types/astrology';
import { Sun } from 'lucide-react';

export const MuhurtaPanel: React.FC<{ data: MuhurtaResponse }> = ({ data }) => (
  <div className="bg-slate-900 border border-amber-500/30 rounded-2xl p-6 space-y-4">
    <h3 className="text-lg font-bold font-cinzel text-amber-300 flex items-center gap-2">
      <Sun className="w-5 h-5 text-amber-400" /> Elective Muhurta
    </h3>
  </div>
);
