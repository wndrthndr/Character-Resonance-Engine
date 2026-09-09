'use client';

import {
  useEffect,
  useMemo,
  useRef,
  useState,
} from 'react';

import {
  AnimatePresence,
  motion,
} from 'framer-motion';

import {
  DossierSection,
} from '@/components/dossier-section';

type Character = {
  name: string;
  tagline?: string;
  desc?: string;
  franchise?: string;
  image?: string;
  traits?: string[];

  geometry?: {
    color?: string;
  };

  trait_vector?: number[];
};

export function CharacterIndexSection() {
  const gridContainerRef = useRef<HTMLDivElement>(null);

  const [characters, setCharacters] = useState<Character[]>([]);
  const [selected, setSelected] = useState<Character | null>(null);
  const [activeFranchise, setActiveFranchise] = useState('all');
  const [search, setSearch] = useState('');
  const [debouncedSearch, setDebouncedSearch] = useState('');
  const [loading, setLoading] = useState(true);

  // Debounce search input
  useEffect(() => {
    const timer = setTimeout(() => {
      setDebouncedSearch(search);
    }, 250);
    return () => clearTimeout(timer);
  }, [search]);

  // Fetch Characters
  useEffect(() => {
    async function loadCharacters() {
      try {
        setLoading(true);
        const response = await fetch(`http://127.0.0.1:8000/api/characters/`);
        if (!response.ok) throw new Error('Registry request failed');

        const data = await response.json();
        setCharacters(data);
        if (data.length) setSelected(data[0]);
      } catch (error) {
        console.error('Registry error:', error);
      } finally {
        setLoading(false);
      }
    }
    loadCharacters();
  }, []);

  const franchises = useMemo(() => {
    const unique = Array.from(
      new Set(characters.map((char) => char.franchise).filter(Boolean))
    ) as string[];

    return ['all', ...unique];
  }, [characters]);

  // Filter Logic
// Filter Logic (with automatic shuffle for 'all')
const filteredCharacters = useMemo(() => {
  const query = debouncedSearch.trim().toLowerCase();

  const matched = characters.filter((character) => {
    const franchiseMatch =
      activeFranchise === 'all' || character.franchise === activeFranchise;

    if (!franchiseMatch) return false;
    if (!query) return true;

    const nameMatch = character.name.toLowerCase().includes(query);
    const taglineMatch = character.tagline?.toLowerCase().includes(query) ?? false;
    const descMatch = character.desc?.toLowerCase().includes(query) ?? false;
    const franchiseTextMatch = character.franchise?.toLowerCase().includes(query) ?? false;
    const traitMatch = character.traits?.some((t) => t.toLowerCase().includes(query)) ?? false;

    return nameMatch || taglineMatch || descMatch || franchiseTextMatch || traitMatch;
  });

  // Shuffle only when 'all' is selected and there's no active search query
  if (activeFranchise === 'all' && !query) {
    const shuffled = [...matched];
    for (let i = shuffled.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [shuffled[i], shuffled[j]] = [shuffled[j], shuffled[i]];
    }
    return shuffled;
  }

  return matched;
}, [characters, activeFranchise, debouncedSearch]);

  // RESET SCROLL ONLY ON SEARCH OR FRANCHISE CHANGE
  useEffect(() => {
    if (gridContainerRef.current) {
      gridContainerRef.current.scrollTop = 0;
    }
  }, [activeFranchise, debouncedSearch]);

  // FALLBACK SELECTION HANDLING (Does not jump page scroll on selection)
  useEffect(() => {
    if (filteredCharacters.length === 0) {
      setSelected(null);
      return;
    }

    const stillExists = filteredCharacters.some(
      (character) => character.name === selected?.name
    );

    if (!stillExists) {
      setSelected(filteredCharacters[0]);
    }
  }, [filteredCharacters]);

  // DIRECT ACCENT VALUE (No grey/black/luminance override)
  const accent = selected?.geometry?.color || '#3b82f6';

  return (
    <DossierSection
      index={3}
      label="04 / REGISTRY_GRID"
      fileId="AX-9999"

    >
      <div className="pointer-events-none absolute inset-0 z-0 bg-[linear-gradient(to_right,#3b82f6_1px,transparent_1px),linear-gradient(to_bottom,#3b82f6_1px,transparent_1px)] bg-[size:64px_64px] opacity-[0.025]" />

      <motion.div
        animate={{ backgroundColor: `${accent}0a` }}
        transition={{ duration: 0.7 }}
        className="pointer-events-none absolute inset-0 z-0"
      />

      <div className="relative z-10 flex h-full gap-8 p-8 pt-16 md:p-12 md:pt-20">
        
        {/* LEFT CHARACTER POSTER */}
        <aside className="relative w-[300px] shrink-0 overflow-hidden border-r border-white/10 md:w-[350px]">
          <AnimatePresence mode="wait">
            {selected && (
              <motion.div
                key={selected.name}
                initial={{ opacity: 0 }}
                animate={{ opacity: 1 }}
                exit={{ opacity: 0 }}
                transition={{ duration: 0.45 }}
                className="absolute inset-0 flex flex-col justify-between p-6"
              >
                {/* BACKGROUND IMAGE WITH ENTRANCE ANIMATION */}
                {selected.image ? (
                  <motion.img
                    key={selected.name}
                    src={selected.image}
                    initial={{ scale: 1.3, opacity: 0, filter: 'brightness(3) contrast(1.5)' }}
                    animate={{ scale: 1, opacity: 1, filter: 'brightness(1) contrast(1)' }}
                    transition={{ duration: 0.35, ease: 'easeOut' }}
                    className="absolute inset-0 h-full w-full object-cover"
                  />
                ) : (
                  <div className="absolute inset-0 bg-white/[0.025]">
                    <div className="font-mono absolute left-1/2 top-1/2 -translate-x-1/2 -translate-y-1/2 text-[10px] uppercase tracking-[0.3em] text-white/20">
                      Image Pending
                    </div>
                  </div>
                )}

                <div className="pointer-events-none absolute inset-0 bg-gradient-to-b from-black/40 via-black/20 to-black" />
                <div className="pointer-events-none absolute inset-x-0 bottom-0 h-[75%] bg-gradient-to-t from-[#070809] via-[#070809]/90 to-transparent" />

                {/* TOP TACTICAL BADGE */}
                <div className="relative z-20 flex items-center justify-between">
                  <div className="flex items-center gap-2">
                    <span className="relative flex h-2 w-2">
                      <span
                        className="absolute h-full w-full animate-ping rounded-full"
                        style={{ backgroundColor: accent }}
                      />
                      <span
                        className="relative h-2 w-2 rounded-full"
                        style={{ backgroundColor: accent }}
                      />
                    </span>
                    <span className="font-mono text-[9px] font-semibold uppercase tracking-[0.3em] text-white/80">
                      Active Profile
                    </span>
                  </div>
                  
                </div>

                {/* BOTTOM CHARACTER INFO */}
                <motion.div
                  initial={{ opacity: 0, y: 30 }}
                  animate={{ opacity: 1, y: 0 }}
                  transition={{ delay: 0.15, duration: 0.5 }}
                  className="relative z-20 mt-auto pt-10"
                >
                  <div
                    className="font-mono mb-2 text-[10px] font-bold uppercase tracking-[0.3em]"
                    style={{ color: accent }}
                  >
                    {formatFranchise(selected.franchise || 'unknown')}
                  </div>

                  <h2 className="font-display text-4xl font-black uppercase leading-[0.9] tracking-tight text-white md:text-5xl">
                    {selected.name}
                  </h2>

                  <motion.div
                    initial={{ width: 0 }}
                    animate={{ width: 60 }}
                    transition={{ delay: 0.3, duration: 0.5 }}
                    className="my-3 h-[3px]"
                    style={{ backgroundColor: accent }}
                  />

                  {/* TAGLINE & DESCRIPTION GRID BLOCK */}
          <div className="space-y-2">
            {selected.tagline && (
              <div className="inline-block rounded-xs border border-white/10 bg-white/5 px-2 py-0.5 backdrop-blur-xs">
                <p className="font-mono text-[9px] font-semibold uppercase tracking-[0.2em] text-white/90">
                  {selected.tagline}
                </p>
              </div>
            )}

            {selected.desc && (
              <div className="relative border-l-2 pl-3 py-1" style={{ borderColor: `${accent}aa` }}>
                <p className="font-mono max-w-[280px] text-[11px] leading-relaxed tracking-wide text-white/80">
                  {selected.desc}
                </p>
              </div>
            )}
          </div>


                  {/* VECTOR SIGNAL VISUALIZER */}
                  {selected.trait_vector && selected.trait_vector.length > 0 && (
                    <div className="mt-5 rounded-sm border border-white/10 bg-black/40 p-3 backdrop-blur-xs">
                      <div className="mb-2 flex items-center justify-between">
                        <span
                          className="font-mono text-[8px] font-bold tracking-widest"
                          style={{ color: accent }}
                        >
                          SYNCED
                        </span>
                      </div>
                      <div className="flex h-8 items-end gap-1">
                        {selected.trait_vector.map((val, idx) => (
                          <div
                            key={idx}
                            className="flex-1 rounded-t-xs bg-white/10 transition-all duration-500"
                            style={{
                              height: `${Math.max(15, Math.min(100, val * 100))}%`,
                              backgroundColor: idx % 2 === 0 ? accent : `${accent}88`,
                            }}
                          />
                        ))}
                      </div>
                    </div>
                  )}
                </motion.div>
              </motion.div>
            )}
          </AnimatePresence>
        </aside>

        {/* RIGHT SIDE */}
        <section className="flex min-w-0 flex-1 flex-col">
          {/* FILTER BAR */}
          <div className="mb-5 flex shrink-0 items-center gap-4 border-b border-white/10 pb-4">
            <div className="flex min-w-0 flex-1 items-center gap-2 overflow-x-auto">
              {franchises.map((franchise) => {
                const active = activeFranchise === franchise;

                return (
                  <button
                    key={franchise}
                    onClick={() => setActiveFranchise(franchise)}
                    className={`font-mono relative shrink-0 border px-4 py-2 text-[10px] font-semibold uppercase tracking-[0.2em] transition-all ${
                      active
                        ? 'border-[#3b82f6] bg-[#3b82f6]/10 text-[#3b82f6]'
                        : 'border-white/10 text-white/70 hover:border-white/30 hover:text-white'
                    }`}
                  >
                    {formatFranchise(franchise)}
                    {active && (
                      <motion.span
                        layoutId="active-filter"
                        className="absolute bottom-[-1px] left-0 h-[2px] w-full bg-[#3b82f6]"
                      />
                    )}
                  </button>
                );
              })}
            </div>

            {/* SEARCH FIELD */}
            <div className="flex w-[240px] shrink-0 items-center border border-white/10 bg-black/40 focus-within:border-[#3b82f6]">
              <span className="font-mono pl-3 text-[#3b82f6]">/</span>
              <input
                value={search}
                onChange={(e) => setSearch(e.target.value)}
                onKeyDown={(e) => {
                  if (e.key === 'Escape') setSearch('');
                }}
                placeholder="SEARCH NAME, TRAIT..."
                className="font-mono w-full bg-transparent px-3 py-2 text-[10px] uppercase tracking-[0.15em] text-white outline-none placeholder:text-white/30"
              />
              {search && (
                <button
                  onClick={() => setSearch('')}
                  className="font-mono pr-3 text-[11px] text-white/40 hover:text-white"
                >
                  ✕
                </button>
              )}
            </div>
          </div>

          {/* METADATA INFO */}
          <div className="font-mono mb-3 flex items-center justify-between text-[8px] uppercase tracking-[0.25em] text-white/40">
            <span>Displaying // {filteredCharacters.length}</span>
            <span>Filter // {formatFranchise(activeFranchise)}</span>
          </div>

          {/* GRID */}
          <div
            ref={gridContainerRef}
            className="thin-scroll min-h-0 flex-1 overflow-y-auto pr-2"
          >
            {loading ? (
              <div className="font-mono flex h-full items-center justify-center text-[10px] uppercase tracking-[0.3em] text-white/30">
                Loading Registry...
              </div>
            ) : filteredCharacters.length === 0 ? (
              <div className="font-mono flex h-full flex-col items-center justify-center gap-2 text-white/30">
                <span className="text-[12px] uppercase tracking-[0.2em]">
                  No Matching Records Found
                </span>
                <button
                  onClick={() => {
                    setSearch('');
                    setActiveFranchise('all');
                  }}
                  className="border border-white/20 bg-white/5 px-3 py-1 text-[9px] uppercase tracking-[0.15em] text-white hover:bg-white/10"
                >
                  Reset Filters
                </button>
              </div>
            ) : (
              <motion.div layout className="grid grid-cols-2 gap-4 md:grid-cols-3 lg:grid-cols-4 xl:grid-cols-5">
                <AnimatePresence mode="popLayout">
                  {filteredCharacters.map((character) => {
                    const isActive = selected?.name === character.name;
                    const cardAccent = character.geometry?.color || '#3b82f6';

                    return (
                      <motion.button
                        layout
                        key={`${character.franchise}-${character.name}`}
                        initial={{ opacity: 0, y: 15 }}
                        animate={{ opacity: 1, y: 0 }}
                        exit={{ opacity: 0, scale: 0.95 }}
                        whileHover={{ y: -3 }}
                        whileTap={{ scale: 0.97 }}
                        onClick={() => setSelected(character)}
                        className={`group relative aspect-[3/4] overflow-hidden border text-left bg-black ${
                          isActive ? 'border-white' : 'border-white/10 hover:border-white/40'
                        }`}
                      >
                        <div className="absolute inset-x-0 top-0 h-[75%] overflow-hidden bg-white/[0.02]">
                          {character.image ? (
                            <img
                              src={character.image}
                              alt={character.name}
                              className="h-full w-full object-cover object-top opacity-80 transition-all duration-500 group-hover:scale-105 group-hover:opacity-100"
                            />
                          ) : (
                            <div className="font-mono flex h-full items-center justify-center text-[8px] uppercase tracking-[0.2em] text-white/20">
                              Image Pending
                            </div>
                          )}
                          <div className="absolute inset-0 bg-gradient-to-t from-[#070809] via-transparent to-transparent" />
                        </div>

                        <div className="absolute inset-x-0 bottom-0 z-10 p-3">
                          <div className="font-mono mb-1 text-[7px] uppercase tracking-[0.2em] text-white/40">
                            {formatFranchise(character.franchise || 'unknown')}
                          </div>
                          <h3 className="font-display text-lg font-black uppercase leading-tight text-white">
                            {character.name}
                          </h3>

                          <motion.div
                            className="mt-2 h-[2px]"
                            animate={{ width: isActive ? '100%' : '30%' }}
                            style={{ backgroundColor: cardAccent }}
                          />
                        </div>

                        {isActive && (
                          <motion.div
                            layoutId="active-character"
                            className="absolute right-3 top-3 z-20 h-2 w-2"
                            style={{ backgroundColor: cardAccent }}
                          />
                        )}
                      </motion.button>
                    );
                  })}
                </AnimatePresence>
              </motion.div>
            )}
          </div>
        </section>
      </div>
    </DossierSection>
  );
}

function formatFranchise(franchise: string) {
  if (franchise === 'all') return 'All';
  return franchise
    .replace(/_/g, ' ')
    .replace(/\b\w/g, (letter) => letter.toUpperCase());
}