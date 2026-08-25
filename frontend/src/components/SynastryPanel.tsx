import React from 'react';
import { MatchMakingResponse } from '../types/astrology';
import { HeartHandshake, ShieldCheck, Download } from 'lucide-react';

export const SynastryPanel: React.FC<{ data: MatchMakingResponse; onExportPDF: () => void; isDownloading: boolean }> = ({ data, onExportPDF, isDownloading }) => {
  return (
    <div className="bg-slate-900 border border-amber-500/30 rounded-2xl p-6 space-y-6">
      <div className="flex flex-col md:flex-row justify-between items-start md:items-center gap-2">
        <div>
          <h3 className="text-lg font-bold font-cinzel text-amber-300 flex items-center gap-2">
            <HeartHandshake className="w-5 h-5 text-amber-400" /> Ashtakoota Kundli Milap (36 Points)
          </h3>
          <p className="text-xs text-slate-400">Vedic Synastry Matchmaking & Mangal Dosha Compatibility</p>
        </div>
        <button
          onClick={onExportPDF}
          disabled={isDownloading}
          className="bg-amber-500/20 border border-amber-500/40 hover:bg-amber-500/30 text-amber-300 px-3 py-1.5 rounded-xl text-xs font-semibold flex items-center gap-1.5 transition"
        >
          <Download className="w-3.5 h-3.5" />
          {isDownloading ? "Generating PDF..." : "Export Milap PDF"}
        </button>
      </div>

      {/* Score Card */}
      <div className="bg-slate-950 p-4 rounded-xl border border-slate-800 flex justify-between items-center">
        <div>
          <span className="text-xs text-slate-400 uppercase tracking-wider block">Total Score Obtained</span>
          <span className="text-2xl font-bold font-cinzel text-amber-300">{data.ashtakoota.total_score} / 36.0</span>
          <span className="text-xs text-emerald-400 block mt-0.5">{data.overall_compatibility}</span>
        </div>
        <div className="text-right">
          <span className="text-xs text-slate-400 block">Status</span>
          <span className={`text-xs font-bold px-2.5 py-1 rounded-full border ${data.ashtakoota.is_recommended ? 'bg-emerald-500/10 text-emerald-400 border-emerald-500/30' : 'bg-amber-500/10 text-amber-400 border-amber-500/30'}`}>
            {data.ashtakoota.is_recommended ? "Auspicious Union" : "Remedies Advised"}
          </span>
        </div>
      </div>

      {/* Koota Breakdown Grid */}
      <div className="grid grid-cols-2 md:grid-cols-4 gap-2 text-xs">
        {Object.entries(data.ashtakoota.breakdown).map(([koota, score]) => (
          <div key={koota} className="bg-slate-950 p-2.5 rounded-xl border border-slate-800 flex justify-between items-center">
            <span className="text-slate-300 font-medium">{koota}</span>
            <span className="font-bold text-amber-400">{score.obtained} / {score.max}</span>
          </div>
        ))}
      </div>
    </div>
  );
};
