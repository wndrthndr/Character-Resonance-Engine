'use client';

import {
  useEffect,
  useMemo,
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
  const [characters, setCharacters] = useState<Character[]>([]);
  const [selected, setSelected] = useState<Character | null>(null);

  const [activeFranchise, setActiveFranchise] =
    useState('all');

  const [search, setSearch] = useState('');
  const [debouncedSearch, setDebouncedSearch] =
    useState('');

  const [loading, setLoading] = useState(true);

  // Mobile switches between registry and profile.
  const [mobileView, setMobileView] =
    useState<'registry' | 'profile'>('registry');

  // --------------------------------------------------
  // SEARCH DEBOUNCE
  // --------------------------------------------------

  useEffect(() => {
    const timer = setTimeout(() => {
      setDebouncedSearch(search);
    }, 250);

    return () => clearTimeout(timer);
  }, [search]);

  // --------------------------------------------------
  // LOAD CHARACTERS
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

        if (data.length > 0) {
          setSelected(data[0]);
        }
      } catch (error) {
        console.error(
          'Registry error:',
          error
        );
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
          .map(
            (character) =>
              character.franchise
          )
          .filter(Boolean)
      )
    ) as string[];

    return ['all', ...unique];
  }, [characters]);

  // --------------------------------------------------
  // FILTER
  // --------------------------------------------------

  const filteredCharacters = useMemo(() => {
    const query =
      debouncedSearch
        .trim()
        .toLowerCase();

    const matched =
      characters.filter(
        (character) => {
          const franchiseMatch =
            activeFranchise === 'all' ||
            character.franchise ===
              activeFranchise;

          if (!franchiseMatch) {
            return false;
          }

          if (!query) {
            return true;
          }

          const nameMatch =
            character.name
              .toLowerCase()
              .includes(query);

          const taglineMatch =
            character.tagline
              ?.toLowerCase()
              .includes(query) ??
            false;

          const descMatch =
            character.desc
              ?.toLowerCase()
              .includes(query) ??
            false;

          const franchiseMatchText =
            character.franchise
              ?.toLowerCase()
              .includes(query) ??
            false;

          const traitMatch =
            character.traits?.some(
              (trait) =>
                trait
                  .toLowerCase()
                  .includes(query)
            ) ?? false;

          return (
            nameMatch ||
            taglineMatch ||
            descMatch ||
            franchiseMatchText ||
            traitMatch
          );
        }
      );

    // Shuffle only for "all"
    // without search.
    if (
      activeFranchise === 'all' &&
      !query
    ) {
      const shuffled = [...matched];

      for (
        let i = shuffled.length - 1;
        i > 0;
        i--
      ) {
        const j = Math.floor(
          Math.random() * (i + 1)
        );

        [
          shuffled[i],
          shuffled[j],
        ] = [
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
  // KEEP SELECTED VALID
  // --------------------------------------------------

  useEffect(() => {
    if (
      filteredCharacters.length === 0
    ) {
      setSelected(null);
      return;
    }

    const stillExists =
      filteredCharacters.some(
        (character) =>
          character.name ===
          selected?.name
      );

    if (!stillExists) {
      setSelected(
        filteredCharacters[0]
      );
    }
  }, [
    filteredCharacters,
    selected?.name,
  ]);

  // --------------------------------------------------
  // SELECT CHARACTER
  // --------------------------------------------------

  function selectCharacter(
    character: Character
  ) {
    setSelected(character);

    // On mobile, switch to profile.
    setMobileView('profile');
  }

  // --------------------------------------------------
  // BACK TO REGISTRY
  // --------------------------------------------------

  function backToRegistry() {
    setMobileView('registry');
  }

  const accent =
    selected?.geometry?.color ||
    '#3b82f6';

  return (
    <DossierSection
      index={3}
      label="04 / REGISTRY_GRID"
      fileId="AX-9999"
    >
      {/* =====================================================
          BACKGROUND
      ===================================================== */}

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

      <motion.div
        animate={{
          backgroundColor:
            `${accent}0a`,
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

      {/* =====================================================
          =====================================================
          MOBILE UI
          =====================================================
          ===================================================== */}

      <div
        className="
          relative
          z-10
          flex
          h-full
          min-h-0
          w-full
          flex-col
          overflow-hidden
          p-4
          pt-14

          sm:p-6
          sm:pt-16

          md:hidden
        "
      >
        <AnimatePresence mode="wait">

          {/* =================================================
              MOBILE REGISTRY
          ================================================= */}

          {mobileView === 'registry' && (
            <motion.div
              key="mobile-registry"
              initial={{
                opacity: 0,
                x: -20,
              }}
              animate={{
                opacity: 1,
                x: 0,
              }}
              exit={{
                opacity: 0,
                x: -20,
              }}
              transition={{
                duration: 0.25,
              }}
              className="
                flex
                h-full
                min-h-0
                flex-col
              "
            >

              {/* ---------------------------------------------
                  HEADER
              --------------------------------------------- */}

              <div
                className="
                  mb-4
                  flex
                  shrink-0
                  items-end
                  justify-between
                  border-b
                  border-white/10
                  pb-3
                "
              >
                <div>
                  <div
                    className="
                      mb-1
                      font-mono
                      text-[7px]
                      uppercase
                      tracking-[0.3em]
                      text-white/30
                    "
                  >
                    AX-9999 / CHARACTER INDEX
                  </div>

                  <h2
                    className="
                      font-display
                      text-2xl
                      font-black
                      uppercase
                      leading-none
                      tracking-tight
                      text-white

                      sm:text-3xl
                    "
                  >
                    Registry
                  </h2>
                </div>

                <div
                  className="
                    text-right
                    font-mono
                  "
                >
                  <div
                    className="
                      text-[8px]
                      uppercase
                      tracking-[0.2em]
                      text-white/30
                    "
                  >
                    Records
                  </div>

                  <div
                    className="
                      text-lg
                      font-bold
                      text-white
                    "
                  >
                    {filteredCharacters.length
                      .toString()
                      .padStart(
                        2,
                        '0'
                      )}
                  </div>
                </div>
              </div>

              {/* ---------------------------------------------
                  FRANCHISE FILTERS
              --------------------------------------------- */}

              <div
                className="
                  mb-3
                  shrink-0
                  overflow-x-auto
                  [scrollbar-width:none]
                  [&::-webkit-scrollbar]:hidden
                "
              >
                <div
                  className="
                    flex
                    w-max
                    gap-2
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

                            ${
                              active
                                ? 'border-[#3b82f6] bg-[#3b82f6]/10 text-[#3b82f6]'
                                : 'border-white/10 text-white/50'
                            }
                          `}
                        >
                          {formatFranchise(
                            franchise
                          )}

                          {active && (
                            <motion.div
                              layoutId="mobile-filter"
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

              {/* ---------------------------------------------
                  SEARCH
              --------------------------------------------- */}

              <div
                className="
                  mb-4
                  flex
                  h-9
                  shrink-0
                  items-center
                  border
                  border-white/10
                  bg-black/40
                  focus-within:border-[#3b82f6]
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
                    setSearch(
                      e.target.value
                    )
                  }
                  onKeyDown={(e) => {
                    if (
                      e.key === 'Escape'
                    ) {
                      setSearch('');
                    }
                  }}
                  placeholder="SEARCH NAME, TRAIT..."
                  className="
                    min-w-0
                    flex-1
                    bg-transparent
                    px-3
                    font-mono
                    text-[8px]
                    uppercase
                    tracking-[0.15em]
                    text-white
                    outline-none
                    placeholder:text-white/25
                  "
                />

                {search && (
                  <button
                    onClick={() =>
                      setSearch('')
                    }
                    className="
                      px-3
                      font-mono
                      text-[10px]
                      text-white/40
                    "
                  >
                    ✕
                  </button>
                )}
              </div>

              {/* ---------------------------------------------
                  GRID LABEL
              --------------------------------------------- */}

              <div
                className="
                  mb-2
                  flex
                  shrink-0
                  items-center
                  justify-between
                  font-mono
                  text-[7px]
                  uppercase
                  tracking-[0.2em]
                  text-white/30
                "
              >
                <span>
                  Displaying //
                  {' '}
                  {filteredCharacters.length}
                </span>

                <span>
                  Swipe →
                </span>
              </div>

              {/* =================================================
                  MOBILE CHARACTER GRID

                  IMPORTANT:
                  NO VERTICAL SCROLL.

                  Cards are placed in 2 rows and the whole
                  registry moves horizontally.
              ================================================= */}

              <div
                className="
                  min-h-0
                  flex-1
                  overflow-x-auto
                  overflow-y-hidden
                  [scrollbar-width:none]
                  [&::-webkit-scrollbar]:hidden
                "
              >
                {loading ? (
                  <div
                    className="
                      flex
                      h-full
                      min-w-full
                      items-center
                      justify-center
                      font-mono
                      text-[8px]
                      uppercase
                      tracking-[0.3em]
                      text-white/30
                    "
                  >
                    Loading Registry...
                  </div>
                ) : filteredCharacters.length ===
                  0 ? (
                  <div
                    className="
                      flex
                      h-full
                      min-w-full
                      flex-col
                      items-center
                      justify-center
                      gap-3
                      font-mono
                    "
                  >
                    <span
                      className="
                        text-[9px]
                        uppercase
                        tracking-[0.15em]
                        text-white/30
                      "
                    >
                      No Matching Records
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
                        text-[7px]
                        uppercase
                        tracking-[0.15em]
                        text-white
                      "
                    >
                      Reset Filters
                    </button>
                  </div>
                ) : (
                  <div
                    className="
                      grid
                      h-full
                      grid-flow-col
                      grid-rows-2
                      auto-cols-[120px]
                      gap-3
                      pb-2

                      sm:auto-cols-[145px]
                    "
                  >
                    <AnimatePresence mode="popLayout">
                      {filteredCharacters.map(
                        (
                          character
                        ) => {
                          const isActive =
                            selected?.name ===
                            character.name;

                          const cardAccent =
                            character
                              .geometry
                              ?.color ||
                            '#3b82f6';

                          return (
                            <motion.button
                              layout
                              key={`${character.franchise}-${character.name}`}
                              initial={{
                                opacity: 0,
                                scale: 0.96,
                              }}
                              animate={{
                                opacity: 1,
                                scale: 1,
                              }}
                              exit={{
                                opacity: 0,
                                scale: 0.9,
                              }}
                              whileTap={{
                                scale: 0.96,
                              }}
                              onClick={() =>
                                selectCharacter(
                                  character
                                )
                              }
                              className={`
                                group
                                relative
                                min-h-0
                                overflow-hidden
                                border
                                bg-black
                                text-left

                                ${
                                  isActive
                                    ? 'border-white'
                                    : 'border-white/10'
                                }
                              `}
                            >
                              {/* IMAGE */}

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
                                    absolute
                                    inset-0
                                    h-full
                                    w-full
                                    object-cover
                                    object-top
                                    opacity-80
                                    transition-transform
                                    duration-500
                                    group-active:scale-105
                                  "
                                />
                              ) : (
                                <div
                                  className="
                                    absolute
                                    inset-0
                                    flex
                                    items-center
                                    justify-center
                                    font-mono
                                    text-[6px]
                                    uppercase
                                    tracking-[0.15em]
                                    text-white/20
                                  "
                                >
                                  Image Pending
                                </div>
                              )}

                              {/* OVERLAY */}

                              <div
                                className="
                                  absolute
                                  inset-0
                                  bg-gradient-to-t
                                  from-black
                                  via-black/20
                                  to-transparent
                                "
                              />

                              {/* INFO */}

                              <div
                                className="
                                  absolute
                                  inset-x-0
                                  bottom-0
                                  z-10
                                  p-2
                                "
                              >
                                <div
                                  className="
                                    mb-0.5
                                    truncate
                                    font-mono
                                    text-[5px]
                                    uppercase
                                    tracking-[0.15em]
                                    text-white/40
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
                                    text-xs
                                    font-black
                                    uppercase
                                    leading-tight
                                    text-white
                                  "
                                >
                                  {
                                    character.name
                                  }
                                </h3>

                                <div
                                  className="
                                    mt-1.5
                                    h-[2px]
                                  "
                                  style={{
                                    width:
                                      isActive
                                        ? '100%'
                                        : '30%',
                                    backgroundColor:
                                      cardAccent,
                                  }}
                                />
                              </div>

                              {/* ACTIVE */}

                              {isActive && (
                                <div
                                  className="
                                    absolute
                                    right-2
                                    top-2
                                    z-20
                                    h-1.5
                                    w-1.5
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
                  </div>
                )}
              </div>

              {/* ---------------------------------------------
                  MOBILE HINT
              --------------------------------------------- */}

              <div
                className="
                  mt-2
                  flex
                  shrink-0
                  items-center
                  justify-between
                  font-mono
                  text-[6px]
                  uppercase
                  tracking-[0.2em]
                  text-white/20
                "
              >
                <span>
                  Select a record
                </span>

                <span>
                  Registry / 04
                </span>
              </div>
            </motion.div>
          )}

          {/* =================================================
              MOBILE PROFILE
          ================================================= */}

          {mobileView === 'profile' &&
            selected && (
              <motion.div
                key="mobile-profile"
                initial={{
                  opacity: 0,
                  x: 20,
                }}
                animate={{
                  opacity: 1,
                  x: 0,
                }}
                exit={{
                  opacity: 0,
                  x: 20,
                }}
                transition={{
                  duration: 0.25,
                }}
                className="
                  flex
                  h-full
                  min-h-0
                  flex-col
                "
              >

                {/* ---------------------------------------------
                    PROFILE HEADER
                --------------------------------------------- */}

                <div
                  className="
                    mb-3
                    flex
                    shrink-0
                    items-center
                    justify-between
                  "
                >
                  <button
                    onClick={
                      backToRegistry
                    }
                    className="
                      flex
                      items-center
                      gap-2
                      border
                      border-white/10
                      bg-white/[0.03]
                      px-3
                      py-2
                      font-mono
                      text-[7px]
                      uppercase
                      tracking-[0.2em]
                      text-white/60
                    "
                  >
                    <span>
                      ←
                    </span>

                    Registry
                  </button>

                  <span
                    className="
                      font-mono
                      text-[7px]
                      uppercase
                      tracking-[0.25em]
                      text-white/20
                    "
                  >
                    Active Profile
                  </span>
                </div>

                {/* ---------------------------------------------
                    PROFILE CONTENT
                --------------------------------------------- */}

                <div
                  className="
                    min-h-0
                    flex-1
                    overflow-hidden
                    border
                    border-white/10
                    bg-black
                  "
                >
                  <div
                    className="
                      relative
                      flex
                      h-full
                      min-h-0
                      flex-col
                      overflow-hidden
                    "
                  >

                    {/* IMAGE */}

                    {selected.image ? (
                      <motion.img
                        key={
                          selected.name
                        }
                        initial={{
                          scale: 1.08,
                          opacity: 0,
                        }}
                        animate={{
                          scale: 1,
                          opacity: 1,
                        }}
                        transition={{
                          duration: 0.4,
                        }}
                        src={
                          selected.image
                        }
                        alt={
                          selected.name
                        }
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
                          bg-white/[0.02]
                        "
                      />
                    )}

                    {/* IMAGE OVERLAY */}

                    <div
                      className="
                        pointer-events-none
                        absolute
                        inset-0
                        bg-gradient-to-b
                        from-black/40
                        via-black/30
                        to-black
                      "
                    />

                    <div
                      className="
                        pointer-events-none
                        absolute
                        inset-x-0
                        bottom-0
                        h-[75%]
                        bg-gradient-to-t
                        from-[#070809]
                        via-[#070809]/95
                        to-transparent
                      "
                    />

                    {/* PROFILE DATA */}

                    <div
                      className="
                        relative
                        z-10
                        mt-auto
                        p-4

                        sm:p-6
                      "
                    >

                      {/* FRANCHISE */}

                      <div
                        className="
                          mb-1
                          font-mono
                          text-[7px]
                          font-bold
                          uppercase
                          tracking-[0.25em]

                          sm:text-[9px]
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
                          max-w-full
                          font-display
                          text-3xl
                          font-black
                          uppercase
                          leading-[0.9]
                          tracking-tight
                          text-white

                          sm:text-4xl
                        "
                      >
                        {
                          selected.name
                        }
                      </h2>

                      {/* LINE */}

                      <div
                        className="
                          my-2
                          h-[3px]
                          w-12
                        "
                        style={{
                          backgroundColor:
                            accent,
                        }}
                      />

                      {/* TAGLINE */}

                      {selected.tagline && (
                        <div
                          className="
                            mb-2
                            inline-block
                            max-w-full
                            border
                            border-white/10
                            bg-white/5
                            px-2
                            py-1
                          "
                        >
                          <span
                            className="
                              block
                              truncate
                              font-mono
                              text-[7px]
                              font-semibold
                              uppercase
                              tracking-[0.15em]
                              text-white/80
                            "
                          >
                            {
                              selected.tagline
                            }
                          </span>
                        </div>
                      )}

                      {/* DESCRIPTION */}

                      {selected.desc && (
                        <div
                          className="
                            mb-3
                            border-l-2
                            py-1
                            pl-3
                          "
                          style={{
                            borderColor:
                              `${accent}aa`,
                          }}
                        >
                          <p
                            className="
                              line-clamp-4
                              font-mono
                              text-[9px]
                              leading-relaxed
                              tracking-wide
                              text-white/75

                              sm:text-[10px]
                            "
                          >
                            {
                              selected.desc
                            }
                          </p>
                        </div>
                      )}

                      {/* VECTOR */}

                      {selected.trait_vector &&
                        selected
                          .trait_vector
                          .length >
                          0 && (
                          <div
                            className="
                              rounded-sm
                              border
                              border-white/10
                              bg-black/50
                              p-2
                              backdrop-blur-sm
                            "
                          >
                            <div
                              className="
                                mb-1
                                font-mono
                                text-[6px]
                                font-bold
                                tracking-[0.2em]
                              "
                              style={{
                                color:
                                  accent,
                              }}
                            >
                              VECTOR
                              {' '}
                              / SYNCED
                            </div>

                            <div
                              className="
                                flex
                                h-6
                                items-end
                                gap-1
                              "
                            >
                              {selected.trait_vector.map(
                                (
                                  val,
                                  idx
                                ) => (
                                  <div
                                    key={
                                      idx
                                    }
                                    className="
                                      flex-1
                                      rounded-t-xs
                                    "
                                    style={{
                                      height: `${Math.max(
                                        15,
                                        Math.min(
                                          100,
                                          val *
                                            100
                                        )
                                      )}%`,
                                      backgroundColor:
                                        idx %
                                          2 ===
                                        0
                                          ? accent
                                          : `${accent}88`,
                                    }}
                                  />
                                )
                              )}
                            </div>
                          </div>
                        )}
                    </div>
                  </div>
                </div>
              </motion.div>
            )}
        </AnimatePresence>
      </div>

      {/* =====================================================
          =====================================================
          DESKTOP UI
          =====================================================
          ===================================================== */}

      <div
        className="
          relative
          z-10
          hidden
          h-full
          min-h-0
          w-full
          gap-8
          overflow-hidden
          p-8
          pt-16

          md:flex
          md:p-10
          md:pt-20

          lg:p-12
        "
      >

        {/* =================================================
            DESKTOP POSTER
        ================================================= */}

        <aside
          className="
            relative
            w-[300px]
            shrink-0
            overflow-hidden
            border-r
            border-white/10
            pr-6

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
                  absolute
                  inset-0
                  flex
                  flex-col
                  justify-between
                  p-6
                "
              >

                {/* IMAGE */}

                {selected.image ? (
                  <motion.img
                    key={
                      selected.name
                    }
                    src={
                      selected.image
                    }
                    alt={
                      selected.name
                    }
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
                        text-[10px]
                        uppercase
                        tracking-[0.3em]
                        text-white/20
                      "
                    >
                      Image Pending
                    </div>
                  </div>
                )}

                {/* OVERLAYS */}

                <div
                  className="
                    pointer-events-none
                    absolute
                    inset-0
                    bg-gradient-to-b
                    from-black/40
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
                    h-[75%]
                    bg-gradient-to-t
                    from-[#070809]
                    via-[#070809]/90
                    to-transparent
                  "
                />

                {/* BADGE */}

                <div
                  className="
                    relative
                    z-20
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
                        backgroundColor:
                          accent,
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
                        backgroundColor:
                          accent,
                      }}
                    />
                  </span>

                  <span
                    className="
                      font-mono
                      text-[9px]
                      font-semibold
                      uppercase
                      tracking-[0.3em]
                      text-white/80
                    "
                  >
                    Active Profile
                  </span>
                </div>

                {/* INFO */}

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
                  "
                >
                  <div
                    className="
                      mb-2
                      font-mono
                      text-[10px]
                      font-bold
                      uppercase
                      tracking-[0.3em]
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

                  <h2
                    className="
                      font-display
                      text-4xl
                      font-black
                      uppercase
                      leading-[0.9]
                      tracking-tight
                      text-white

                      lg:text-5xl
                    "
                  >
                    {
                      selected.name
                    }
                  </h2>

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
                      backgroundColor:
                        accent,
                    }}
                  />

                  {selected.tagline && (
                    <div
                      className="
                        mb-2
                        inline-block
                        rounded-xs
                        border
                        border-white/10
                        bg-white/5
                        px-2
                        py-0.5
                      "
                    >
                      <p
                        className="
                          font-mono
                          text-[9px]
                          font-semibold
                          uppercase
                          tracking-[0.2em]
                          text-white/90
                        "
                      >
                        {
                          selected.tagline
                        }
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
                        borderColor:
                          `${accent}aa`,
                      }}
                    >
                      <p
                        className="
                          max-w-[280px]
                          font-mono
                          text-[11px]
                          leading-relaxed
                          tracking-wide
                          text-white/80
                        "
                      >
                        {
                          selected.desc
                        }
                      </p>
                    </div>
                  )}

                  {selected.trait_vector &&
                    selected
                      .trait_vector
                      .length >
                      0 && (
                      <div
                        className="
                          mt-5
                          rounded-sm
                          border
                          border-white/10
                          bg-black/40
                          p-3
                        "
                      >
                        <div
                          className="
                            mb-2
                            font-mono
                            text-[8px]
                            font-bold
                            tracking-widest
                          "
                          style={{
                            color:
                              accent,
                          }}
                        >
                          SYNCED
                        </div>

                        <div
                          className="
                            flex
                            h-8
                            items-end
                            gap-1
                          "
                        >
                          {selected.trait_vector.map(
                            (
                              val,
                              idx
                            ) => (
                              <div
                                key={
                                  idx
                                }
                                className="
                                  flex-1
                                  rounded-t-xs
                                "
                                style={{
                                  height: `${Math.max(
                                    15,
                                    Math.min(
                                      100,
                                      val *
                                        100
                                    )
                                  )}%`,
                                  backgroundColor:
                                    idx %
                                      2 ===
                                    0
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
            DESKTOP REGISTRY
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

          {/* FILTER BAR */}

          <div
            className="
              relative
              mb-5
              flex
              shrink-0
              items-center
              gap-4
              border-b
              border-white/10
              pb-4
            "
          >
            <div
              className="
                flex
                min-w-0
                flex-1
                gap-2
                overflow-x-auto
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
                        px-4
                        py-2
                        font-mono
                        text-[10px]
                        font-semibold
                        uppercase
                        tracking-[0.2em]
                        transition-all

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
                          layoutId="desktop-filter"
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

            {/* SEARCH */}

            <div
              className="
                flex
                w-[240px]
                shrink-0
                items-center
                border
                border-white/10
                bg-black/40
                focus-within:border-[#3b82f6]
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
                  setSearch(
                    e.target.value
                  )
                }
                onKeyDown={(e) => {
                  if (
                    e.key === 'Escape'
                  ) {
                    setSearch('');
                  }
                }}
                placeholder="SEARCH NAME, TRAIT..."
                className="
                  w-full
                  bg-transparent
                  px-3
                  py-2
                  font-mono
                  text-[10px]
                  uppercase
                  tracking-[0.15em]
                  text-white
                  outline-none
                  placeholder:text-white/30
                "
              />

              {search && (
                <button
                  onClick={() =>
                    setSearch('')
                  }
                  className="
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

          {/* METADATA */}

          <div
            className="
              mb-3
              flex
              shrink-0
              items-center
              justify-between
              font-mono
              text-[8px]
              uppercase
              tracking-[0.25em]
              text-white/40
            "
          >
            <span>
              Displaying //
              {' '}
              {filteredCharacters.length}
            </span>

            <span>
              Filter //
              {' '}
              {formatFranchise(
                activeFranchise
              )}
            </span>
          </div>

          {/* GRID */}

          <div
            className="
              thin-scroll
              min-h-0
              flex-1
              overflow-y-auto
              pr-2
            "
          >
            {loading ? (
              <div
                className="
                  flex
                  h-full
                  items-center
                  justify-center
                  font-mono
                  text-[10px]
                  uppercase
                  tracking-[0.3em]
                  text-white/30
                "
              >
                Loading Registry...
              </div>
            ) : filteredCharacters.length ===
              0 ? (
              <div
                className="
                  flex
                  h-full
                  flex-col
                  items-center
                  justify-center
                  gap-2
                  font-mono
                  text-white/30
                "
              >
                <span
                  className="
                    text-[12px]
                    uppercase
                    tracking-[0.2em]
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
                    py-1
                    text-[9px]
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
              <motion.div
                layout
                className="
                  grid
                  grid-cols-3
                  gap-4

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
                        character
                          .geometry
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
                            selectCharacter(
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
                                  font-mono
                                  text-[8px]
                                  uppercase
                                  tracking-[0.2em]
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

                          <div
                            className="
                              absolute
                              inset-x-0
                              bottom-0
                              z-10
                              p-3
                            "
                          >
                            <div
                              className="
                                mb-1
                                font-mono
                                text-[7px]
                                uppercase
                                tracking-[0.2em]
                                text-white/40
                              "
                            >
                              {formatFranchise(
                                character.franchise ||
                                  'unknown'
                              )}
                            </div>

                            <h3
                              className="
                                font-display
                                text-lg
                                font-black
                                uppercase
                                leading-tight
                                text-white
                              "
                            >
                              {
                                character.name
                              }
                            </h3>

                            <motion.div
                              className="
                                mt-2
                                h-[2px]
                              "
                              animate={{
                                width:
                                  isActive
                                    ? '100%'
                                    : '30%',
                              }}
                              style={{
                                backgroundColor:
                                  cardAccent,
                              }}
                            />
                          </div>

                          {isActive && (
                            <motion.div
                              layoutId="desktop-active-character"
                              className="
                                absolute
                                right-3
                                top-3
                                z-20
                                h-2
                                w-2
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

// =====================================================
// FORMAT FRANCHISE
// =====================================================

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
