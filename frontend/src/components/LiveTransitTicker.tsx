import React, { useState, useEffect } from 'react';
import { Radio } from 'lucide-react';

export const LiveTransitTicker: React.FC = () => {
  const [liveData, setLiveData] = useState<{ timestamp: string; planets: Record<string, any> } | null>(null);

  useEffect(() => {
    const protocol = window.location.protocol === 'https:' ? 'wss:' : 'ws:';
    const socket = new WebSocket(`${protocol}//${window.location.host}/ws/ephemeris/live`);
    socket.onmessage = (event) => {
      try { setLiveData(JSON.parse(event.data)); } catch (e) { console.error(e); }
    };
    return () => socket.close();
  }, []);

  if (!liveData) return null;

  return (
    <div className="bg-slate-900/90 border border-amber-500/20 rounded-xl px-4 py-2 flex items-center justify-between text-xs overflow-x-auto shadow-md">
      <div className="flex items-center gap-2 text-amber-400 font-bold whitespace-nowrap">
        <Radio className="w-3.5 h-3.5 animate-pulse text-emerald-400" />
        <span>LIVE GOCHAR STREAM:</span>
      </div>
      <div className="flex gap-4 items-center text-slate-300 font-mono text-[11px] whitespace-nowrap overflow-x-auto px-4">
        {Object.entries(liveData.planets).map(([pName, pData]) => (
          <span key={pName} className="flex items-center gap-1">
            <span className="text-amber-300 font-semibold">{pName}:</span>
            <span>{pData.sign} {pData.degree_in_sign.toFixed(2)}°</span>
          </span>
        ))}
      </div>
    </div>
  );
};
