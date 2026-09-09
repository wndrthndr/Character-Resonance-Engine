'use client';

import { useEffect, useState, useRef } from 'react';
import { DossierSection } from '@/components/dossier-section';
/* ==============================================================
   RESONANCE FLIP GRID
   Temporary solid-color version for testing.
============================================================== */

// Every tile gets a color from this palette (kept inside the blue /
// indigo / teal / slate family already established elsewhere on the
// page), rather than only a handful of "special" cells.
const RESONANCE_PALETTE = [
  '#172554', '#1e3a8a', '#1d4ed8', '#1e40af',
  '#312e81', '#3730a3', '#4338ca', '#4c1d95',
  '#164e63', '#155e75', '#134e4a', '#115e59',
  '#1e293b', '#334155', '#3f3f46', '#0f172a',
];

function tileColor(index: number) {
  // Odd stride relative to the palette length keeps adjacent tiles
  // from repeating the same color, without relying on Math.random()
  // (which would cause a server/client hydration mismatch).
  return RESONANCE_PALETTE[(index * 5 + 3) % RESONANCE_PALETTE.length];
}

function ResonanceFlipGrid({ mounted }: { mounted: boolean }) {
  const columns = 8;
  const rows = 5;
  const totalCells = columns * rows;
  const centerRow = (rows - 1) / 2;
  const centerCol = (columns - 1) / 2;

  // Click/tap opens a tile fully, holds it open, then closes it on its
  // own — works on touch devices where hover never fires, and gives
  // desktop clicks a deliberate "open then close" beat instead of
  // snapping shut the instant the cursor drifts off.
  const [openIndex, setOpenIndex] = useState<number | null>(null);
  const closeTimer = useRef<ReturnType<typeof setTimeout> | null>(null);

  const handleOpen = (index: number) => {
    if (closeTimer.current) clearTimeout(closeTimer.current);
    setOpenIndex(index);
    closeTimer.current = setTimeout(() => setOpenIndex(null), 1400);
  };

  useEffect(() => {
    return () => {
      if (closeTimer.current) clearTimeout(closeTimer.current);
    };
  }, []);

  return (
    <div className="resonance-grid pointer-events-auto absolute inset-0 z-[5]">
      <div
        className="grid h-full w-full"
        style={{
          gridTemplateColumns: `repeat(${columns}, 1fr)`,
          gridTemplateRows: `repeat(${rows}, 1fr)`,
        }}
      >
        {Array.from({ length: totalCells }).map((_, index) => {
          const color = tileColor(index);
          const row = Math.floor(index / columns);
          const col = index % columns;
          // Distance from center drives the flare timing, so the
          // whole grid ignites as one outward wave on page load
          // instead of firing all at once.
          const distance = Math.abs(row - centerRow) + Math.abs(col - centerCol);
          const delay = 250 + distance * 70;
          const isOpen = openIndex === index;

          return (
            <div
              key={index}
              onClick={() => handleOpen(index)}
              className="resonance-tile group relative min-h-0 min-w-0 cursor-pointer border border-white/[0.035]"
              style={{ perspective: '900px' }}
            >
              {/* FLARE — a brief radial glow burst in the tile's own
                  color, timed with the flip below, once on mount */}
              {mounted && (
                <span
                  className="tile-flare pointer-events-none absolute inset-0 z-10"
                  style={{
                    background: `radial-gradient(circle at 50% 50%, ${color} 0%, transparent 72%)`,
                    animationDelay: `${delay}ms`,
                  }}
                />
              )}

              <div
                className="resonance-tile-inner relative h-full w-full transition-transform duration-650 ease-[cubic-bezier(0.16,1,0.3,1)] group-hover:[transform:rotateY(180deg)]"
                style={{
                  transformStyle: 'preserve-3d',
                  transform: isOpen ? 'rotateY(180deg)' : undefined,
                  animation: mounted
                    ? `tile-flip-flare 820ms ease-out ${delay}ms 1`
                    : undefined,
                }}
              >
                {/* FRONT — carries a faint permanent tint of the
                    tile's color, so the grid reads as colored even
                    before/after the flare and outside of hover */}
                <div
                  className="resonance-tile-face absolute inset-0 flex items-center justify-center"
                  style={{
                    backgroundColor: color,
                    opacity: 0.05,
                    backfaceVisibility: 'hidden',
                    WebkitBackfaceVisibility: 'hidden',
                  }}
                >
                  <span
                    className="h-[3px] w-[3px] rounded-full"
                    style={{ backgroundColor: color, opacity: 0.6 }}
                  />
                </div>

                {/* BACK — full-strength color, revealed by the mount
                    flare and again on hover */}
                <div
                  className="resonance-tile-back absolute inset-0 overflow-hidden"
                  style={{
                    backgroundColor: color,
                    backfaceVisibility: 'hidden',
                    WebkitBackfaceVisibility: 'hidden',
                    transform: 'rotateY(180deg)',
                  }}
                >
                  <div className="absolute inset-0 bg-[repeating-linear-gradient(to_bottom,transparent_0px,transparent_3px,rgba(255,255,255,0.08)_4px)]" />
                  <div className="absolute left-1/2 top-1/2 h-5 w-5 -translate-x-1/2 -translate-y-1/2 border border-white/30" />
                  <span className="absolute bottom-2 right-2 font-mono text-[6px] tracking-[0.2em] text-white/35">
                    SIG_{String(index).padStart(2, '0')}
                  </span>
                </div>
              </div>
            </div>
          );
        })}
      </div>
    </div>
  );
}

export function AtmosphereSection() {
  const [mounted, setMounted] = useState(false);
  const word = "ECHO".split("");
  const handleBegin = () => {
    window.scrollTo({
      top: window.innerHeight*2,
      behavior: 'smooth',
    });
  };
  const handleChar = () => {
    window.scrollTo({
      top: window.innerHeight*3,
      behavior: 'smooth',
    });
  };
  useEffect(() => {
    const timer = setTimeout(() => {
      setMounted(true);
    }, 100);

    return () => clearTimeout(timer);
  }, []);

  function MagneticCTA({
    onClick,
    children,
  }: {
    onClick: () => void;
    children: React.ReactNode;
  }) {
    const ref = useRef<HTMLButtonElement>(null);
    const [offset, setOffset] = useState({ x: 0, y: 0 });
    const [hovering, setHovering] = useState(false);
  
    const handleMove = (e: React.MouseEvent<HTMLButtonElement>) => {
      const rect = ref.current?.getBoundingClientRect();
      if (!rect) return;
      const x = e.clientX - rect.left - rect.width / 2;
      const y = e.clientY - rect.top - rect.height / 2;
      setOffset({ x: x * 0.22, y: y * 0.32 });
    };
  
    const handleLeave = () => {
      setHovering(false);
      setOffset({ x: 0, y: 0 });
    };
  
    return (
      <button
        ref={ref}
        onClick={onClick}
        onMouseMove={handleMove}
        onMouseEnter={() => setHovering(true)}
        onMouseLeave={handleLeave}
        style={{
          transform: `translate(${offset.x}px, ${offset.y}px)`,
          transition: hovering
            ? 'transform 180ms cubic-bezier(0.16,1,0.3,1)'
            : 'transform 550ms cubic-bezier(0.34,1.56,0.64,1)',
        }}
        className="
          cta-sheen
          pointer-events-auto
          group
          relative
          inline-flex
          items-center
          gap-3
          overflow-hidden
          border
          border-[#3b82f6]/40
          bg-[#0b0f16]/70
          px-8
          py-4
          font-mono
          text-[11px]
          uppercase
          tracking-[0.35em]
          text-white
          transition-colors
          duration-300
          hover:border-[#3b82f6]
          hover:bg-[#111827]
          hover:shadow-[0_0_40px_rgba(59,130,246,0.18)]
        "
      >
        <span className="relative z-10 flex items-center gap-3">
          {children}
        </span>
      </button>
    );
  }
  
  return (
    <DossierSection
      index={0}
      label="01 / FRAGMENT"
      fileId="SIG-7792"
      className="bg-black text-white"
    >
      {/* =========================================================
          BACKGROUND
          Layered on purpose: base gradient -> grid -> ambient
          lights (3, not 1) -> waveform trace -> grain -> scan
          lines -> vignette. Flat black was reading empty because
          the old grid layer had a background-size but no actual
          background-image, so it never painted anything.
      ========================================================= */}

      <div className="pointer-events-none absolute inset-0 z-0 overflow-hidden">

        {/* Base gradient — gives the black actual depth instead of a flat fill */}
        <div
          className="absolute inset-0"
          style={{
            background:
              'radial-gradient(ellipse 130% 85% at 50% 8%, #0a0e18 0%, #030405 45%, #000000 80%)',
          }}
        />

        {/* Grid — now actually painted, faded toward the frame edges */}
        <div
          className="absolute inset-0 opacity-[0.16]"
          style={{
            backgroundImage:
              'linear-gradient(rgba(148,180,255,0.16) 1px, transparent 1px), linear-gradient(90deg, rgba(148,180,255,0.16) 1px, transparent 1px)',
            backgroundSize: '64px 64px',
            maskImage:
              'radial-gradient(ellipse 68% 60% at 50% 42%, black 15%, transparent 78%)',
            WebkitMaskImage:
              'radial-gradient(ellipse 68% 60% at 50% 42%, black 15%, transparent 78%)',
          }}
        />

        {/* Primary ambient light — blue, centered behind ECHO */}
        <div
          className="
            absolute
            left-1/2 top-1/2
            h-[520px] w-[820px]
            -translate-x-1/2
            -translate-y-1/2
            rounded-full
            bg-[#3b82f6]/[0.07]
            blur-[170px]
          "
        />

        {/* Secondary lights — indigo + teal, pulled from the flip-grid palette,
            offset off-center so the frame has more than one point of interest */}
        <div
          className="
            absolute
            left-[18%] top-[76%]
            h-[380px] w-[560px]
            -translate-x-1/2
            -translate-y-1/2
            rounded-full
            bg-[#312e81]/[0.11]
            blur-[150px]
          "
        />
        <div
          className="
            absolute
            left-[84%] top-[18%]
            h-[320px] w-[460px]
            -translate-x-1/2
            -translate-y-1/2
            rounded-full
            bg-[#134e4a]/[0.13]
            blur-[140px]
          "
        />

        {/* Resonance waveform — draws itself in once, ties directly to
            the "Trace the ECHO" copy instead of being generic decoration */}
        <svg
          className="absolute left-1/2 top-[46%] -translate-x-1/2 -translate-y-1/2"
          width="1400"
          height="280"
          viewBox="0 0 1400 280"
          fill="none"
          preserveAspectRatio="xMidYMid slice"
        >
          <path
            d="M0,140 C60,140 60,52 120,52 C180,52 180,214 240,214 C300,214 300,74 360,74 C420,74 420,196 480,196 C540,196 540,104 600,104 C660,104 660,182 720,182 C780,182 780,140 840,140 C900,140 900,52 960,52 C1020,52 1020,214 1080,214 C1140,214 1140,84 1200,84 C1260,84 1260,140 1400,140"
            stroke="#5b9dff"
            strokeWidth="1.5"
            pathLength="1"
            className="atmosphere-waveform-path"
          />
        </svg>

        {/* Grain — subtle static texture, on-brand for a "signal/decrypt" surface */}
        <div
          className="absolute inset-0 opacity-[0.05] mix-blend-overlay"
          style={{
            backgroundImage:
              "url(\"data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='120' height='120'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='2' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)'/%3E%3C/svg%3E\")",
          }}
        />

        {/* Vertical scan line */}
        <div
          className="
            atmosphere-scan
            absolute
            left-0 top-0
            h-full w-px
            bg-gradient-to-b
            from-transparent
            via-[#3b82f6]/60
            to-transparent
          "
        />

        {/* Horizontal scan */}
        <div
          className="
            atmosphere-scan-horizontal
            absolute
            left-0 top-0
            h-px w-full
            bg-gradient-to-r
            from-transparent
            via-[#3b82f6]/30
            to-transparent
          "
        />

        {/* CRT scanlines */}
        <div
          className="
            absolute inset-0
            opacity-[0.025]
            [background-image:linear-gradient(transparent_50%,rgba(255,255,255,0.08)_50%)]
            [background-size:100%_4px]
          "
        />

        {/* Vignette — pulls focus back to center, stops the grid/grain from
            feeling like it's tiling flatly to the frame */}
        <div
          className="absolute inset-0"
          style={{
            background:
              'radial-gradient(ellipse 88% 90% at 50% 50%, transparent 45%, rgba(0,0,0,0.7) 100%)',
          }}
        />
      </div>

      {/* Ping rings — the one bold, orchestrated motion moment. Fires once
          on load, radiating from center behind ECHO like a resonance pulse. */}
      {mounted && (
        <div className="pointer-events-none absolute left-1/2 top-[46%] z-[6] -translate-x-1/2 -translate-y-1/2">
          <span
            className="atmosphere-ping absolute left-1/2 top-1/2 rounded-full border border-[#5b9dff]/40"
            style={{ animationDelay: '550ms' }}
          />
          <span
            className="atmosphere-ping absolute left-1/2 top-1/2 rounded-full border border-[#5b9dff]/28"
            style={{ animationDelay: '820ms' }}
          />
          <span
            className="atmosphere-ping absolute left-1/2 top-1/2 rounded-full border border-[#5b9dff]/18"
            style={{ animationDelay: '1090ms' }}
          />
        </div>
      )}

      {/* INTERACTIVE FLIP GRID — outside pointer-events-none background */}
      <ResonanceFlipGrid mounted={mounted} />

      {/* =========================================================
          LEFT VERTICAL DATA
      ========================================================= */}

      <div
        className={`
          pointer-events-none
          absolute
          left-7 top-1/2
          z-20
          hidden
          -translate-y-1/2
          transition-all
          delay-500
          duration-1000
          lg:block

          ${
            mounted
              ? 'translate-x-0 opacity-100'
              : '-translate-x-6 opacity-0'
          }
        `}
      >
        <div className="flex items-center gap-5">

          <div
            className="
              h-36 w-px
              bg-gradient-to-b
              from-transparent
              via-white/20
              to-transparent
            "
          />

          <div
            className="
              [writing-mode:vertical-rl]
              rotate-180
              font-mono
              text-[8px]
              uppercase
              tracking-[0.4em]
              text-white/20
            "
          >
            Resonance Mapping SystemMapping
          </div>
        </div>
      </div>
      

      {/* =========================================================
          RIGHT SIDE COORDINATES
      ========================================================= */}

      <div
        className={`
          pointer-events-none
          absolute
          right-7 top-1/2
          z-20
          hidden
          -translate-y-1/2
          font-mono
          text-[8px]
          uppercase
          tracking-[0.25em]
          text-white/20
          transition-all
          delay-700
          duration-1000
          lg:block

          ${
            mounted
              ? 'translate-x-0 opacity-100'
              : 'translate-x-6 opacity-0'
          }
        `}
      >
        
      </div>

      {/* =========================================================
          MAIN CONTENT
      ========================================================= */}

      <main
        className="
          relative z-20 pointer-events-none
          flex h-full
          items-center
          justify-center
          px-6
          pb-20
          pt-20
        "
      >
        <div className="relative w-full max-w-6xl">

          {/* =====================================================
              STATUS
          ===================================================== */}

          <div
            className={`
              mb-8
              flex items-center
              justify-center
              transition-all
              delay-300
              duration-700

              ${
                mounted
                  ? 'translate-y-0 opacity-100'
                  : 'translate-y-4 opacity-0'
              }
            `}
          >
            <div
              className="
                flex items-center gap-3
                border border-[#3b82f6]/50
                bg-[#08090b]/80
                px-4 py-2
                font-mono
                text-[8px]
                uppercase
                tracking-[0.3em]
                text-[#3b82f6]
                backdrop-blur-sm
              "
            >
              <span className="relative flex h-1.5 w-1.5">
                <span
                  className="
                    absolute
                    inline-flex
                    h-full w-full
                    animate-ping
                    bg-[#3b82f6]
                    opacity-50
                  "
                />

                <span
                  className="
                    relative
                    inline-flex
                    h-1.5 w-1.5
                    bg-[#3b82f6]
                  "
                />
              </span>

              Awaiting resonance signature
            </div>
          </div>

          {/* =====================================================
              HERO TYPOGRAPHY
          ===================================================== */}

          <div className="relative mx-auto text-center">

            {/* TRACE THE */}
            <div
              className={`
                relative z-10
                overflow-hidden
                transition-all
                delay-500
                duration-1000

                ${
                  mounted
                    ? 'translate-y-0 opacity-100'
                    : 'translate-y-8 opacity-0'
                }
              `}
            >
              <div
                className="
                  font-mono
                  text-[10px]
                  uppercase
                  tracking-[0.7em]
                  text-white/30
                  md:text-xs
                "
              >
                Trace the
              </div>
            </div>

            {/* ECHO */}
            <div
              className={`
                relative
                mx-auto
                mt-2
                transition-all
                delay-700
                duration-1000

                ${
                  mounted
                    ? 'scale-100 opacity-100'
                    : 'scale-[0.94] opacity-0'
                }
              `}
            >
              {/* Main word */}
              <h1
  className="
    loki-container
    relative
    z-10
    select-none
    text-[7rem]
    font-black
    uppercase
    tracking-tight
    text-[#3b82f6]
    sm:text-[9rem]
    md:text-[11rem]
    lg:text-[13rem]
    rotate-[-5deg]
  "
  data-text="ECHO"
>
  <span className="loki-letter">E</span>
  <span className="loki-letter">C</span>
  <span className="loki-letter">H</span>
  <span className="loki-letter">O</span>
</h1>
              {/* Horizontal crossing line */}
              <div
                className="
                  absolute
                  retro-display
                  left-1/2 top-[52%]
                  z-20
                  h-px
                  w-[115%]
                  -translate-x-1/2
                  bg-gradient-to-r
                  from-transparent
                  via-white/15
                  to-transparent
                "
              />

              {/* Small glitch block */}
              <div
                className="
                  atmosphere-glitch-block
                  absolute
                  right-[12%]
                  top-[25%]
                  z-30
                  h-2
                  w-14
                  bg-[#3b82f6]
                "
              />

              <div
                className="
                  atmosphere-glitch-block-secondary
                  absolute
                  bottom-[18%]
                  left-[17%]
                  z-30
                  h-[2px]
                  w-20
                  bg-white/50
                "
              />
            </div>

            {/* ===================================================
                DESCRIPTION
            =================================================== */}

            <div
              className={`
                mx-auto
                mt-10
                flex
                max-w-lg
                items-start
                gap-5
                text-left
                transition-all
                delay-1000
                duration-1000

                ${
                  mounted
                    ? 'translate-y-0 opacity-100'
                    : 'translate-y-5 opacity-0'
                }
              `}
            >

              
            </div>
          </div>
          

          {/* =====================================================
              LOWER METRICS
          ===================================================== */}

<div
            className={`
              mx-auto
              mt-14
              flex
              justify-center
              border-y
              border-white/[0.07]
              py-6
              transition-all
              delay-[1200ms]
              duration-1000
              ease-[cubic-bezier(0.16,1,0.3,1)]
              flex-col
              gap-4
              w-[320px]

              ${
                mounted
                  ? 'translate-y-0 opacity-100'
                  : 'translate-y-4 opacity-0'
              }
            `}
          >
            <MagneticCTA onClick={handleBegin}>
              Begin Session
              <span className="transition-transform duration-300 group-hover:translate-x-1">
                →
              </span>
            </MagneticCTA>

            <MagneticCTA onClick={handleChar}>
              Characters
              <span className="transition-transform duration-300 group-hover:translate-x-1">
                →
              </span>
            </MagneticCTA>
          </div>
        </div>
      </main>

      {/* =========================================================
          BOTTOM TICKER
      ========================================================= */}

      <div
        className="
          pointer-events-none
          absolute
          bottom-14
          left-0
          z-20
          w-full
          overflow-hidden
          border-y
          border-white/[0.05]
          bg-black/20
          py-2
        "
      >
      
      </div>

      {/* =========================================================
          BOTTOM DATA
      ========================================================= */}

      <div
        className="
          pointer-events-none
          absolute
          bottom-6 left-7
          z-20
          font-mono
          text-[8px]
          uppercase
          tracking-[0.25em]
          text-white/20
        "
      >
        Engine_State // Idle
      </div>

      <div
        className="
          pointer-events-none
          absolute
          bottom-6 right-7
          z-20
          font-mono
          text-[8px]
          uppercase
          tracking-[0.25em]
          text-white/20
        "
      >
        Status // 0% Decrypted
      </div>

      {/* =========================================================
          LOCAL ANIMATION CSS
      ========================================================= */}

      <style jsx global>{`
        /* =========================================================
        RESONANCE FLIP GRID
     ========================================================= */
     
             .resonance-grid {
          perspective: 1400px;
          pointer-events: auto;
        }

        .resonance-tile {
          perspective: 900px;
        }

        .resonance-tile-inner {
          transform-style: preserve-3d;
          transition: transform 650ms cubic-bezier(0.16, 1, 0.3, 1);
        }

        .resonance-tile-front,
        .resonance-tile-back {
          backface-visibility: hidden;
          -webkit-backface-visibility: hidden;
        }

        .resonance-tile-back {
          transform: rotateY(180deg);
        }

        .resonance-tile:hover .resonance-tile-inner {
          transform: rotateY(180deg);
        }

        .resonance-tile:hover {
          z-index: 2;
        }

        /*
         * Boot-up flare: each tile's own color blooms and fades in a
         * radial burst, timed with the flip below, once on load.
         */
        .tile-flare {
          opacity: 0;
          animation: tile-flare-glow 780ms ease-out 1;
        }

        @keyframes tile-flare-glow {
          0% {
            opacity: 0;
          }
          35% {
            opacity: 0.9;
          }
          100% {
            opacity: 0;
          }
        }

        /*
         * Boot-up flip: tile turns to reveal its color, then settles
         * back to front. After this finishes, normal hover control
         * takes back over (this animation only ever runs once).
         */
        @keyframes tile-flip-flare {
          0% {
            transform: rotateY(0deg);
          }
          45% {
            transform: rotateY(180deg);
          }
          100% {
            transform: rotateY(0deg);
          }
        }

        /* =========================================================
        ECHO FONT CYCLE
        ========================================================= */

        .echo-font-cycle {
          animation:
            echo-font-change 8s steps(1, end) infinite,
            atmosphere-glitch-main 7s infinite;
        }

        @keyframes echo-font-change {
          0% {
            font-family: Impact, Haettenschweiler, "Arial Narrow Bold", sans-serif;
          }

          20% {
            font-family: Georgia, "Times New Roman", serif;
          }

          40% {
            font-family: "Courier New", Courier, monospace;
          }

          60% {
            font-family: "Arial Black", Arial, sans-serif;
          }

          80% {
            font-family: "Trebuchet MS", Arial, sans-serif;
          }

          100% {
            font-family: Impact, Haettenschweiler, "Arial Narrow Bold", sans-serif;
          }
        }



        /*
         * ==========================================
         * MAIN ECHO GLITCH
         * ==========================================
         */

        .atmosphere-glitch {
          animation: atmosphere-glitch-main 7s infinite;
        }

        .atmosphere-glitch::before,
        .atmosphere-glitch::after {
          content: attr(data-text);

          position: absolute;

          inset: 0;

          pointer-events: none;

          opacity: 0;
        }

        .atmosphere-glitch::before {
          color: #ffffff;

          transform: translateX(-4px);

          clip-path:
            polygon(
              0 20%,
              100% 20%,
              100% 42%,
              0 42%
            );

          animation:
            atmosphere-glitch-before
            7s infinite;
        }

        .atmosphere-glitch::after {
          color: #1d4ed8;

          transform: translateX(4px);

          clip-path:
            polygon(
              0 58%,
              100% 58%,
              100% 78%,
              0 78%
            );

          animation:
            atmosphere-glitch-after
            7s infinite;
        }


        /*
         * Random-ish main glitch
         */

        @keyframes atmosphere-glitch-main {

          0%,
          88%,
          100% {
            transform: translate(0);
          }

          89% {
            transform: translate(-3px, 1px);
          }

          90% {
            transform: translate(3px, -1px);
          }

          91% {
            transform: translate(-1px, 0);
          }

          92% {
            transform: translate(0);
          }
        }


        /*
         * Upper sliced glitch
         */

        @keyframes atmosphere-glitch-before {

          0%,
          87%,
          93%,
          100% {
            opacity: 0;
          }

          88% {
            opacity: 0.7;
            transform: translateX(-6px);
          }

          89% {
            opacity: 0.3;
            transform: translateX(5px);
          }

          90% {
            opacity: 0.7;
            transform: translateX(-3px);
          }

          92% {
            opacity: 0;
          }
        }


        /*
         * Lower sliced glitch
         */

        @keyframes atmosphere-glitch-after {

          0%,
          88%,
          94%,
          100% {
            opacity: 0;
          }

          89% {
            opacity: 0.5;
            transform: translateX(7px);
          }

          91% {
            opacity: 0.8;
            transform: translateX(-5px);
          }

          93% {
            opacity: 0;
          }
        }


        /*
         * ==========================================
         * GLITCH BLOCKS
         * ==========================================
         */

        .atmosphere-glitch-block {
          animation:
            atmosphere-block-glitch
            5s steps(1) infinite;
        }

        .atmosphere-glitch-block-secondary {
          animation:
            atmosphere-block-glitch-two
            6s steps(1) infinite;
        }

        @keyframes atmosphere-block-glitch {

          0%,
          80%,
          100% {
            opacity: 0;
            transform: translateX(0);
          }

          82% {
            opacity: 0.8;
            transform: translateX(-20px);
          }

          84% {
            opacity: 0.3;
            transform: translateX(15px);
          }

          86% {
            opacity: 0;
          }
        }

        @keyframes atmosphere-block-glitch-two {

          0%,
          72%,
          100% {
            opacity: 0;
          }

          74% {
            opacity: 0.5;
            transform: translateX(30px);
          }

          76% {
            opacity: 0.2;
            transform: translateX(-10px);
          }

          78% {
            opacity: 0;
          }
        }


        /*
         * ==========================================
         * VERTICAL SCANNER
         * ==========================================
         */

        .atmosphere-scan {
          animation:
            atmosphere-scan-animation
            9s linear infinite;
        }

        @keyframes atmosphere-scan-animation {

          0% {
            left: -5%;
            opacity: 0;
          }

          10% {
            opacity: 0.4;
          }

          90% {
            opacity: 0.4;
          }

          100% {
            left: 105%;
            opacity: 0;
          }
        }


        /*
         * ==========================================
         * HORIZONTAL SCANNER
         * ==========================================
         */

        .atmosphere-scan-horizontal {
          animation:
            atmosphere-horizontal-animation
            11s linear infinite;
        }

        @keyframes atmosphere-horizontal-animation {

          0% {
            top: -10%;
            opacity: 0;
          }

          10% {
            opacity: 0.3;
          }

          90% {
            opacity: 0.3;
          }

          100% {
            top: 110%;
            opacity: 0;
          }
        }


        /*
         * ==========================================
         * BOTTOM TICKER
         * ==========================================
         */

        .atmosphere-ticker {
          animation:
            atmosphere-ticker-animation
            35s linear infinite;
        }

        @keyframes atmosphere-ticker-animation {

          from {
            transform: translateX(0);
          }

          to {
            transform: translateX(-50%);
          }
        }

        /*
         * ==========================================
         * RESONANCE WAVEFORM — draws in once, then
         * breathes very slightly. Not a loop of the
         * draw itself, just a settled pulse.
         * ==========================================
         */

        .atmosphere-waveform-path {
          stroke-dasharray: 1;
          stroke-dashoffset: 1;
          opacity: 0;
          animation:
            waveform-draw 2.6s cubic-bezier(0.16, 1, 0.3, 1) 900ms forwards,
            waveform-breathe 7s ease-in-out 3.6s infinite;
        }

        @keyframes waveform-draw {
          0% {
            stroke-dashoffset: 1;
            opacity: 0;
          }
          15% {
            opacity: 0.55;
          }
          100% {
            stroke-dashoffset: 0;
            opacity: 0.4;
          }
        }

        @keyframes waveform-breathe {
          0%, 100% {
            opacity: 0.32;
          }
          50% {
            opacity: 0.5;
          }
        }

        /*
         * ==========================================
         * PING RINGS — single burst on load
         * ==========================================
         */

        .atmosphere-ping {
          width: 10px;
          height: 10px;
          transform: translate(-50%, -50%);
          animation: atmosphere-ping-expand 2.6s cubic-bezier(0.16, 1, 0.3, 1) forwards;
        }

        @keyframes atmosphere-ping-expand {
          0% {
            width: 10px;
            height: 10px;
            opacity: 0.65;
          }
          100% {
            width: 960px;
            height: 960px;
            opacity: 0;
          }
        }


        /*
         * ==========================================
         * REDUCED MOTION ACCESSIBILITY
         * ==========================================
         */

        @media (prefers-reduced-motion: reduce) {

          .echo-font-cycle,
          .atmosphere-glitch,
          .atmosphere-glitch::before,
          .atmosphere-glitch::after,
          .atmosphere-glitch-block,
          .atmosphere-glitch-block-secondary,
          .atmosphere-scan,
          .atmosphere-scan-horizontal,
          .atmosphere-ticker,
          .atmosphere-waveform-path,
          .atmosphere-ping,
          .tile-flare,
          .resonance-tile-inner {
            animation: none !important;
          }

          .atmosphere-waveform-path {
            stroke-dashoffset: 0;
            opacity: 0.35;
          }

          .atmosphere-ping {
            display: none;
          }
        }
      `}</style>
      
    </DossierSection>
  );
}


/* ==============================================================
   METRIC COMPONENT
================================================================ */

function Metric({
  label,
  value,
  border = false,
}: {
  label: string;
  value: string;
  border?: boolean;
}) {
  return (
    <div
      className={`
        text-center
        ${border ? 'border-x border-white/[0.07]' : ''}
      `}
    >
      <div
        className="
          font-mono
          text-[7px]
          uppercase
          tracking-[0.3em]
          text-white/20
        "
      >
        {label}
      </div>

      <div
        className="
          mt-2
          font-mono
          text-[10px]
          tracking-[0.2em]
          text-white/50
        "
      >
        {value}
      </div>
    </div>
  );
}