import React from 'react';
import { MuhurtaResponse } from '../types/astrology';
import { Sun, Clock } from 'lucide-react';

export const MuhurtaPanel: React.FC<{ data: MuhurtaResponse }> = ({ data }) => {
  return (
    <div className="bg-slate-900 border border-amber-500/30 rounded-2xl p-6 space-y-6">
      <div className="flex justify-between items-center">
        <h3 className="text-lg font-bold font-cinzel text-amber-300 flex items-center gap-2">
          <Sun className="w-5 h-5 text-amber-400" /> Elective Muhurta & Auspicious Timing
        </h3>
        <span className="text-xs text-slate-400">Date: {data.target_date}</span>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-3 gap-3">
        <div className="bg-slate-950 p-3 rounded-xl border border-emerald-500/30">
          <span className="text-[10px] text-emerald-400 font-bold uppercase block">Abhijit Muhurat</span>
          <span className="text-sm font-bold text-slate-100">{data.special_spans.abhijit_muhurat.start_time} - {data.special_spans.abhijit_muhurat.end_time}</span>
        </div>
        <div className="bg-slate-950 p-3 rounded-xl border border-red-500/30">
          <span className="text-[10px] text-red-400 font-bold uppercase block">Rahu Kaal (Avoid)</span>
          <span className="text-sm font-bold text-slate-100">{data.special_spans.rahu_kaal}</span>
        </div>
        <div className="bg-slate-950 p-3 rounded-xl border border-amber-500/30">
          <span className="text-[10px] text-amber-400 font-bold uppercase block">Brahma Muhurta</span>
          <span className="text-sm font-bold text-slate-100">{data.special_spans.brahma_muhurta.start_time} - {data.special_spans.brahma_muhurta.end_time}</span>
        </div>
      </div>

      <div className="space-y-2">
        <h4 className="text-xs font-bold text-amber-300 uppercase tracking-wider flex items-center gap-1.5">
          <Clock className="w-3.5 h-3.5" /> Daytime Choghadiya Sequence
        </h4>
        <div className="grid grid-cols-2 md:grid-cols-4 gap-2 text-xs">
          {data.choghadiya_day.map((c, idx) => (
            <div key={idx} className={`p-2.5 rounded-xl border flex flex-col justify-between ${c.quality === 'Good' ? 'bg-emerald-950/30 border-emerald-500/30 text-emerald-200' : 'bg-slate-950 border-slate-800 text-slate-300'}`}>
              <span className="font-bold">{c.name}</span>
              <span className="text-[11px] font-mono mt-1">{c.start_time} - {c.end_time}</span>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
};
