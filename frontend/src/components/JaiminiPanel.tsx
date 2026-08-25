import React from 'react';
import { JaiminiResponse } from '../types/astrology';
import { Compass } from 'lucide-react';

export const JaiminiPanel: React.FC<{ data: JaiminiResponse }> = ({ data }) => (
  <div className="bg-slate-900 border border-amber-500/30 rounded-2xl p-6 space-y-4">
    <h3 className="text-lg font-bold font-cinzel text-amber-300 flex items-center gap-2"><Compass className="w-5 h-5 text-amber-400" /> Jaimini Karakas</h3>
  </div>
);
