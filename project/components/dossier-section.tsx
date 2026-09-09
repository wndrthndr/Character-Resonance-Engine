'use client';

import { useEffect, useRef } from 'react';
import { useArchive } from '@/components/pinned-scroll';

type Props = {
  index: number;
  label: string;
  fileId?: string;
  children: React.ReactNode;
  className?: string;
};

export function DossierSection({
  index,
  label,
  fileId,
  children,
  className = '',
}: Props) {
  const { registerSection } = useArchive();
  const ref = useRef<HTMLElement>(null);

  useEffect(() => {
    if (!ref.current) return;

    const unreg = registerSection(ref.current);
    return unreg;
  }, [registerSection]);

  return (
    <section
      ref={ref}
      data-section={index}
      className={`archive-section relative h-screen w-screen shrink-0 overflow-hidden ${className}`}
      style={{ ['--reveal' as string]: '0' }}
    >
      <div className="pointer-events-none absolute inset-0 z-40 p-6 font-mono text-[10px] uppercase tracking-wide-dossier opacity-80">
        <div className="flex h-full flex-col justify-between">
          <div className="flex items-start justify-between">
            

            
          </div>
        </div>
      </div>

      <div
        className="relative z-20 h-full w-full bg-black"
        style={{
          transform: 'translateY(calc((1 - var(--reveal)) * 24px))',
          opacity: 0.99,
        }}
      >
        {children}
      </div>
    </section>
  );
}