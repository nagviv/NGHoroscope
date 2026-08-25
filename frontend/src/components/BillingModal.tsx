import React, { useState } from 'react';
import { CreditCard, Sparkles, Check, Loader2, X } from 'lucide-react';

export const BillingModal: React.FC<{ isOpen: boolean; onClose: () => void; token: string }> = ({ isOpen, onClose, token }) => {
  const [loadingTier, setLoadingTier] = useState<string | null>(null);

  if (!isOpen) return null;

  const handleSubscribe = async (tier: string) => {
    setLoadingTier(tier);
    try {
      const res = await fetch(`/api/v1/billing/checkout?tier=${tier}`, {
        method: 'POST',
        headers: { 'Authorization': `Bearer ${token}` }
      });
      const data = await res.json();
      if (data.checkout_url) {
        window.open(data.checkout_url, '_blank');
      }
    } finally {
      setLoadingTier(null);
    }
  };

  return (
    <div className="fixed inset-0 bg-slate-950/80 backdrop-blur-sm z-50 flex items-center justify-center p-4">
      <div className="bg-slate-900 border border-amber-500/30 rounded-2xl max-w-2xl w-full p-6 relative space-y-6 shadow-2xl">
        <button onClick={onClose} className="absolute top-4 right-4 text-slate-400 hover:text-white">
          <X className="w-5 h-5" />
        </button>

        <div className="text-center space-y-1">
          <h3 className="text-2xl font-cinzel font-bold text-amber-300 flex items-center justify-center gap-2">
            <Sparkles className="w-6 h-6 text-amber-400" /> Upgrade to Jyotish Pro
          </h3>
          <p className="text-xs text-slate-400">Unlock unlimited AI Astrologer consultations and professional PDF reports.</p>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
          <div className="bg-slate-950 border border-slate-800 rounded-xl p-5 space-y-4 flex flex-col justify-between">
            <div className="space-y-3">
              <span className="text-xs font-bold uppercase tracking-wider text-amber-400">Monthly Pro</span>
              <div className="text-2xl font-bold text-slate-100">$9.99 <span className="text-xs text-slate-400 font-normal">/ month</span></div>
              <ul className="space-y-2 text-xs text-slate-300">
                <li className="flex items-center gap-2"><Check className="w-3.5 h-3.5 text-emerald-400" /> Unlimited AI Astrologer Q&A</li>
                <li className="flex items-center gap-2"><Check className="w-3.5 h-3.5 text-emerald-400" /> 50 AI Credits Refill Monthly</li>
                <li className="flex items-center gap-2"><Check className="w-3.5 h-3.5 text-emerald-400" /> Unlimited Kundli & Synastry PDFs</li>
              </ul>
            </div>
            <button
              onClick={() => handleSubscribe('Premium_Monthly')}
              disabled={loadingTier === 'Premium_Monthly'}
              className="w-full bg-amber-500 hover:bg-amber-600 text-slate-950 font-semibold py-2.5 rounded-xl text-xs flex items-center justify-center gap-2 transition"
            >
              {loadingTier === 'Premium_Monthly' ? <Loader2 className="w-4 h-4 animate-spin" /> : <CreditCard className="w-4 h-4" />}
              Subscribe Monthly
            </button>
          </div>

          <div className="bg-slate-950 border border-amber-500/50 rounded-xl p-5 space-y-4 flex flex-col justify-between relative shadow-lg shadow-amber-500/10">
            <div className="absolute -top-3 right-4 bg-amber-500 text-slate-950 text-[10px] font-bold px-2.5 py-0.5 rounded-full uppercase">
              Best Value
            </div>
            <div className="space-y-3">
              <span className="text-xs font-bold uppercase tracking-wider text-amber-400">Annual Pass</span>
              <div className="text-2xl font-bold text-slate-100">$79.99 <span className="text-xs text-slate-400 font-normal">/ year</span></div>
              <ul className="space-y-2 text-xs text-slate-300">
                <li className="flex items-center gap-2"><Check className="w-3.5 h-3.5 text-emerald-400" /> Everything in Monthly Pro</li>
                <li className="flex items-center gap-2"><Check className="w-3.5 h-3.5 text-emerald-400" /> Save 33% Annually</li>
                <li className="flex items-center gap-2"><Check className="w-3.5 h-3.5 text-emerald-400" /> Priority WebSocket Stream Access</li>
              </ul>
            </div>
            <button
              onClick={() => handleSubscribe('Annual_Pass')}
              disabled={loadingTier === 'Annual_Pass'}
              className="w-full bg-gradient-to-r from-amber-500 to-amber-600 hover:from-amber-600 hover:to-amber-700 text-slate-950 font-semibold py-2.5 rounded-xl text-xs flex items-center justify-center gap-2 transition shadow-md shadow-amber-500/20"
            >
              {loadingTier === 'Annual_Pass' ? <Loader2 className="w-4 h-4 animate-spin" /> : <CreditCard className="w-4 h-4" />}
              Get Annual Pass
            </button>
          </div>
        </div>
      </div>
    </div>
  );
};
