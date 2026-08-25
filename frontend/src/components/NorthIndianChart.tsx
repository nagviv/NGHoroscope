import React from 'react';
import { NatalChartResponse } from '../types/astrology';

interface Props {
  chart: NatalChartResponse;
  vargaType?: 'D1_Rashi' | 'D9_Navamsha' | 'D10_Dashamsha';
}

const RASHI_ABBR = ['Ar', 'Ta', 'Ge', 'Cn', 'Le', 'Vi', 'Li', 'Sc', 'Sg', 'Cp', 'Aq', 'Pi'];
const PLANET_ABBR: Record<string, string> = {
  Sun: 'Su', Moon: 'Mo', Mars: 'Ma', Mercury: 'Me',
  Jupiter: 'Ju', Venus: 'Ve', Saturn: 'Sa', Rahu: 'Ra', Ketu: 'Ke'
};

export const NorthIndianChart: React.FC<Props> = ({ chart, vargaType = 'D1_Rashi' }) => {
  const ascSignIdx = chart.ascendant.sign_index;
  
  // Group planets by house (1-12)
  const housePlanets: Record<number, string[]> = {
    1: [], 2: [], 3: [], 4: [], 5: [], 6: [],
    7: [], 8: [], 9: [], 10: [], 11: [], 12: []
  };

  Object.entries(chart.planets).forEach(([pName, pData]) => {
    let house = pData.house;
    if (vargaType === 'D9_Navamsha') {
      // Calculate D9 house relative to D9 Ascendant
      const d9SignMap: Record<string, number> = {
        Aries: 0, Taurus: 1, Gemini: 2, Cancer: 3, Leo: 4, Virgo: 5,
        Libra: 6, Scorpio: 7, Sagittarius: 8, Capricorn: 9, Aquarius: 10, Pisces: 11
      };
      const d9AscIdx = d9SignMap[chart.ascendant.d9_sign];
      const pD9Idx = d9SignMap[pData.d9_sign];
      house = ((pD9Idx - d9AscIdx + 12) % 12) + 1;
    }
    const label = `${PLANET_ABBR[pName] || pName}${pData.is_retrograde ? '(R)' : ''}`;
    housePlanets[house]?.push(label);
  });

  const getSignNumber = (houseNum: number) => {
    return ((ascSignIdx + (houseNum - 1)) % 12) + 1;
  };

  return (
    <div className="w-full max-w-[420px] aspect-square mx-auto relative bg-slate-900/90 rounded-xl p-2 border border-amber-500/30 shadow-2xl shadow-amber-950/20">
      <svg viewBox="0 0 400 400" className="w-full h-full stroke-amber-400/80 stroke-[1.5] fill-none text-slate-100">
        {/* Outer Box */}
        <rect x="10" y="10" width="380" height="380" className="stroke-amber-500 stroke-2" />
        
        {/* Main Diagonals */}
        <line x1="10" y1="10" x2="390" y2="390" />
        <line x1="390" y1="10" x2="10" y2="390" />
        
        {/* Inner Diamond */}
        <polygon points="200,10 390,200 200,390 10,200" className="stroke-amber-400 stroke-2" />

        {/* House 1 (Top Center Diamond) */}
        <text x="200" y="45" className="fill-amber-400 text-xs text-center font-bold" textAnchor="middle">{getSignNumber(1)}</text>
        <text x="200" y="110" className="fill-amber-200 text-sm font-semibold" textAnchor="middle">
          {housePlanets[1].join(' ')}
        </text>

        {/* House 2 (Top Left Triangle) */}
        <text x="110" y="45" className="fill-amber-400 text-xs" textAnchor="middle">{getSignNumber(2)}</text>
        <text x="110" y="80" className="fill-slate-200 text-xs" textAnchor="middle">{housePlanets[2].join(' ')}</text>

        {/* House 3 (Left Top Triangle) */}
        <text x="45" y="110" className="fill-amber-400 text-xs" textAnchor="middle">{getSignNumber(3)}</text>
        <text x="75" y="130" className="fill-slate-200 text-xs" textAnchor="middle">{housePlanets[3].join(' ')}</text>

        {/* House 4 (Left Center Diamond) */}
        <text x="110" y="205" className="fill-amber-400 text-xs font-bold" textAnchor="middle">{getSignNumber(4)}</text>
        <text x="110" y="230" className="fill-amber-200 text-sm font-semibold" textAnchor="middle">{housePlanets[4].join(' ')}</text>

        {/* House 5 (Left Bottom Triangle) */}
        <text x="45" y="295" className="fill-amber-400 text-xs" textAnchor="middle">{getSignNumber(5)}</text>
        <text x="75" y="275" className="fill-slate-200 text-xs" textAnchor="middle">{housePlanets[5].join(' ')}</text>

        {/* House 6 (Bottom Left Triangle) */}
        <text x="110" y="365" className="fill-amber-400 text-xs" textAnchor="middle">{getSignNumber(6)}</text>
        <text x="110" y="330" className="fill-slate-200 text-xs" textAnchor="middle">{housePlanets[6].join(' ')}</text>

        {/* House 7 (Bottom Center Diamond) */}
        <text x="200" y="365" className="fill-amber-400 text-xs font-bold" textAnchor="middle">{getSignNumber(7)}</text>
        <text x="200" y="300" className="fill-amber-200 text-sm font-semibold" textAnchor="middle">{housePlanets[7].join(' ')}</text>

        {/* House 8 (Bottom Right Triangle) */}
        <text x="290" y="365" className="fill-amber-400 text-xs" textAnchor="middle">{getSignNumber(8)}</text>
        <text x="290" y="330" className="fill-slate-200 text-xs" textAnchor="middle">{housePlanets[8].join(' ')}</text>

        {/* House 9 (Right Bottom Triangle) */}
        <text x="355" y="295" className="fill-amber-400 text-xs" textAnchor="middle">{getSignNumber(9)}</text>
        <text x="325" y="275" className="fill-slate-200 text-xs" textAnchor="middle">{housePlanets[9].join(' ')}</text>

        {/* House 10 (Right Center Diamond) */}
        <text x="290" y="205" className="fill-amber-400 text-xs font-bold" textAnchor="middle">{getSignNumber(10)}</text>
        <text x="290" y="230" className="fill-amber-200 text-sm font-semibold" textAnchor="middle">{housePlanets[10].join(' ')}</text>

        {/* House 11 (Right Top Triangle) */}
        <text x="355" y="110" className="fill-amber-400 text-xs" textAnchor="middle">{getSignNumber(11)}</text>
        <text x="325" y="130" className="fill-slate-200 text-xs" textAnchor="middle">{housePlanets[11].join(' ')}</text>

        {/* House 12 (Top Right Triangle) */}
        <text x="290" y="45" className="fill-amber-400 text-xs" textAnchor="middle">{getSignNumber(12)}</text>
        <text x="290" y="80" className="fill-slate-200 text-xs" textAnchor="middle">{housePlanets[12].join(' ')}</text>
      </svg>
    </div>
  );
};
