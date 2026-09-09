'use client';

import { useEffect, useState, useMemo } from 'react';
import Link from 'next/link';

export function QuizComponent({ franchise }: { franchise: string }) {
  const [sessionId, setSessionId] = useState<string | null>(null);
  const [question, setQuestion] = useState<any>(null);
  const [result, setResult] = useState<any>(null);
  const [loading, setLoading] = useState(false);

  // UI-only state for the styling/animations below
  const [selectedKey, setSelectedKey] = useState<string | null>(null);
  const [entering, setEntering] = useState(true);
  const [scanned, setScanned] = useState(false);
  const [questionNumber, setQuestionNumber] = useState(1);

  // 🚀 START QUIZ
  useEffect(() => {
    startQuiz();
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [franchise]);

  const startQuiz = async () => {
    setLoading(true);
    try {
      const res = await fetch(`${process.env.NEXT_PUBLIC_API_URL}api/quiz/start`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ franchise }),
      });

      const data = await res.json();

      if (!data) {
        console.error("Invalid response");
        setLoading(false);
        return;
      }

      setSessionId(data.session_id);
      setQuestion(data.question);
      setQuestionNumber(1);
      setSelectedKey(null);
      setResult(null);
    } catch (err) {
      console.error('Start error:', err);
    }
    setLoading(false);
  };

  // 🚀 HANDLE ANSWER
  const handleAnswer = async (key: string) => {
    if (!sessionId || !question || loading) return;

    setSelectedKey(key);
    setLoading(true);

    try {
      const res = await fetch(`${process.env.NEXT_PUBLIC_API_URL}api/quiz/answer`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          session_id: sessionId,
          response: {
            question_id: question.id,
            selected_option: key,
          },
        }),
      });

      const data = await res.json();
      console.log('RESPONSE:', data);

      if (data.completed || !data.question) {
        setResult(data);
        setQuestion(null);
      } else {
        setQuestion(data.question);
        setQuestionNumber((n) => n + 1);
        setSelectedKey(null);
      }
    } catch (err) {
      console.error('Answer error:', err);
    }

    setLoading(false);
  };

  // 🔁 RESTART
  const restartQuiz = () => {
    setResult(null);
    setSessionId(null);
    setQuestion(null);
    setSelectedKey(null);
    setQuestionNumber(1);
    setScanned(false);
    startQuiz();
  };

  // Slide-in animation whenever a new question mounts
  useEffect(() => {
    if (!question) return;
    setEntering(true);
    const t = setTimeout(() => setEntering(false), 50);
    return () => clearTimeout(t);
  }, [question]);

  // Reveal animation once results come back
  useEffect(() => {
    if (!result) return;
    setEntering(true);
    setScanned(false);
    const t1 = setTimeout(() => setEntering(false), 50);
    const t2 = setTimeout(() => setScanned(true), 250);
    return () => {
      clearTimeout(t1);
      clearTimeout(t2);
    };
  }, [result]);

  // Normalize confidence: accept either 0-1 or 0-100
  const confidencePct =
    result?.confidence !== undefined
      ? Math.round(
          result.confidence <= 1 ? result.confidence * 100 : result.confidence
        )
      : undefined;

  // =========================
  // LOADING
  // =========================
  if (loading && !question) {
    return (
      <div className="relative flex min-h-screen items-center justify-center overflow-hidden bg-[#080808] p-6 text-white">
        <div
          className="
            pointer-events-none
            absolute inset-0
            opacity-[0.035]
            [background-image:linear-gradient(rgba(59,130,246,0.5)_1px,transparent_1px),linear-gradient(90deg,rgba(59,130,246,0.5)_1px,transparent_1px)]
            [background-size:64px_64px]
          "
        />

        <Link
          href="/"
          className="
            absolute left-6 top-6 z-20
            font-mono text-[9px]
            uppercase tracking-[0.3em]
            text-white/40
            transition-colors
            hover:text-[#3b82f6]
          "
        >
          ← Return to Archive
        </Link>

        <div
          className="
            relative z-10
            w-full max-w-xl
            border border-white/20
            bg-[#0b0b0b]
            px-8 py-10
            shadow-[10px_10px_0_0_#3b82f6]
            md:px-12 md:py-14
          "
        >
          <div
            className="
              mb-8 flex items-center gap-3
              font-mono text-[9px]
              uppercase tracking-[0.35em]
              text-[#3b82f6]
            "
          >
            <span className="relative flex h-2 w-2">
              <span className="absolute inline-flex h-full w-full animate-ping bg-[#3b82f6] opacity-75" />
              <span className="relative inline-flex h-2 w-2 bg-[#3b82f6]" />
            </span>
            System initialization
          </div>

          <h1
            className="
              text-5xl font-black
              uppercase leading-[0.85]
              tracking-[-0.05em]
              md:text-7xl
            "
          >
            Booting
            <span className="block text-[#3b82f6]">
              Engine
              <span className="animate-pulse">_</span>
            </span>
          </h1>

          <div className="mt-10 h-px w-full bg-white/10">
            <div className="h-px w-1/3 animate-pulse bg-[#3b82f6]" />
          </div>

          <div
            className="
              mt-4 flex justify-between
              font-mono text-[8px]
              uppercase tracking-[0.25em]
              text-white/30
            "
          >
            <span>Resonance core</span>
            <span>Establishing connection...</span>
          </div>
        </div>
      </div>
    );
  }

  // =========================
  // RESULT
  // =========================
  const character = result?.predicted_character;

  const primary = character?.color || '#3b82f6';

  // simple contrast (white or black text)
  const getContrast = (hex: string) => {
    if (!hex) return '#000';
    const c = hex.substring(1); // remove #
    const rgb = parseInt(c, 16);
    const r = (rgb >> 16) & 255;
    const g = (rgb >> 8) & 255;
    const b = rgb & 255;

    const luminance = (0.299 * r + 0.587 * g + 0.114 * b) / 255;
    return luminance > 0.5 ? '#000' : '#fff';
  };

  const contrast = getContrast(primary);

  if (result) {
    const matches = result?.matches || [];
    const topMatch = matches?.[0];
    const primaryMatch = matches[0] || null;
    const secondMatch = matches[1] || null;
    const thirdMatch = matches[2] || null;

    

    

    
    
  

    const primary =
      primaryMatch?.character?.geometry?.color ||
      result?.predicted_character?.color ||
      "#3b82f6";

    const traitLabels: Record<string, string> = {
      ACTION: "Action Oriented",
      ANALYTICAL: "Analytical",
      EMPATHETIC: "Empathetic",
      JUSTICE_DRIVEN: "Justice Driven",
      AMBITIOUS: "Ambitious",
      CREATIVE: "Creative",
      LOYAL: "Loyal",
      DISCIPLINED: "Disciplined",
      HUMOROUS: "Humorous",
      CURIOUS: "Curious",
      PRAGMATIC: "Pragmatic",
      REBELLIOUS: "Rebellious",
    };

    const formatTrait = (trait: string) =>
      traitLabels[trait] || trait.replaceAll("_", " ");

    const inferenceSignals =
      primaryMatch?.matching_traits
        ?.slice(0, 3)
        .map((trait: any) => ({
          name: formatTrait(trait.trait),
          similarity: Math.round(trait.similarity * 100),
        })) || [];

    

    const confidencePct =
      primaryMatch?.score ??
      result?.confidence ??
      undefined;

    const score = confidencePct !== undefined
      ? Math.round(Number(confidencePct))
      : null;

    const Meter = ({
      label,
      value,
      accent = primary,
    }: {
      label: string;
      value: number;
      accent?: string;
    }) => (
      <div>
        <div className="mb-1.5 flex items-center justify-between">
          <span className="retro-label text-[#77746d]">{label}</span>
          <span
            className="font-mono text-[11px] tabular-nums"
            style={{ color: accent }}
          >
            {Math.round(value * 100)}%
          </span>
        </div>
        <div className="relative h-2 overflow-hidden bg-black/[0.08]">
          <div
            className="h-full transition-[width] duration-1000 ease-out"
            style={{
              width: scanned ? `${Math.max(0, Math.min(100, Math.round(value * 100)))}%` : "0%",
              background: accent,
            }}
          />
          <div
            className="absolute inset-y-0 left-0 w-px opacity-30"
            style={{ background: accent }}
          />
        </div>
      </div>
    );

    const rankItems = [
      { rank: 2, match: secondMatch },
      { rank: 3, match: thirdMatch },
    ];

    return (
      <div
        className={`min-h-dvh w-full overflow-x-hidden bg-[#11110f] text-[#e9e4d7] transition-opacity duration-700 ${
          entering ? "opacity-0" : "opacity-100"
        }`}
      >
        <style>{`
          @import url('https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@500;600;700;800;900&family=IBM+Plex+Mono:wght@400;500;600&display=swap');

          .retro-page {
            font-family: 'IBM Plex Mono', ui-monospace, monospace;
          }

          .retro-display {
            font-family: 'Barlow Condensed', Impact, sans-serif;
          }

          .retro-label {
            font-family: 'IBM Plex Mono', ui-monospace, monospace;
            font-size: 9px;
            line-height: 1;
            text-transform: uppercase;
            letter-spacing: .18em;
          }

          .paper-noise {
            background-image:
              radial-gradient(rgba(255,255,255,.035) .7px, transparent .7px),
              radial-gradient(rgba(0,0,0,.08) .7px, transparent .7px);
            background-position: 0 0, 4px 4px;
            background-size: 8px 8px;
          }

          .scan-lines {
            background-image: repeating-linear-gradient(
              0deg,
              transparent 0px,
              transparent 3px,
              rgba(255,255,255,.018) 4px
            );
          }

          .result-rule {
            background: repeating-linear-gradient(
              90deg,
              rgba(233,228,215,.16) 0,
              rgba(233,228,215,.16) 1px,
              transparent 1px,
              transparent 7px
            );
          }

          @media (prefers-reduced-motion: reduce) {
            *, *::before, *::after {
              animation-duration: .01ms !important;
              transition-duration: .01ms !important;
            }
          }
        `}</style>

        <div className="retro-page paper-noise relative min-h-dvh">
          {/* restrained retro-futurist atmosphere */}
          <div
            className="pointer-events-none absolute inset-0 opacity-[0.11]"
            style={{
              background: `
                radial-gradient(ellipse at 50% 25%, ${primary} 0%, transparent 38%),
                radial-gradient(ellipse at 100% 100%, #6d5842 0%, transparent 32%)
              `,
            }}
          />
          <div className="scan-lines pointer-events-none absolute inset-0 opacity-60" />

          <div className="relative mx-auto flex min-h-dvh w-full max-w-[1600px] flex-col px-5 sm:px-8 lg:px-12">
            {/* TOP IDENTITY STRIP */}
            <header className="flex h-[68px] shrink-0 items-center justify-between border-b border-[#e9e4d7]/10">
              <Link
                href="/"
                className="group retro-label flex items-center gap-3 text-[#817c72] transition-colors hover:text-[#e9e4d7]"
              >
                <span className="text-sm transition-transform group-hover:-translate-x-1">
                  ←
                </span>
                return / quiz
              </Link>

              <div className="hidden items-center gap-4 sm:flex">
                <span className="retro-label text-[#5e5a53]">
                  {franchise}.dat
                </span>
                <span className="h-1 w-1 rounded-full bg-[#5e5a53]" />
                <span
                  className="retro-label"
                  style={{ color: primary }}
                >
                  analysis complete
                </span>
              </div>

              <button
                onClick={restartQuiz}
                className="group inline-flex items-center gap-4 self-start border border-[#e9e4d7]/20 px-5 py-3 transition-all duration-200 hover:border-[#e9e4d7]/45 hover:bg-[#e9e4d7]/[0.04] active:translate-y-px sm:self-auto"
              >
                <span className="retro-label text-[#aaa499]">
                  Run again
                </span>
                <span
                  className="text-sm transition-transform duration-200 group-hover:translate-x-1"
                  style={{ color: primary }}
                >
                  →
                </span>
              </button>
            </header>

            {/* MAIN COMPOSITION */}
            <main className="grid flex-1 grid-cols-1 gap-0 lg:grid-cols-[minmax(0,1fr)_340px]">
              {/* =====================================================
                  PRIMARY RESULT — intentionally dominates the page
              ====================================================== */}
              <section className="relative flex min-h-[720px] flex-col justify-between border-b border-[#e9e4d7]/10 py-10 lg:min-h-0 lg:border-b-0 lg:border-r lg:py-12 lg:pr-12 xl:pr-16">
                {/* little instrument marks */}
                <div className="flex items-start justify-between">
                  <div>
                    <div className="retro-label mb-3 text-[#5e5a53]">
                      subject identified
                    </div>
                    <div className="flex items-center gap-2">
                      <span
                        className="h-1.5 w-1.5 rounded-full"
                        style={{
                          background: primary,
                          boxShadow: `0 0 10px ${primary}`,
                        }}
                      />
                      <span className="retro-label text-[#aaa499]">
                        personality profile
                      </span>
                    </div>
                  </div>

                  {score !== null && (
                    <div className="text-right">
                      <div
                        className="retro-display text-5xl font-black leading-[.8] tracking-[-.02em] sm:text-6xl"
                        style={{ color: primary }}
                      >
                        {score}
                      </div>
                      <div className="retro-label mt-2 text-[#625e56]">
                        match index
                      </div>
                    </div>
                  )}
                </div>

                {/* Result title + image */}
                <div className="relative grid min-h-0 flex-1 items-center gap-8 py-6 lg:grid-cols-[minmax(0,1fr)_390px] lg:gap-12 xl:gap-16">

  {/* =========================
      RESULT TEXT
  ========================= */}
  <div className="relative z-10 flex min-w-0 flex-col">

    {/* Small label */}
    <div
      className={`retro-label mb-4 text-[#625e56] transition-all duration-500 ${
        scanned
          ? "translate-x-0 opacity-100"
          : "-translate-x-4 opacity-0"
      }`}
    >
      your result is
    </div>

    {/* CHARACTER TITLE */}
    <h1
      className={`retro-display max-w-4xl text-[clamp(4.5rem,9vw,10rem)] font-black uppercase leading-[.76] tracking-[-.035em] text-[#eee9dd] transition-all duration-700 ${
        scanned
          ? "translate-x-0 opacity-100"
          : "-translate-x-5 opacity-0"
      }`}
      style={{
        textShadow: `4px 4px 0 ${primary}18`,
      }}
    >
      {primaryMatch?.name || "UNKNOWN"}
    </h1>

    {/* Accent line */}
    <div
      className={`mt-5 h-[2px] w-full max-w-[520px] origin-left transition-transform duration-700 ${
        scanned ? "scale-x-100" : "scale-x-0"
      }`}
      style={{ background: primary }}
    />

    {/* TAG / TAGLINE */}
    {primaryMatch?.tagline && (
      <div
        className={`mt-5 transition-all delay-150 duration-700 ${
          scanned
            ? "translate-y-0 opacity-100"
            : "translate-y-2 opacity-0"
        }`}
      >
        <div className="retro-label mb-2 text-[#5e5a53]">
          profile designation
        </div>

        <p
          className="retro-display text-xl font-semibold uppercase tracking-wide sm:text-2xl"
          style={{ color: primary }}
        >
          {primaryMatch.tagline}
        </p>
      </div>
    )}

    {/* DESCRIPTION */}
    {primaryMatch?.description && (
      <div
        className={`mt-6 max-w-2xl transition-all delay-200 duration-700 ${
          scanned
            ? "translate-y-0 opacity-100"
            : "translate-y-2 opacity-0"
        }`}
      >
        <div className="retro-label mb-2 text-[#5e5a53]">
          profile readout
        </div>

        <p className="text-sm leading-6 text-[#858078] sm:text-[15px]">
          {primaryMatch.description}
        </p>
      </div>
    )}

    {/* ALIGNMENT BAR */}
    {score !== null && (
      <div
        className={`mt-7 max-w-2xl transition-all delay-300 duration-700 ${
          scanned
            ? "translate-y-0 opacity-100"
            : "translate-y-2 opacity-0"
        }`}
      >
        <div className="mb-2 flex items-center justify-between">
          <span className="retro-label text-[10px] text-[#5e5a53]">
            alignment
          </span>

          <span
            className="retro-label text-[10px]"
            style={{ color: primary }}
          >
            {score}/100
          </span>
        </div>

        <div className="result-rule relative h-2 overflow-hidden">
          <div
            className="h-full transition-[width] duration-1000 ease-out"
            style={{
              width: scanned
                ? `${Math.max(0, Math.min(100, score))}%`
                : "0%",
              background: primary,
            }}
          />
        </div>
      </div>
    )}
  </div>


  {/* =========================
      CHARACTER IMAGE
  ========================= */}
  {primaryMatch?.image && (
    <div
      className={`relative mx-auto flex h-full min-h-0 w-full max-w-[390px] items-center justify-center transition-all delay-100 duration-1000 ${
        scanned
          ? "translate-y-0 opacity-100"
          : "translate-y-6 opacity-0"
      }`}
    >
      {/* Technical frame */}
      <div
        className="pointer-events-none absolute inset-2 border"
        style={{ borderColor: `${primary}45` }}
      />

      <div
        className="pointer-events-none absolute -left-1 -top-1 h-7 w-7 border-l border-t"
        style={{ borderColor: primary }}
      />

      <div
        className="pointer-events-none absolute -bottom-1 -right-1 h-7 w-7 border-b border-r"
        style={{ borderColor: primary }}
      />

      <div className="absolute left-5 top-5 z-20 retro-label text-[#5e5a53]">
        portrait / 01
      </div>

      {/* Portrait */}
      <div className="relative flex h-full max-h-[520px] w-full items-center justify-center p-5 sm:p-7">

        <div
          className="pointer-events-none absolute h-[65%] w-[65%] rounded-full blur-[70px] opacity-20"
          style={{ background: primary }}
        />

        <img
          src={primaryMatch.image}
          alt={primaryMatch.name}
          className="relative z-10 max-h-full max-w-full object-contain drop-shadow-[0_20px_30px_rgba(0,0,0,.4)]"
        />

        {/* MATCH STAMP */}
        {score !== null && scanned && (
          <div
            key={`character-match-stamp-${score}`}
            className="stamp absolute bottom-[10%] right-[2%] z-30"
            style={{ color: primary }}
          >
            <div
              className="relative border-2 px-4 py-3"
              style={{
                borderColor: primary,
                background: `${primary}12`,
                boxShadow: `
                  4px 4px 0 ${primary}20,
                  0 0 20px ${primary}18
                `,
                textShadow: `0 0 8px ${primary}55`,
              }}
            >
              <div className="retro-label text-[8px] opacity-70">
                MATCH
              </div>

              <div className="retro-display text-4xl font-black leading-[.85] sm:text-5xl">
                {score}%
              </div>

              <div
                className="my-1.5 h-px opacity-50"
                style={{ background: primary }}
              />

              <div className="retro-label text-[7px] opacity-60">
                VERIFIED
              </div>
            </div>
          </div>
        )}
      </div>

      <div className="absolute bottom-4 right-5 retro-label text-[#5e5a53]">
        img_ref // active
      </div>
    </div>
  )}
</div>

                {/* Bottom description + meter */}
               
              </section>

              {/* =====================================================
                  SECONDARY DATA — clearly subordinate
              ====================================================== */}
              <aside className="flex flex-col lg:pl-8 xl:pl-10">
                {/* WHY */}
                
                <section className="border-b border-[#e9e4d7]/10 py-7">
  <div className="mb-6 flex items-end justify-between">
    <div>
      <span className="retro-label text-[#5e5a53]">01</span>

      <h2 className="retro-display mt-1 text-3xl font-bold uppercase tracking-wide text-[#ddd8cc]">
        Why this one
      </h2>
    </div>

    <span className="retro-label text-[#5e5a53]">
      {topMatch?.signals?.length ?? 0} signals
    </span>
  </div>

  {topMatch?.signals?.length ? (
    <div className="divide-y divide-[#e9e4d7]/10">
      {topMatch.signals.map((signal: any, index: number) => {
        const userPercent = Math.round(
          (signal.user_strength ?? 0) * 100
        );

        const characterPercent = Math.round(
          (signal.character_strength ?? 0) * 100
        );

        const difference = characterPercent - userPercent;
        const trait = signal.trait.replaceAll("_", " ");

        const interpretation =
          Math.abs(difference) <= 3
            ? `You and ${topMatch.name} are almost identical here.`
            : Math.abs(difference) <= 8
              ? `You and ${topMatch.name} are very similar here.`
              : difference > 0
                ? `${topMatch.name} leans more into this than you do.`
                : `You lean more into this than ${topMatch.name}.`;
                

        return (
          <div
            key={signal.trait}
            className="py-4 first:pt-0 last:pb-0"
          >
            {/* Top line */}
            <div className="mb-2 flex items-center justify-between">
              <div className="flex items-center gap-2">
                <span className="font-mono text-[9px] text-[#4f4b45]">
                  0{index + 1}
                </span>

                <span className="retro-label text-sm tracking-[0.14em] text-[#aaa59b]">
                  {trait}
                </span>
              </div>

              <span className="font-mono text-[9px] text-[#5e5a53]">
                {difference === 0
                  ? "MATCH"
                  : `${difference > 0 ? "+" : ""}${difference}%`}
              </span>
            </div>

            {/* Comparison */}
            <div className="flex items-baseline justify-between">
              <div className="flex items-baseline gap-2">
                <span className="text-[9px] uppercase tracking-[0.18em] text-[#5e5a53]">
                  You
                </span>

                <span className="retro-display text-3xl font-bold leading-none text-[#ddd8cc]">
                  {userPercent}%
                </span>
              </div>

              <span className="px-3 text-xs text-[#4f4b45]">
                ↔
              </span>

              <div className="flex items-baseline gap-2">
                <span className="retro-display text-2xl font-bold leading-none text-[#ddd8cc]">
                  {characterPercent}%
                </span>

                <span className="text-[9px] uppercase tracking-[0.18em] text-[#5e5a53]">
                  {topMatch.name}
                </span>
              </div>
            </div>

            {/* Interpretation */}
            <p className="mt-2 text-[10px] leading-4 text-[#77736b]">
              {interpretation}
            </p>
          </div>
        );
      })}
    </div>
  ) : (
    <p className="text-xs leading-5 text-[#77736b]">
      The strongest pattern across your answers points here.
    </p>
  )}
</section>

                {/* OTHER MATCHES */}
                <section className="border-b border-[#e9e4d7]/10 py-8">
                  <div className="mb-6 flex items-end justify-between">
                    <div>
                      <span className="retro-label text-[#5e5a53]">02</span>
                      <h2 className="retro-display mt-1 text-3xl font-bold uppercase tracking-wide text-[#ddd8cc]">
                        Other matches
                      </h2>
                    </div>
                    <span className="retro-label text-[#5e5a53]">rank</span>
                  </div>

                  <div className="space-y-2">
                    {rankItems.map(({ rank, match }) => (
                      <div
                        key={rank}
                        className={`group relative flex min-h-[82px] items-center gap-4 border border-[#e9e4d7]/10 px-3 transition-all duration-500 hover:border-[#e9e4d7]/25 ${
                          scanned
                            ? "translate-x-0 opacity-100"
                            : "translate-x-3 opacity-0"
                        }`}
                        style={{
                          transitionDelay: `${250 + (rank - 2) * 100}ms`,
                        }}
                      >
                        <span className="retro-display w-8 text-3xl font-bold text-[#4f4b45]">
                          {String(rank).padStart(2, "0")}
                        </span>

                        {match?.image && (
                          <div className="h-14 w-14 shrink-0 overflow-hidden border border-[#e9e4d7]/10 bg-[#191814]">
                            <img
                              src={match.image}
                              alt={match.name}
                              className="h-full w-full object-contain opacity-80 transition-opacity group-hover:opacity-100"
                            />
                          </div>
                        )}

                        {match ? (
                          <div className="min-w-0 flex-1">
                            <div className="truncate text-xs font-semibold uppercase tracking-wide text-[#c8c2b6]">
                              {match.name}
                            </div>
                            <div className="mt-1 retro-label text-[#5e5a53]">
                              secondary signal
                            </div>
                          </div>
                        ) : (
                          <span className="retro-label text-[#48443f]">
                            no signal
                          </span>
                        )}

                        {match?.score !== undefined && (
                          <span className="font-mono text-[11px] text-[#77736b]">
                            {Math.round(Number(match.score))}%
                          </span>
                        )}
                      </div>
                    ))}
                  </div>
                </section>

                
              </aside>
            </main>

            {/* FOOTER */}
            <footer className="flex shrink-0 flex-col gap-4 border-t border-[#e9e4d7]/10 py-5 sm:flex-row sm:items-center sm:justify-between">
              <div className="flex items-center gap-4">
                <span className="retro-label text-[#4f4b45]">
                  profile // complete
                </span>
                <span className="hidden h-px w-12 bg-[#4f4b45] sm:block" />
                <span className="retro-label text-[#4f4b45]">
                  {franchise}
                </span>
              </div>

              
            </footer>
          </div>
        </div>
      </div>
    );
  }
  // =========================
  // NO QUESTION
  // =========================
  if (!question) {
    return (
      <div className="flex min-h-screen items-center justify-center bg-[#080808] p-6 text-white">
        <div
          className="
            border border-white/20
            bg-[#0b0b0b]
            px-8 py-6
            font-mono text-xs
            uppercase tracking-[0.25em]
            text-white/50
            shadow-[8px_8px_0_0_#3b82f6]
          "
        >
          <span className="text-[#3b82f6]">ERROR //</span> No question
          available.
        </div>
      </div>
    );
  }

  // =========================
  // QUESTION
  // =========================
  return (
    <div className="relative flex min-h-screen flex-col overflow-hidden bg-[#080808] text-white">
      <div className="absolute inset-0 bg-[linear-gradient(to_bottom,transparent,rgba(255,255,255,0.05),transparent)] animate-pulse pointer-events-none" />

      {/* HEADER */}
      <header
        className="
          relative z-20
          flex items-center justify-between
          gap-4
          border-b border-white/10
          px-5 py-5
          md:px-8
        "
      >
        <Link
          href="/"
          className="
            font-mono text-[9px]
            uppercase tracking-[0.25em]
            text-white/40
            transition-colors
            hover:text-[#3b82f6]
          "
        >
          ← Return to Archive
        </Link>

        <div
          className="
            hidden items-center gap-3
            font-mono text-[9px]
            uppercase tracking-[0.3em]
            text-white/30
            sm:flex
          "
        >
          <span className="h-px w-8 bg-white/20" />
          <span>{franchise}</span>
          <span className="h-1.5 w-1.5 animate-pulse bg-[#3b82f6]" />
          <span>Resonance Sequence</span>
          <span className="h-px w-8 bg-white/20" />
        </div>

        <div
          className="
            font-mono text-[9px]
            tabular-nums
            tracking-[0.25em]
            text-white/50
          "
        >
          {String(questionNumber).padStart(2, '0')}
        </div>
      </header>

      {/* PROGRESS (indeterminate — total question count isn't returned by the API) */}
      <div className="relative z-20 h-[2px] w-full overflow-hidden bg-white/10">
        <div className="h-full w-1/3 animate-pulse bg-[#3b82f6] shadow-[0_0_12px_rgba(59,130,246,0.8)]" />
      </div>

      {/* QUESTION BODY */}
      <main
        className={`
          relative z-10
          flex flex-1
          items-center
          px-5 py-12
          transition-all
          duration-300
          md:px-12
          lg:px-20
          ${entering ? 'translate-x-5 opacity-0' : 'translate-x-0 opacity-100'}
        `}
      >
        <div className="mx-auto w-full max-w-6xl">
          <div
            className="
              mb-7
              flex items-center gap-3
              font-mono text-[9px]
              uppercase tracking-[0.35em]
              text-[#3b82f6]
            "
          >
            <span className="h-1.5 w-1.5 bg-[#3b82f6]" />
            Sequence // {String(questionNumber).padStart(2, '0')}
            <span className="h-px w-12 bg-[#3b82f6]/40" />
          </div>

          <h2
            className="
              max-w-5xl
              text-3xl font-display font-bold
              uppercase leading-[0.95]
              
              md:text-6xl
              lg:text-7xl
            "
          >
            {question.question}
          </h2>

          <div className="mt-12 grid gap-5 md:grid-cols-2">
            {Object.entries(question.options).map(
              ([key, option]: any, index: number) => {
                const isSelected = selectedKey === key;

                return (
                  <button
                    key={key}
                    onClick={() => {
                      if (!loading && !selectedKey) {
                        handleAnswer(key);
                      }
                    }}
                    disabled={loading}
                    className={`
                      group
                      relative
                      min-h-[110px]
                      overflow-hidden
                      border
                      p-6
                      text-left
                      transition-all
                      duration-200
                      disabled:cursor-not-allowed
                      ${
                        isSelected
                          ? `
                            translate-x-[5px]
                            translate-y-[5px]
                            border-[#3b82f6]
                            bg-[#3b82f6]
                            text-black
                            shadow-none
                          `
                          : `
                            border-white/15
                            bg-[#0b0b0b]
                            text-white
                            shadow-[6px_6px_0_0_rgba(59,130,246,0.35)]
                            hover:-translate-y-1
                            hover:border-[#3b82f6]
                            hover:shadow-[7px_7px_0_0_#3b82f6]
                          `
                      }
                    `}
                  >
                    <span
                      className="
                        absolute left-0 top-0
                        h-full w-[2px]
                        bg-[#3b82f6]
                        opacity-0
                        transition-opacity
                        group-hover:opacity-100
                      "
                    />

                    <div className="flex items-start gap-5">
                      <span
                        className={`
                          mt-1
                          font-mono text-[10px]
                          tracking-[0.2em]
                          ${isSelected ? 'text-black/60' : 'text-[#3b82f6]'}
                        `}
                      >
                        [{String.fromCharCode(65 + index)}]
                      </span>

                      <span
                        className="
                          text-base font-bold
                          uppercase leading-snug
                          tracking-wide
                          md:text-lg
                        "
                      >
                        {option.text}
                      </span>
                    </div>

                    <span
                      className={`
                        absolute bottom-3 right-3
                        h-2 w-2
                        border-b border-r
                        ${isSelected ? 'border-black/40' : 'border-white/20'}
                      `}
                    />
                  </button>
                );
              }
            )}
          </div>
        </div>
      </main>

      {/* FOOTER */}
      <footer
        className="
          relative z-20
          flex items-center justify-between
          border-t border-white/10
          px-5 py-4
          font-mono text-[8px]
          uppercase tracking-[0.25em]
          text-white/30
          md:px-8
        "
      >
        <div className="flex items-center gap-3">
          <span
            className={`
              h-1.5 w-1.5
              ${selectedKey ? 'animate-pulse bg-[#3b82f6]' : 'bg-white/20'}
            `}
          />
          Sequence Position // {String(questionNumber).padStart(2, '0')}
        </div>

        <span className="hidden sm:block">
          {selectedKey
            ? 'Signal Captured // Processing'
            : 'Select Response To Continue'}
        </span>
      </footer>
    </div>
  );
}