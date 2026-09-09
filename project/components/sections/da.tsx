'use client';

import { useEffect, useRef, useState } from 'react';
import { DossierSection } from '@/components/dossier-section';

/* ==================================================================
   MAGNETIC CTA
   Wraps a button so it gently "pulls" toward the cursor on hover and
   springs back on release. Behavior of onClick is untouched — this
   only adds a transform layer around the exact same button markup.
================================================================== */

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

export function AtmosphereSection() {
  const [mounted, setMounted] = useState(false);
  const word = 'ECHO'.split('');
  const [mouse, setMouse] = useState({ x: 0, y: 0 });
  const [scrollY, setScrollY] = useState(0);
  const [reducedMotion, setReducedMotion] = useState(false);

  useEffect(() => {
    const mq = window.matchMedia('(prefers-reduced-motion: reduce)');
    setReducedMotion(mq.matches);
    const handler = () => setReducedMotion(mq.matches);
    mq.addEventListener('change', handler);
    return () => mq.removeEventListener('change', handler);
  }, []);

  useEffect(() => {
    const handleMove = (e: MouseEvent) => {
      const x = (e.clientX / window.innerWidth - 0.5) * 2;
      const y = (e.clientY / window.innerHeight - 0.5) * 2;
      setMouse({ x, y });
    };

    window.addEventListener('mousemove', handleMove);
    return () => window.removeEventListener('mousemove', handleMove);
  }, []);

  useEffect(() => {
    let raf = 0;
    const onScroll = () => {
      cancelAnimationFrame(raf);
      raf = requestAnimationFrame(() => setScrollY(window.scrollY));
    };
    window.addEventListener('scroll', onScroll, { passive: true });
    return () => {
      window.removeEventListener('scroll', onScroll);
      cancelAnimationFrame(raf);
    };
  }, []);

  const handleBegin = () => {
    window.scrollTo({
      top: window.innerHeight * 2,
      behavior: 'smooth',
    });
  };
  const handleChar = () => {
    window.scrollTo({
      top: window.innerHeight * 3,
      behavior: 'smooth',
    });
  };

  useEffect(() => {
    const timer = setTimeout(() => {
      setMounted(true);
    }, 100);

    return () => clearTimeout(timer);
  }, []);

  const mx = reducedMotion ? 0 : mouse.x;
  const my = reducedMotion ? 0 : mouse.y;
  const sy = reducedMotion ? 0 : scrollY;

  // Scroll-driven recede: the hero text quietly lifts and dims as the
  // reader scrolls away, foreshadowing the "Begin Session" transition.
  const scrollProgress = Math.min(sy / (typeof window !== 'undefined' ? window.innerHeight * 0.9 : 900), 1);
  const heroFadeStyle: React.CSSProperties = {
    opacity: 1 - scrollProgress * 0.55,
    transform: `translateY(${scrollProgress * -34}px) scale(${1 - scrollProgress * 0.04})`,
    transition: 'opacity 120ms linear, transform 120ms linear',
  };

  return (
    <DossierSection
      index={0}
      label="01 / FRAGMENT"
      fileId="SIG-7792"
      className="bg-black text-white"
    >
      {/* =========================================================
          BACKGROUND
      ========================================================= */}

      <div className="pointer-events-none absolute inset-0 z-0 overflow-hidden ">

        {/* Grid */}
        <div
          className="
            absolute inset-0
            opacity-[0.035]
            [background-size:64px_64px]
            bg-black/[0.02]
          "
          style={{
            transform: `translate3d(${mx * -4}px, ${my * -4 + sy * 0.02}px, 0)`,
            transition: 'transform 900ms cubic-bezier(0.16,1,0.3,1)',
          }}
        />

        {/* Film grain — adds a quiet, premium texture without touching palette */}
        <svg
          className="absolute inset-0 h-full w-full opacity-[0.03]"
          xmlns="http://www.w3.org/2000/svg"
        >
          <filter id="atmosphere-grain">
            <feTurbulence type="fractalNoise" baseFrequency="0.85" numOctaves="2" stitchTiles="stitch" />
          </filter>
          <rect width="100%" height="100%" filter="url(#atmosphere-grain)" />
        </svg>

        {/* Large background word — slowest parallax layer, furthest back */}
        <div
          className={`
            absolute
            left-1/2 top-1/2
            -translate-x-1/2
            -translate-y-1/2
            select-none
            whitespace-nowrap
            font-sans
            text-[28vw]
            font-black
            uppercase
            leading-none
            tracking-[-0.09em]
            text-white/[0.3]
            transition-all
            duration-[1800ms]
            z-10
            ${
              mounted
                ? 'scale-100 opacity-10'
                : 'scale-110 opacity-0'
            }
          `}
        >
          {word.map((char, i) => (
      <span key={i} className="glitch-letter">
        {char}
      </span>
    ))}
        </div>
        {/* Blue ambient light — mid-depth parallax layer */}
        <div
          className="
            absolute
            left-1/2 top-1/2
            h-[500px] w-[800px]
            -translate-x-1/2
            -translate-y-1/2
            rounded-full
            bg-[#3b82f6]/[0.045]
            blur-[160px]
          "
          style={{
            transform: `translate3d(calc(-50% + ${mx * 18}px), calc(-50% + ${my * 18 + sy * 0.1}px), 0)`,
            transition: 'transform 700ms cubic-bezier(0.16,1,0.3,1)',
          }}
        />

        {/* Cursor spotlight — a soft light that follows the reader */}
        <div
          className="absolute inset-0"
          style={{
            background: `radial-gradient(560px circle at ${50 + mx * 42}% ${50 + my * 42}%, rgba(59,130,246,0.07), transparent 72%)`,
            opacity: mounted ? 1 : 0,
            transition: 'opacity 900ms ease, background 300ms linear',
          }}
        />

        {/* Reticle — thin cursor-tracking crosshair, ties to "Trace the Echo" */}
        <div
          className="hidden lg:block"
          style={{ opacity: mounted ? 0.55 : 0, transition: 'opacity 900ms ease' }}
        >
          <div
            className="absolute top-0 bottom-0 w-px bg-gradient-to-b from-transparent via-[#3b82f6]/25 to-transparent"
            style={{ left: `${50 + mx * 42}%`, transition: 'left 500ms cubic-bezier(0.16,1,0.3,1)' }}
          />
          <div
            className="absolute left-0 right-0 h-px bg-gradient-to-r from-transparent via-[#3b82f6]/25 to-transparent"
            style={{ top: `${50 + my * 42}%`, transition: 'top 500ms cubic-bezier(0.16,1,0.3,1)' }}
          />
        </div>

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
      </div>

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
          ease-[cubic-bezier(0.16,1,0.3,1)]
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
          ease-[cubic-bezier(0.16,1,0.3,1)]
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
          relative z-20
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
              ease-[cubic-bezier(0.16,1,0.3,1)]

              ${
                mounted
                  ? 'translate-y-0 opacity-100'
                  : 'translate-y-4 opacity-0'
              }
            `}
          >
            <div className="relative">
              {/* Rotating signature ring behind the badge */}
              <div className="badge-ring pointer-events-none absolute -inset-[1px]" />

              <div
                className="
                  relative
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
          </div>

          {/* =====================================================
              HERO TYPOGRAPHY
          ===================================================== */}

          <div className="relative mx-auto text-center" style={heroFadeStyle}>

            {/* TRACE THE */}
            <div
              className={`
                relative z-10
                overflow-hidden
                transition-all
                delay-500
                duration-1000
                ease-[cubic-bezier(0.16,1,0.3,1)]

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
                transition-opacity
                delay-700
                duration-1000
                ease-[cubic-bezier(0.16,1,0.3,1)]

                ${mounted ? 'opacity-100' : 'opacity-0'}
              `}
            >
              {/* Main word */}
              <h1
                className="
                  atmosphere-glitch
                  atmosphere-float
                  relative
                  z-10
                  select-none
                  font-sans
                  text-[22vw]
                  font-black
                  uppercase
                  leading-[0.75]
                  tracking-[-0.08em]
                  text-[#3b82f6]
                  sm:text-[18vw]
                  lg:text-[13rem]
                "
                
                data-text="ECHO"
                style={{
                  transform: `
                    rotate(-2deg)
                    scale(${mounted ? 1 : 0.94})
                    translate(${mx * 14}px, ${my * 14 + sy * -0.15}px)
                  `,
                  transition: 'transform 200ms cubic-bezier(0.16,1,0.3,1)',
                }}
              >
                ECHO
              </h1>

              {/* Horizontal crossing line */}
              <div
                className="
                  absolute
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
                ease-[cubic-bezier(0.16,1,0.3,1)]

                ${
                  mounted
                    ? 'translate-y-0 opacity-100 blur-0'
                    : 'translate-y-5 opacity-0 blur-[6px]'
                }
              `}
            >
              <div className="mt-1 h-14 w-[2px] shrink-0 bg-[#3b82f6]" />

              <div>
                <div
                  className="
                    mb-2
                    font-mono
                    text-[8px]
                    uppercase
                    tracking-[0.3em]
                    text-[#3b82f6]/60
                  "
                >
                  // Directive 001
                </div>

                <p
                  className="
                    font-mono
                    text-[9px]
                    uppercase
                    leading-6
                    tracking-[0.17em]
                    text-white/35
                    md:text-[10px]
                  "
                >
                  Mapping the twelve-fold geometry of the
                  subconscious. Initiate the sequence to locate
                  the pattern hidden within your design.
                </p>
              </div>
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
          atmosphere-ticker-wrap
          pointer-events-auto
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
        style={{
          WebkitMaskImage:
            'linear-gradient(to right, transparent, black 8%, black 92%, transparent)',
          maskImage:
            'linear-gradient(to right, transparent, black 8%, black 92%, transparent)',
        }}
      >
        <div
          className="
            atmosphere-ticker
            flex
            w-max
            whitespace-nowrap
            font-mono
            text-[7px]
            uppercase
            tracking-[0.35em]
            text-white/15
          "
        >
          <span>
            RESONANCE ENGINE ONLINE &nbsp;///&nbsp;
            SIGNAL CALIBRATION PENDING &nbsp;///&nbsp;
            ARCHETYPE VECTORS 00—12 &nbsp;///&nbsp;
            PATTERN RECOGNITION ACTIVE &nbsp;///&nbsp;
            AWAITING SUBJECT INPUT &nbsp;///&nbsp;
          </span>

          <span>
            RESONANCE ENGINE ONLINE &nbsp;///&nbsp;
            SIGNAL CALIBRATION PENDING &nbsp;///&nbsp;
            ARCHETYPE VECTORS 00—12 &nbsp;///&nbsp;
            PATTERN RECOGNITION ACTIVE &nbsp;///&nbsp;
            AWAITING SUBJECT INPUT &nbsp;///&nbsp;
          </span>
        </div>
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
         * IDLE FLOAT — subtle breathing motion on ECHO
         * (layered underneath the inline parallax transform
         *  via a wrapping transform-origin trick is avoided;
         *  instead this nudges vertical position slowly so it
         *  composes naturally with the mouse/scroll offset)
         * ==========================================
         */

        .atmosphere-float {
          animation: atmosphere-float-anim 8s ease-in-out infinite;
        }

        @keyframes atmosphere-float-anim {
          0%, 100% { margin-top: 0px; }
          50% { margin-top: -6px; }
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
         * BACKGROUND WORD — per-letter idle float
         * ==========================================
         */

        .glitch-letter {
          display: inline-block;
          animation: atmosphere-letter-float 6s ease-in-out infinite;
        }

        .glitch-letter:nth-child(1) { animation-delay: 0s; }
        .glitch-letter:nth-child(2) { animation-delay: 0.4s; }
        .glitch-letter:nth-child(3) { animation-delay: 0.8s; }
        .glitch-letter:nth-child(4) { animation-delay: 1.2s; }

        @keyframes atmosphere-letter-float {
          0%, 100% { transform: translateY(0); }
          50% { transform: translateY(-6px); }
        }


        /*
         * ==========================================
         * STATUS BADGE — rotating signature ring
         * ==========================================
         */

        .badge-ring {
          background: conic-gradient(
            from 0deg,
            transparent,
            rgba(59, 130, 246, 0.55),
            transparent 30%
          );
          filter: blur(2px);
          animation: atmosphere-badge-rotate 4s linear infinite;
        }

        @keyframes atmosphere-badge-rotate {
          to { transform: rotate(360deg); }
        }


        /*
         * ==========================================
         * CTA SHEEN — diagonal light sweep on hover
         * ==========================================
         */

        .cta-sheen::before {
          content: '';
          position: absolute;
          inset: 0;
          background: linear-gradient(
            115deg,
            transparent 20%,
            rgba(59, 130, 246, 0.25) 50%,
            transparent 80%
          );
          transform: translateX(-130%);
          transition: transform 700ms cubic-bezier(0.16, 1, 0.3, 1);
          pointer-events: none;
        }

        .cta-sheen:hover::before {
          transform: translateX(130%);
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

        .atmosphere-ticker-wrap:hover .atmosphere-ticker {
          animation-play-state: paused;
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
         * REDUCED MOTION ACCESSIBILITY
         * ==========================================
         */

        @media (prefers-reduced-motion: reduce) {

          .atmosphere-glitch,
          .atmosphere-glitch::before,
          .atmosphere-glitch::after,
          .atmosphere-glitch-block,
          .atmosphere-glitch-block-secondary,
          .atmosphere-scan,
          .atmosphere-scan-horizontal,
          .atmosphere-ticker,
          .atmosphere-float,
          .glitch-letter,
          .badge-ring,
          .cta-sheen::before {
            animation: none !important;
            transition: none !important;
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