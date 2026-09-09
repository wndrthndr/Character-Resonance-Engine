'use client';

import { useState } from 'react'; // Remove this if not used
import { useArchive } from '@/components/pinned-scroll'; 

export function HudOverlay() {
  const context = useArchive();
  
  // 1. Fallback to a default state if context or progress is undefined
  const { progress } = context || {};
  const { progress: p, activeIndex, total } = progress || { 
    progress: 0, 
    activeIndex: 0, 
    total: 0 
  };

  return (
    <div className="pointer-events-none fixed inset-0 z-50 mix-blend-difference">
      {/* Corner ticks */}
      <Corner className="left-6 top-6" />
      <Corner className="right-6 top-6 rotate-90" />
      <Corner className="left-6 bottom-6 -rotate-90" />
      <Corner className="right-6 bottom-6 rotate-180" />

      {/* Top bar — archive id + classification */}
      <div className="absolute left-1/2 top-6 flex -translate-x-1/2 items-center gap-4 font-mono text-[10px] uppercase tracking-wide-dossier text-paper">
        <span className="h-px w-8 bg-paper/50" />
        <span>DIGITAL ARCHIVE / AX-SERIES</span>
        <span className="h-1.5 w-1.5 bg-signal animate-pulse-slow" />
        <span>CLASSIFIED · TIER V</span>
        <span className="h-px w-8 bg-paper/50" />
      </div>

      {/* Bottom bar — sequence index + progress meter */}
      <div className="absolute bottom-6 left-1/2 flex -translate-x-1/2 items-center gap-6 font-mono text-[10px] uppercase tracking-wide-dossier text-paper">
        <span>SEQ</span>
        <div className="flex items-center gap-2">
          {Array.from({ length: total }).map((_, i) => (
            <span
              key={i}
              className={`h-2 w-2 transition-all duration-300 ${
                i === activeIndex
                  ? 'w-8 bg-signal'
                  : i < activeIndex
                  ? 'bg-paper/80'
                  : 'bg-paper/25'
              }`}
            />
          ))}
        </div>
        <span className="tabular-nums">
          {String(activeIndex + 1).padStart(2, '0')}
          <span className="text-paper/40"> / {String(total).padStart(2, '0')}</span>
        </span>
        <span className="h-px w-10 bg-paper/30" />
        <span className="tabular-nums">{Math.round(p * 100)}%</span>
      </div>
    </div>
  );
}

function Corner({ className = '' }: { className?: string }) {
  return (
    <div className={`absolute ${className}`}>
      <div className="h-3 w-3 border-l border-t border-paper/70" />
    </div>
  );
}