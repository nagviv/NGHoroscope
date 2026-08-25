import React, { useState } from 'react';
import { BirthDetailsRequest } from '../types/astrology';
import { AIAnswerResponse } from '../types/astrology';
import { Sparkles, Send, Loader2, BookOpen, Compass } from 'lucide-react';

interface Props {
  birthDetails: any;
}

export const AIQuestionPanel: React.FC<Props> = ({ birthDetails }) => {
  const [question, setQuestion] = useState('');
  const [category, setCategory] = useState('Career');
  const [loading, setLoading] = useState(false);
  const [response, setResponse] = useState<AIAnswerResponse | null>(null);

  const handleAsk = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!question.trim()) return;

    setLoading(true);
    try {
      const res = await fetch('/api/v1/ai/ask', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          birth_details: birthDetails,
          question,
          category
        })
      });
      const data = await res.json();
      setResponse(data);
    } catch (err) {
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="bg-slate-900 border border-amber-500/30 rounded-2xl p-6 shadow-xl space-y-6">
      <div className="flex items-center gap-3">
        <div className="p-2.5 rounded-xl bg-amber-500/10 border border-amber-500/30 text-amber-400">
          <Sparkles className="w-5 h-5" />
        </div>
        <div>
          <h3 className="text-lg font-bold font-cinzel text-amber-200">Interactive Vedic Astrologer</h3>
          <p className="text-xs text-slate-400">Contextual interpretations synthesized with classical Jyotish rules</p>
        </div>
      </div>

      <form onSubmit={handleAsk} className="space-y-3">
        <div className="flex gap-2">
          <select
            value={category}
            onChange={(e) => setCategory(e.target.value)}
            className="bg-slate-950 border border-slate-800 rounded-xl px-3 py-2 text-xs text-amber-300 focus:outline-none focus:border-amber-500"
          >
            <option value="Career">Career & Status</option>
            <option value="Relationships">Marriage & Partnerships</option>
            <option value="Finance">Wealth & Dhana</option>
            <option value="Spiritual">Spiritual Evolution</option>
          </select>
          <input
            type="text"
            value={question}
            onChange={(e) => setQuestion(e.target.value)}
            placeholder="Ask anything (e.g., When is a good time for career switch?)"
            className="flex-1 bg-slate-950 border border-slate-800 rounded-xl px-4 py-2 text-sm text-slate-100 placeholder-slate-500 focus:outline-none focus:border-amber-500"
          />
          <button
            type="submit"
            disabled={loading}
            className="bg-gradient-to-r from-amber-500 to-amber-600 hover:from-amber-600 hover:to-amber-700 text-slate-950 font-semibold px-5 py-2 rounded-xl flex items-center gap-2 transition disabled:opacity-50 text-sm shadow-md shadow-amber-500/20"
          >
            {loading ? <Loader2 className="w-4 h-4 animate-spin" /> : <Send className="w-4 h-4" />}
            Ask
          </button>
        </div>
      </form>

      {response && (
        <div className="bg-slate-950/70 border border-amber-500/20 rounded-xl p-5 space-y-4">
          <div className="flex flex-wrap gap-2">
            {response.astrological_factors.map((f, i) => (
              <span key={i} className="text-[11px] bg-amber-500/10 text-amber-300 border border-amber-500/20 px-2.5 py-1 rounded-md font-medium">
                {f}
              </span>
            ))}
          </div>

          <div className="space-y-2">
            <h4 className="text-sm font-bold text-slate-200 flex items-center gap-2">
              <Compass className="w-4 h-4 text-amber-400" />
              Astrological Synthesis
            </h4>
            <p className="text-sm text-slate-300 leading-relaxed bg-slate-900/60 p-4 rounded-lg border border-slate-800/80">
              {response.analysis}
            </p>
          </div>

          <div className="space-y-2 pt-2 border-t border-slate-800">
            <h4 className="text-xs font-bold text-amber-400 uppercase tracking-wider flex items-center gap-2">
              <BookOpen className="w-3.5 h-3.5" />
              Vedic Remedies & Actionable Insights
            </h4>
            <ul className="space-y-1.5 text-xs text-slate-300">
              {response.practical_remedies.map((r, i) => (
                <li key={i} className="flex items-start gap-2">
                  <span className="text-amber-500 font-bold">•</span>
                  <span>{r}</span>
                </li>
              ))}
            </ul>
          </div>
        </div>
      )}
    </div>
  );
};
