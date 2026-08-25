import React from 'react';
import { KakshyaResponse } from '../types/astrology';
import { Target } from 'lucide-react';

export const KakshyaPanel: React.FC<{ data: KakshyaResponse }> = ({ data }) => (
  <div className="bg-slate-900 border border-amber-500/30 rounded-2xl p-6 space-y-4">
    <h3 className="text-lg font-bold font-cinzel text-amber-300 flex items-center gap-2">
      <Target className="w-5 h-5 text-amber-400" /> Ashtakavarga Kakshya Timing
    </h3>
  </div>
);
