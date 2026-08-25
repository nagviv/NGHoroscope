import React from 'react';
import { KPResponse } from '../types/astrology';
import { Layers } from 'lucide-react';

export const KPPanel: React.FC<{ data: KPResponse }> = ({ data }) => {
  return (
    <div className="bg-slate-900 border border-amber-500/30 rounded-2xl p-6 space-y-4">
      <h3 className="text-lg font-bold font-cinzel text-amber-300 flex items-center gap-2">
        <Layers className="w-5 h-5 text-amber-400" /> Krishnamurti Paddhati (KP System)
      </h3>
      <div className="overflow-x-auto">
        <table className="w-full text-xs text-left">
          <thead>
            <tr className="bg-slate-950 text-amber-400">
              <th className="p-2">Cusp</th><th className="p-2">Sign</th><th className="p-2">Star Lord</th><th className="p-2">Sub Lord</th>
            </tr>
          </thead>
          <tbody>
            {data.cusps.map(c => (
              <tr key={c.cusp} className="border-b border-slate-800">
                <td className="p-2 font-bold">{c.cusp}</td><td className="p-2">{c.sign}</td><td className="p-2">{c.star_lord}</td><td className="p-2 font-bold text-amber-300">{c.sub_lord}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
};
