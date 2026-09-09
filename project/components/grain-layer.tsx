'use client';

import { useEffect, useRef } from 'react';

/**
 * Animated film-grain + vignette overlay. Sits above section backgrounds
 * but below HUD. Uses a pre-baked SVG noise tile that drifts via keyframes.
 */
export function GrainLayer({ tone = 'paper' }: { tone?: 'paper' | 'ink' }) {
  const ref = useRef<HTMLDivElement>(null);
  useEffect(() => {
    // subtle opacity breathing
    const el = ref.current;
    if (!el) return;
    let raf = 0;
    let t = 0;
    const tick = () => {
      t += 0.012;
      el.style.opacity = String(0.02 + Math.sin(t) * 0.02);
      raf = requestAnimationFrame(tick);
    };
    raf = requestAnimationFrame(tick);
    return () => cancelAnimationFrame(raf);
  }, []);

  return (
    <>
      <div
        ref={ref}
        className="pointer-events-none absolute inset-0 z-30 grain-overlay animate-grain"
        aria-hidden
      />
      <div
  className="pointer-events-none absolute inset-0 z-30"
  style={{
    background: tone === 'ink' 
      ? 'radial-gradient(circle, transparent 40%, rgba(0,0,0,0.8) 150%)' 
      : 'radial-gradient(circle, transparent 40%, rgba(245,245,220,0.8) 150%)'
  }}
  aria-hidden
/>
    </>
  );
}
