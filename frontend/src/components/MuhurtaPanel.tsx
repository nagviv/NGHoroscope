import React from 'react';
import { MuhurtaResponse } from '../types/astrology';
import { Sun, Clock } from 'lucide-react';

export const MuhurtaPanel: React.FC<{ data: MuhurtaResponse }> = ({ data }) => {
  return (
    <div className="bg-slate-900 border border-amber-500/30 rounded-2xl p-6 space-y-6 shadow-xl">
      <div className="flex justify-between items-center">
        <div>
          <h3 className="text-lg font-bold font-cinzel text-amber-300 flex items-center gap-2">
            <Sun className="w-5 h-5 text-amber-400" /> Elective Muhurta ({data?.target_date})
          </h3>
          <p className="text-xs text-slate-400">Daily Choghadiya & Hora Timings</p>
        </div>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-4 text-xs">
        {/* Choghadiya */}
        <div className="bg-slate-950 p-4 rounded-xl border border-slate-800 space-y-3">
          <h4 className="text-xs font-bold text-amber-400 uppercase tracking-wider flex items-center gap-1.5">
            <Clock className="w-3.5 h-3.5 text-amber-400" /> Day Choghadiya
          </h4>
          <div className="space-y-2">
            {data?.choghadiya_day?.map((c, idx) => (
              <div key={idx} className="flex justify-between items-center bg-slate-900 p-2 rounded border border-slate-800">
                <span className="font-bold text-amber-300">{c.name} ({c.nature})</span>
                <span className="text-[11px] text-slate-400">{c.start_time} - {c.end_time}</span>
              </div>
            ))}
          </div>
        </div>

        {/* Special Spans / Rahu Kaal */}
        <div className="bg-slate-950 p-4 rounded-xl border border-slate-800 space-y-3">
          <h4 className="text-xs font-bold text-amber-400 uppercase tracking-wider">Auspicious & Inauspicious Spans</h4>
          <div className="space-y-2 text-slate-300">
            <div className="bg-slate-900 p-2.5 rounded border border-slate-800 flex justify-between items-center">
              <span>Abhijit Muhurat:</span>
              <strong className="text-emerald-400">{data?.special_spans?.abhijit_muhurat?.start_time} - {data?.special_spans?.abhijit_muhurat?.end_time}</strong>
            </div>
            <div className="bg-slate-900 p-2.5 rounded border border-slate-800 flex justify-between items-center">
              <span>Rahu Kaal:</span>
              <strong className="text-rose-400">{data?.special_spans?.rahu_kaal}</strong>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};