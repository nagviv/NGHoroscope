import React, { useState } from 'react';
import { AIAnswerResponse } from '../types/astrology';
import { Sparkles, Send, Loader2 } from 'lucide-react';

export const AIQuestionPanel: React.FC<{ birthDetails: any }> = ({ birthDetails }) => {
  const [question, setQuestion] = useState('');
  const [loading, setLoading] = useState(false);
  const [response, setResponse] = useState<AIAnswerResponse | null>(null);

  const handleAsk = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!question.trim()) return;
    setLoading(true);
    try {
      const res = await fetch('/api/v1/ai/ask', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify({ birth_details: birthDetails, question, category: 'Career' }) });
      setResponse(await res.json());
    } finally { setLoading(false); }
  };

  return (
    <div className="bg-slate-900 border border-amber-500/30 rounded-2xl p-6 space-y-4">
      <h3 className="text-lg font-bold font-cinzel text-amber-200 flex items-center gap-2"><Sparkles className="w-5 h-5 text-amber-400" /> AI Astrologer Q&A</h3>
      <form onSubmit={handleAsk} className="flex gap-2">
        <input type="text" value={question} onChange={(e) => setQuestion(e.target.value)} placeholder="Ask your astrological question..." className="flex-1 bg-slate-950 border border-slate-800 rounded-xl px-4 py-2 text-sm text-slate-100 focus:outline-none focus:border-amber-500" />
        <button type="submit" disabled={loading} className="bg-amber-500 text-slate-950 font-semibold px-4 py-2 rounded-xl flex items-center gap-2">{loading ? <Loader2 className="w-4 h-4 animate-spin" /> : <Send className="w-4 h-4" />} Ask</button>
      </form>
      {response && <div className="bg-slate-950 p-4 rounded-xl border border-slate-800 space-y-2 text-xs text-slate-300"><div className="font-bold text-amber-400">Analysis:</div><p>{response.analysis}</p></div>}
    </div>
  );
};
