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

  // --------------------------------------------------
  // DEBOUNCE SEARCH
  // --------------------------------------------------

  useEffect(() => {
    const timer = setTimeout(() => {
      setDebouncedSearch(search);
    }, 250);

    return () => clearTimeout(timer);
  }, [search]);

  // --------------------------------------------------
  // FETCH CHARACTERS
  // --------------------------------------------------

  useEffect(() => {
    async function loadCharacters() {
      try {
        setLoading(true);

        const response = await fetch(
          `${process.env.NEXT_PUBLIC_API_URL}/api/characters/`
        );

        if (!response.ok) {
          throw new Error('Registry request failed');
        }

        const data = await response.json();

        setCharacters(data);

        if (data.length) {
          setSelected(data[0]);
        }
      } catch (error) {
        console.error('Registry error:', error);
      } finally {
        setLoading(false);
      }
    }

    loadCharacters();
  }, []);

  // --------------------------------------------------
  // FRANCHISES
  // --------------------------------------------------

  const franchises = useMemo(() => {
    const unique = Array.from(
      new Set(
        characters
          .map((char) => char.franchise)
          .filter(Boolean)
      )
    ) as string[];

    return ['all', ...unique];
  }, [characters]);

  // --------------------------------------------------
  // FILTER CHARACTERS
  // --------------------------------------------------

  const filteredCharacters = useMemo(() => {
    const query = debouncedSearch.trim().toLowerCase();

    const matched = characters.filter((character) => {
      const franchiseMatch =
        activeFranchise === 'all' ||
        character.franchise === activeFranchise;

      if (!franchiseMatch) return false;

      if (!query) return true;

      const nameMatch =
        character.name.toLowerCase().includes(query);

      const taglineMatch =
        character.tagline
          ?.toLowerCase()
          .includes(query) ?? false;

      const descMatch =
        character.desc
          ?.toLowerCase()
          .includes(query) ?? false;

      const franchiseTextMatch =
        character.franchise
          ?.toLowerCase()
          .includes(query) ?? false;

      const traitMatch =
        character.traits?.some((trait) =>
          trait.toLowerCase().includes(query)
        ) ?? false;

      return (
        nameMatch ||
        taglineMatch ||
        descMatch ||
        franchiseTextMatch ||
        traitMatch
      );
    });

    // Shuffle only when showing everything
    // and there is no search.
    if (activeFranchise === 'all' && !query) {
      const shuffled = [...matched];

      for (let i = shuffled.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));

        [shuffled[i], shuffled[j]] = [
          shuffled[j],
          shuffled[i],
        ];
      }

      return shuffled;
    }

    return matched;
  }, [
    characters,
    activeFranchise,
    debouncedSearch,
  ]);

  // --------------------------------------------------
  // RESET GRID SCROLL
  // --------------------------------------------------

  useEffect(() => {
    if (gridContainerRef.current) {
      gridContainerRef.current.scrollTop = 0;
    }
  }, [activeFranchise, debouncedSearch]);

  // --------------------------------------------------
  // FALLBACK SELECTION
  // --------------------------------------------------

  useEffect(() => {
    if (filteredCharacters.length === 0) {
      setSelected(null);
      return;
    }

    const stillExists = filteredCharacters.some(
      (character) =>
        character.name === selected?.name
    );

    if (!stillExists) {
      setSelected(filteredCharacters[0]);
    }
  }, [filteredCharacters, selected?.name]);

  // --------------------------------------------------
  // ACCENT
  // --------------------------------------------------

  const accent =
    selected?.geometry?.color || '#3b82f6';

  return (
    <DossierSection
      index={3}
      label="04 / REGISTRY_GRID"
      fileId="AX-9999"
    >
      {/* ------------------------------------------------
          BACKGROUND GRID
      ------------------------------------------------ */}

      <div
        className="
          pointer-events-none
          absolute
          inset-0
          z-0
          bg-[linear-gradient(to_right,#3b82f6_1px,transparent_1px),linear-gradient(to_bottom,#3b82f6_1px,transparent_1px)]
          bg-[size:64px_64px]
          opacity-[0.025]
        "
      />

      {/* ------------------------------------------------
          ACCENT BACKGROUND
      ------------------------------------------------ */}

      <motion.div
        animate={{
          backgroundColor: `${accent}0a`,
        }}
        transition={{
          duration: 0.7,
        }}
        className="
          pointer-events-none
          absolute
          inset-0
          z-0
        "
      />

      {/* =================================================
          MAIN RESPONSIVE CONTAINER
      ================================================= */}

      <div
        className="
          relative
          z-10
          flex
          h-full
          min-h-0
          w-full
          flex-col
          gap-6
          overflow-hidden
          p-4
          pt-14

          sm:p-6
          sm:pt-16

          md:flex-row
          md:gap-8
          md:p-10
          md:pt-20

          lg:p-12
        "
      >

        {/* =================================================
            CHARACTER PROFILE / POSTER
        ================================================= */}

        <aside
          className="
            relative
            w-full
            shrink-0
            overflow-hidden

            md:w-[300px]
            md:border-r
            md:border-white/10
            md:pr-6

            lg:w-[350px]
          "
        >
          <AnimatePresence mode="wait">
            {selected && (
              <motion.div
                key={selected.name}
                initial={{
                  opacity: 0,
                }}
                animate={{
                  opacity: 1,
                }}
                exit={{
                  opacity: 0,
                }}
                transition={{
                  duration: 0.45,
                }}
                className="
                  relative
                  flex
                  min-h-0
                  w-full
                  flex-col
                  justify-between
                  overflow-hidden
                  rounded-sm
                  border
                  border-white/10

                  aspect-[4/5]

                  sm:aspect-[16/9]

                  md:absolute
                  md:inset-0
                  md:aspect-auto
                  md:rounded-none
                  md:border-0
                "
              >

                {/* =================================================
                    CHARACTER IMAGE
                ================================================= */}

                {selected.image ? (
                  <motion.img
                    key={selected.name}
                    src={selected.image}
                    alt={selected.name}
                    initial={{
                      scale: 1.3,
                      opacity: 0,
                      filter:
                        'brightness(3) contrast(1.5)',
                    }}
                    animate={{
                      scale: 1,
                      opacity: 1,
                      filter:
                        'brightness(1) contrast(1)',
                    }}
                    transition={{
                      duration: 0.35,
                      ease: 'easeOut',
                    }}
                    className="
                      absolute
                      inset-0
                      h-full
                      w-full
                      object-cover
                      object-top
                    "
                  />
                ) : (
                  <div
                    className="
                      absolute
                      inset-0
                      bg-white/[0.025]
                    "
                  >
                    <div
                      className="
                        absolute
                        left-1/2
                        top-1/2
                        -translate-x-1/2
                        -translate-y-1/2
                        whitespace-nowrap
                        font-mono
                        text-[9px]
                        uppercase
                        tracking-[0.3em]
                        text-white/20
                      "
                    >
                      Image Pending
                    </div>
                  </div>
                )}

                {/* =================================================
                    IMAGE OVERLAYS
                ================================================= */}

                <div
                  className="
                    pointer-events-none
                    absolute
                    inset-0
                    bg-gradient-to-b
                    from-black/50
                    via-black/20
                    to-black
                  "
                />

                <div
                  className="
                    pointer-events-none
                    absolute
                    inset-x-0
                    bottom-0
                    h-[80%]
                    bg-gradient-to-t
                    from-[#070809]
                    via-[#070809]/90
                    to-transparent
                  "
                />

                {/* =================================================
                    TOP BADGE
                ================================================= */}

                <div
                  className="
                    relative
                    z-20
                    flex
                    items-center
                    justify-between
                    p-4

                    sm:p-5

                    md:p-6
                  "
                >
                  <div
                    className="
                      flex
                      items-center
                      gap-2
                    "
                  >
                    <span
                      className="
                        relative
                        flex
                        h-2
                        w-2
                      "
                    >
                      <span
                        className="
                          absolute
                          h-full
                          w-full
                          animate-ping
                          rounded-full
                        "
                        style={{
                          backgroundColor: accent,
                        }}
                      />

                      <span
                        className="
                          relative
                          h-2
                          w-2
                          rounded-full
                        "
                        style={{
                          backgroundColor: accent,
                        }}
                      />
                    </span>

                    <span
                      className="
                        font-mono
                        text-[8px]
                        font-semibold
                        uppercase
                        tracking-[0.25em]
                        text-white/80

                        sm:text-[9px]
                      "
                    >
                      Active Profile
                    </span>
                  </div>
                </div>

                {/* =================================================
                    CHARACTER INFORMATION
                ================================================= */}

                <motion.div
                  initial={{
                    opacity: 0,
                    y: 30,
                  }}
                  animate={{
                    opacity: 1,
                    y: 0,
                  }}
                  transition={{
                    delay: 0.15,
                    duration: 0.5,
                  }}
                  className="
                    relative
                    z-20
                    mt-auto
                    p-4
                    pt-10

                    sm:p-5

                    md:p-6
                  "
                >
                  {/* FRANCHISE */}

                  <div
                    className="
                      mb-2
                      font-mono
                      text-[8px]
                      font-bold
                      uppercase
                      tracking-[0.25em]

                      sm:text-[10px]
                    "
                    style={{
                      color: accent,
                    }}
                  >
                    {formatFranchise(
                      selected.franchise ||
                        'unknown'
                    )}
                  </div>

                  {/* NAME */}

                  <h2
                    className="
                      font-display
                      text-3xl
                      font-black
                      uppercase
                      leading-[0.9]
                      tracking-tight
                      text-white

                      sm:text-4xl

                      md:text-5xl
                    "
                  >
                    {selected.name}
                  </h2>

                  {/* ACCENT LINE */}

                  <motion.div
                    initial={{
                      width: 0,
                    }}
                    animate={{
                      width: 60,
                    }}
                    transition={{
                      delay: 0.3,
                      duration: 0.5,
                    }}
                    className="
                      my-3
                      h-[3px]
                    "
                    style={{
                      backgroundColor: accent,
                    }}
                  />

                  {/* =================================================
                      TAGLINE + DESCRIPTION
                  ================================================= */}

                  <div
                    className="
                      space-y-2
                    "
                  >
                    {selected.tagline && (
                      <div
                        className="
                          inline-block
                          max-w-full
                          rounded-xs
                          border
                          border-white/10
                          bg-white/5
                          px-2
                          py-1
                          backdrop-blur-xs
                        "
                      >
                        <p
                          className="
                            truncate
                            font-mono
                            text-[8px]
                            font-semibold
                            uppercase
                            tracking-[0.15em]
                            text-white/90

                            sm:text-[9px]
                          "
                        >
                          {selected.tagline}
                        </p>
                      </div>
                    )}

                    {selected.desc && (
                      <div
                        className="
                          relative
                          border-l-2
                          py-1
                          pl-3
                        "
                        style={{
                          borderColor: `${accent}aa`,
                        }}
                      >
                        <p
                          className="
                            max-w-[280px]
                            font-mono
                            text-[9px]
                            leading-relaxed
                            tracking-wide
                            text-white/80

                            sm:text-[11px]
                          "
                        >
                          {selected.desc}
                        </p>
                      </div>
                    )}
                  </div>

                  {/* =================================================
                      VECTOR SIGNAL
                  ================================================= */}

                  {selected.trait_vector &&
                    selected.trait_vector.length >
                      0 && (
                      <div
                        className="
                          mt-4
                          rounded-sm
                          border
                          border-white/10
                          bg-black/40
                          p-2.5
                          backdrop-blur-xs

                          sm:mt-5
                          sm:p-3
                        "
                      >
                        <div
                          className="
                            mb-2
                            flex
                            items-center
                            justify-between
                          "
                        >
                          <span
                            className="
                              font-mono
                              text-[7px]
                              font-bold
                              tracking-widest

                              sm:text-[8px]
                            "
                            style={{
                              color: accent,
                            }}
                          >
                            SYNCED
                          </span>
                        </div>

                        <div
                          className="
                            flex
                            h-6
                            items-end
                            gap-1

                            sm:h-8
                          "
                        >
                          {selected.trait_vector.map(
                            (val, idx) => (
                              <div
                                key={idx}
                                className="
                                  flex-1
                                  rounded-t-xs
                                  bg-white/10
                                  transition-all
                                  duration-500
                                "
                                style={{
                                  height: `${Math.max(
                                    15,
                                    Math.min(
                                      100,
                                      val * 100
                                    )
                                  )}%`,
                                  backgroundColor:
                                    idx % 2 === 0
                                      ? accent
                                      : `${accent}88`,
                                }}
                              />
                            )
                          )}
                        </div>
                      </div>
                    )}
                </motion.div>
              </motion.div>
            )}
          </AnimatePresence>
        </aside>

        {/* =================================================
            RIGHT / REGISTRY
        ================================================= */}

        <section
          className="
            flex
            min-h-0
            min-w-0
            flex-1
            flex-col
          "
        >

          {/* =================================================
              FILTER + SEARCH
          ================================================= */}

          <div
            className="
              mb-4
              shrink-0
              border-b
              border-white/10
              pb-3

              md:mb-5
              md:pb-4
            "
          >

            {/* FILTERS */}

            <div
              className="
                flex
                w-full
                min-w-0
                items-center
              "
            >
              <div
                className="
                  flex
                  min-w-0
                  max-w-full
                  flex-1
                  gap-2
                  overflow-x-auto
                  pb-1
                  [scrollbar-width:none]
                  [&::-webkit-scrollbar]:hidden
                "
              >
                {franchises.map(
                  (franchise) => {
                    const active =
                      activeFranchise ===
                      franchise;

                    return (
                      <button
                        key={franchise}
                        onClick={() =>
                          setActiveFranchise(
                            franchise
                          )
                        }
                        className={`
                          relative
                          shrink-0
                          border
                          px-3
                          py-2
                          font-mono
                          text-[8px]
                          font-semibold
                          uppercase
                          tracking-[0.15em]
                          transition-all

                          sm:px-4
                          sm:text-[10px]
                          sm:tracking-[0.2em]

                          ${
                            active
                              ? 'border-[#3b82f6] bg-[#3b82f6]/10 text-[#3b82f6]'
                              : 'border-white/10 text-white/70 hover:border-white/30 hover:text-white'
                          }
                        `}
                      >
                        {formatFranchise(
                          franchise
                        )}

                        {active && (
                          <motion.span
                            layoutId="active-filter"
                            className="
                              absolute
                              bottom-[-1px]
                              left-0
                              h-[2px]
                              w-full
                              bg-[#3b82f6]
                            "
                          />
                        )}
                      </button>
                    );
                  }
                )}
              </div>
            </div>

            {/* SEARCH */}

            <div
              className="
                mt-3
                flex
                w-full
                shrink-0
                items-center
                border
                border-white/10
                bg-black/40
                focus-within:border-[#3b82f6]

                md:mt-0
                md:absolute
                md:right-0
                md:top-0
                md:w-[240px]
              "
            >
              <span
                className="
                  pl-3
                  font-mono
                  text-[#3b82f6]
                "
              >
                /
              </span>

              <input
                value={search}
                onChange={(e) =>
                  setSearch(e.target.value)
                }
                onKeyDown={(e) => {
                  if (e.key === 'Escape') {
                    setSearch('');
                  }
                }}
                placeholder="SEARCH NAME, TRAIT..."
                className="
                  w-full
                  min-w-0
                  bg-transparent
                  px-3
                  py-2.5
                  font-mono
                  text-[9px]
                  uppercase
                  tracking-[0.12em]
                  text-white
                  outline-none
                  placeholder:text-white/30

                  sm:text-[10px]
                "
              />

              {search && (
                <button
                  onClick={() =>
                    setSearch('')
                  }
                  className="
                    shrink-0
                    pr-3
                    font-mono
                    text-[11px]
                    text-white/40
                    hover:text-white
                  "
                >
                  ✕
                </button>
              )}
            </div>
          </div>

          {/* =================================================
              METADATA
          ================================================= */}

          <div
            className="
              mb-3
              flex
              shrink-0
              items-center
              justify-between
              gap-4
              font-mono
              text-[7px]
              uppercase
              tracking-[0.2em]
              text-white/40

              sm:text-[8px]
              sm:tracking-[0.25em]
            "
          >
            <span>
              Displaying //{' '}
              {filteredCharacters.length}
            </span>

            <span className="truncate text-right">
              Filter //{' '}
              {formatFranchise(
                activeFranchise
              )}
            </span>
          </div>

          {/* =================================================
              GRID CONTAINER
          ================================================= */}

          <div
            ref={gridContainerRef}
            className="
              thin-scroll
              min-h-0
              flex-1
              overflow-y-auto
              overflow-x-hidden
              pr-1

              sm:pr-2
            "
          >
            {/* =================================================
                LOADING
            ================================================= */}

            {loading ? (
              <div
                className="
                  flex
                  h-full
                  min-h-[200px]
                  items-center
                  justify-center
                  font-mono
                  text-[9px]
                  uppercase
                  tracking-[0.3em]
                  text-white/30
                "
              >
                Loading Registry...
              </div>
            ) : filteredCharacters.length ===
              0 ? (
              /* =================================================
                  EMPTY STATE
              ================================================= */

              <div
                className="
                  flex
                  h-full
                  min-h-[200px]
                  flex-col
                  items-center
                  justify-center
                  gap-2
                  text-center
                  font-mono
                  text-white/30
                "
              >
                <span
                  className="
                    text-[10px]
                    uppercase
                    tracking-[0.15em]

                    sm:text-[12px]
                    sm:tracking-[0.2em]
                  "
                >
                  No Matching Records Found
                </span>

                <button
                  onClick={() => {
                    setSearch('');
                    setActiveFranchise(
                      'all'
                    );
                  }}
                  className="
                    border
                    border-white/20
                    bg-white/5
                    px-3
                    py-1.5
                    text-[8px]
                    uppercase
                    tracking-[0.15em]
                    text-white
                    hover:bg-white/10
                  "
                >
                  Reset Filters
                </button>
              </div>
            ) : (
              /* =================================================
                  CHARACTER GRID
              ================================================= */

              <motion.div
                layout
                className="
                  grid
                  grid-cols-2
                  gap-3

                  sm:grid-cols-3
                  sm:gap-4

                  lg:grid-cols-4

                  xl:grid-cols-5
                "
              >
                <AnimatePresence mode="popLayout">
                  {filteredCharacters.map(
                    (character) => {
                      const isActive =
                        selected?.name ===
                        character.name;

                      const cardAccent =
                        character.geometry
                          ?.color ||
                        '#3b82f6';

                      return (
                        <motion.button
                          layout
                          key={`${character.franchise}-${character.name}`}
                          initial={{
                            opacity: 0,
                            y: 15,
                          }}
                          animate={{
                            opacity: 1,
                            y: 0,
                          }}
                          exit={{
                            opacity: 0,
                            scale: 0.95,
                          }}
                          whileHover={{
                            y: -3,
                          }}
                          whileTap={{
                            scale: 0.97,
                          }}
                          onClick={() =>
                            setSelected(
                              character
                            )
                          }
                          className={`
                            group
                            relative
                            aspect-[3/4]
                            overflow-hidden
                            border
                            bg-black
                            text-left

                            ${
                              isActive
                                ? 'border-white'
                                : 'border-white/10 hover:border-white/40'
                            }
                          `}
                        >
                          {/* IMAGE */}

                          <div
                            className="
                              absolute
                              inset-x-0
                              top-0
                              h-[75%]
                              overflow-hidden
                              bg-white/[0.02]
                            "
                          >
                            {character.image ? (
                              <img
                                src={
                                  character.image
                                }
                                alt={
                                  character.name
                                }
                                loading="lazy"
                                className="
                                  h-full
                                  w-full
                                  object-cover
                                  object-top
                                  opacity-80
                                  transition-all
                                  duration-500
                                  group-hover:scale-105
                                  group-hover:opacity-100
                                "
                              />
                            ) : (
                              <div
                                className="
                                  flex
                                  h-full
                                  items-center
                                  justify-center
                                  px-2
                                  text-center
                                  font-mono
                                  text-[7px]
                                  uppercase
                                  tracking-[0.15em]
                                  text-white/20
                                "
                              >
                                Image Pending
                              </div>
                            )}

                            <div
                              className="
                                absolute
                                inset-0
                                bg-gradient-to-t
                                from-[#070809]
                                via-transparent
                                to-transparent
                              "
                            />
                          </div>

                          {/* =================================================
                              CARD INFORMATION
                          ================================================= */}

                          <div
                            className="
                              absolute
                              inset-x-0
                              bottom-0
                              z-10
                              p-2

                              sm:p-3
                            "
                          >
                            <div
                              className="
                                mb-1
                                truncate
                                font-mono
                                text-[6px]
                                uppercase
                                tracking-[0.15em]
                                text-white/40

                                sm:text-[7px]
                                sm:tracking-[0.2em]
                              "
                            >
                              {formatFranchise(
                                character.franchise ||
                                  'unknown'
                              )}
                            </div>

                            <h3
                              className="
                                line-clamp-2
                                font-display
                                text-sm
                                font-black
                                uppercase
                                leading-tight
                                text-white

                                sm:text-lg
                              "
                            >
                              {character.name}
                            </h3>

                            <motion.div
                              className="
                                mt-1.5
                                h-[2px]

                                sm:mt-2
                              "
                              animate={{
                                width: isActive
                                  ? '100%'
                                  : '30%',
                              }}
                              style={{
                                backgroundColor:
                                  cardAccent,
                              }}
                            />
                          </div>

                          {/* =================================================
                              ACTIVE INDICATOR
                          ================================================= */}

                          {isActive && (
                            <motion.div
                              layoutId="active-character"
                              className="
                                absolute
                                right-2
                                top-2
                                z-20
                                h-1.5
                                w-1.5

                                sm:right-3
                                sm:top-3
                                sm:h-2
                                sm:w-2
                              "
                              style={{
                                backgroundColor:
                                  cardAccent,
                              }}
                            />
                          )}
                        </motion.button>
                      );
                    }
                  )}
                </AnimatePresence>
              </motion.div>
            )}
          </div>
        </section>
      </div>
    </DossierSection>
  );
}

// --------------------------------------------------
// FORMAT FRANCHISE
// --------------------------------------------------

function formatFranchise(
  franchise: string
) {
  if (franchise === 'all') {
    return 'All';
  }

  return franchise
    .replace(/_/g, ' ')
    .replace(/\b\w/g, (letter) =>
      letter.toUpperCase()
    );
}
