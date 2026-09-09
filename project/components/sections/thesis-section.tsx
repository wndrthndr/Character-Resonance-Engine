'use client';

import { DossierSection } from '@/components/dossier-section';

export function ThesisSection() {
  return (
    <DossierSection
      index={2}
      label="03 / THESIS"
      fileId="AX-0900"

    >
      <div className="relative flex h-full min-h-[80vh] items-center overflow-hidden">

        {/* Background atmosphere */}
        <div className="pointer-events-none absolute inset-0">
          <div
            className="absolute inset-0 opacity-[0.045]"
            style={{
              backgroundImage: `
                linear-gradient(rgba(255,255,255,.18) 1px, transparent 1px),
                linear-gradient(90deg, rgba(255,255,255,.18) 1px, transparent 1px)
              `,
              backgroundSize: '100px 100px',
            }}
          />

          <div className="absolute left-[18%] top-[28%] h-[30rem] w-[30rem] rounded-full bg-blue-500/[0.035] blur-[140px]" />
        </div>

        {/* Main composition */}
        <div className="relative z-10 w-full px-8 py-24 md:px-16 lg:px-24">

          {/* Eyebrow */}
          <div className="mb-14 flex items-center gap-4">
            <span className="h-px w-16 bg-blue-500/70" />

            <span className="font-mono text-[9px] uppercase tracking-[0.4em] text-blue-400/70">
              The Idea
            </span>
          </div>

          {/* Statement */}
          <div className="max-w-6xl">
            <h2 className="text-[clamp(3.8rem,9vw,9rem)] font-black uppercase leading-[0.82] tracking-[-0.065em] text-white">
              Fictional
              <br />
              Characters
              <br />
              <span className="text-white/20">
                Are Mirrors.
              </span>
            </h2>
          </div>

          {/* Supporting thought */}
          <div className="mt-16 flex flex-col gap-12 lg:flex-row lg:items-end lg:justify-between">

            <div className="max-w-xl">
              <p className="font-mono text-[11px] leading-7 tracking-[0.07em] text-white/45 md:text-xs">
                We recognize ourselves in characters because
                something about them feels familiar.
              </p>

              <p className="mt-5 font-mono text-[11px] leading-7 tracking-[0.07em] text-white/30 md:text-xs">
                Not their story. Not their abilities.
                <br />
                Their way of thinking.
              </p>
            </div>

            {/* Closing statement */}
            <div className="max-w-sm border-l border-white/10 pl-6">
              <div className="font-mono text-[8px] uppercase tracking-[0.35em] text-white/20">
                Final Observation
              </div>

              <p className="mt-4 text-lg font-medium leading-7 tracking-tight text-white/70 md:text-xl">
                Every choice leaves a trace.
                <br />
                Every trace forms a pattern.
              </p>
            </div>

          </div>

          {/* Bottom line */}
          <div className="mt-24 flex items-center justify-between border-t border-white/10 pt-6">

            <span className="font-mono text-[8px] uppercase tracking-[0.3em] text-white/20">
              Archive // AX-0900
            </span>

            <span className="font-mono text-[8px] uppercase tracking-[0.3em] text-white/20">
              End Of Transmission
            </span>

          </div>

        </div>
      </div>
    </DossierSection>
  );
}