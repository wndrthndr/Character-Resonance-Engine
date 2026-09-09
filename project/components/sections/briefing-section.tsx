'use client';

import { useEffect, useState } from 'react';
import { motion } from 'framer-motion';
import { useRouter } from 'next/navigation';
import { DossierSection } from '@/components/dossier-section';

const universes = [
  { id: '01', title: 'MARVEL', value: 'marvel', color: '#ff5545' },
  { id: '02', title: 'Kung Fu PANDA', value: 'kung_fu_panda', color: '#eab308' },
  { id: '03', title: 'AVATAR:The last airbender', value: 'atla', color: '#6493c4' },
  { id: '04', title: 'DC', value: 'dc', color: '#ffffff' },
];
interface UniverseSectionProps {
  onSelectFranchise: (selectedFranchise: string) => void;
}

export function UniverseSection({
  onSelectFranchise,
}: UniverseSectionProps) {
  const router = useRouter();
  const [hoveredColor, setHoveredColor] = useState('#3b82f6');
  const [selected, setSelected] = useState<string | null>(null);

  // Navigate after the flare plays, and clean the timer up if the
  // component unmounts early (fast nav elsewhere, hot reload, etc.)
  useEffect(() => {
    if (!selected) return;
    const timer = setTimeout(() => {
      router.push(`/quiz?franchise=${selected}`);
    }, 500);
    return () => clearTimeout(timer);
  }, [selected, router]);

  const handleSelect = (value: string) => {
    if (selected) return;
  
    setSelected(value);
    onSelectFranchise(value);
  };

  return (
    <DossierSection index={1} label="02 / SELECTION" fileId="AX-GATE" >

      {/* Dynamic Ambient Light Layer */}
      <motion.div
        animate={{ backgroundColor: `${hoveredColor}12` }}
        transition={{ duration: 0.7, ease: 'easeOut' }}
        className="absolute inset-0 z-0"
      />

      <div className="relative z-10 flex h-full w-full flex-col p-8 md:p-16">

        {/* Header Lockup */}
        <div className="mb-10 border-b-[5px] border-white pb-6">
          <h2
            className="
              animate-rgb-wave
              font-orbitron
              font-bold
              uppercase
              leading-[0.9]
              tracking-tighter
              text-transparent
              bg-clip-text
              bg-gradient-to-r
              from-[#3b82f6]
              via-[#a855f7]
              via-[#eab308]
              to-[#3b82f6]
            "
            style={{ fontSize: 'clamp(2.5rem, 7vw, 7rem)' }}
          >
            Select your<br />
            <span className="opacity-50">Resonance point</span>
          </h2>
        </div>

        {/* Grid of Universes - brutalist bordered blocks */}
        <div className="grid h-full w-full grid-cols-2 gap-4 md:grid-cols-4">
          {universes.map((u) => {
            const isSelected = selected === u.value;
            const isDimmed = selected !== null && !isSelected;

            return (
              <motion.button
                key={u.id}
                type="button"
                aria-label={`Choose ${u.title}`}
                aria-pressed={isSelected}
                disabled={selected !== null}
                onClick={() => handleSelect(u.value)}
                onMouseEnter={() => setHoveredColor(u.color)}
                onFocus={() => setHoveredColor(u.color)}
                whileHover={selected ? undefined : { x: -4, y: -4 }}
                whileTap={selected ? undefined : { x: 0, y: 0 }}
                animate={
                  isSelected
                    ? {
                        scale: [1, 1.04, 0.98],
                        boxShadow: [
                          `8px 8px 0 0 ${u.color}`,
                          `0 0 40px 8px ${u.color}`,
                          `0 0 0 0 ${u.color}00`,
                        ],
                      }
                    : { opacity: isDimmed ? 0.25 : 1 }
                }
                transition={
                  isSelected
                    ? { duration: 0.5, ease: 'easeOut' }
                    : { duration: 0.4, ease: 'easeOut' }
                }
                style={{ boxShadow: `8px 8px 0 0 ${u.color}` }}
                className="
                  group relative flex flex-col justify-between
                  border-[4px] border-white bg-black
                  p-6 text-left md:p-8
                  focus-visible:outline focus-visible:outline-2
                  focus-visible:outline-offset-4 focus-visible:outline-white
                  disabled:cursor-default
                "
              >
                <span className="w-fit border border-white/30 px-2 py-0.5 font-mono text-[10px] text-white/50">
                  ID_{u.id}
                </span>

                <h3 className="font-display text-3xl font-black uppercase text-white md:text-4xl">
                  {u.title}
                </h3>

                {/* Selection Bar */}
                <div className="h-2 w-full" style={{ backgroundColor: u.color }} />
              </motion.button>
            );
          })}
        </div>
      </div>
    </DossierSection>
  );
}