import React from 'react';
import { KPResponse } from '../types/astrology';
import { Layers } from 'lucide-react';

export const KPPanel: React.FC<{ data: KPResponse }> = ({ data }) => {
  return (
    <div className="bg-slate-900 border border-amber-500/30 rounded-2xl p-6 space-y-6 shadow-xl">
      <div className="flex justify-between items-center">
        <h3 className="text-lg font-bold font-cinzel text-amber-300 flex items-center gap-2">
          <Layers className="w-5 h-5 text-amber-400" /> KP System Sub-Lords & Cusps
        </h3>
      </div>

      {/* Ruling Planets */}
      {data?.ruling_planets && (
        <div className="bg-slate-950 p-4 rounded-xl border border-slate-800 space-y-2">
          <h4 className="text-xs font-bold text-amber-400 uppercase tracking-wider">Ruling Planets (RP)</h4>
          <div className="grid grid-cols-2 md:grid-cols-3 gap-2 text-xs text-slate-300">
            {Object.entries(data.ruling_planets).map(([key, val]) => (
              <div key={key} className="bg-slate-900 p-2 rounded border border-slate-800">
                <span className="text-slate-400 block capitalize">{key.replace(/_/g, ' ')}</span>
                <span className="font-bold text-amber-300">{val as string}</span>
              </div>
            ))}
          </div>
        </div>
      )}

      {/* House Cusps */}
      <div className="space-y-2">
        <h4 className="text-xs font-bold text-amber-300 uppercase tracking-wider">Cuspal Sub-Lords</h4>
        <div className="overflow-x-auto">
          <table className="w-full text-left text-xs text-slate-300 border-collapse">
            <thead>
              <tr className="bg-slate-950 text-amber-400 border-b border-slate-800">
                <th className="p-2.5">Cusp</th>
                <th className="p-2.5">Sign</th>
                <th className="p-2.5">Sign Lord</th>
                <th className="p-2.5">Star Lord</th>
                <th className="p-2.5">Sub Lord</th>
              </tr>
            </thead>
            <tbody>
              {data?.cusps?.map((c) => (
                <tr key={c.cusp} className="border-b border-slate-800/50 hover:bg-slate-950/50">
                  <td className="p-2.5 font-bold text-amber-300">{c.cusp}</td>
                  <td className="p-2.5">{c.sign}</td>
                  <td className="p-2.5 text-slate-400">{c.sign_lord}</td>
                  <td className="p-2.5 text-slate-400">{c.star_lord}</td>
                  <td className="p-2.5 font-semibold text-emerald-400">{c.sub_lord}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
};