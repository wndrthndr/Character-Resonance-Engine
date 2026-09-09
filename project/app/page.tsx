'use client';

import { PinnedScroll } from '@/components/pinned-scroll';
import { AtmosphereSection } from '@/components/sections/atmosphere-section';
import { UniverseSection } from '@/components/sections/briefing-section';
import { ThesisSection } from '@/components/sections/thesis-section';
import { CharacterIndexSection } from '@/components/sections/character-index-section';

const SECTION_COUNT = 4;

export default function Page() {
  return (
    <main className="archive-shell relative bg-ink">
      <PinnedScroll sections={SECTION_COUNT}>
        <AtmosphereSection />

        <UniverseSection />

        <CharacterIndexSection />

        <ThesisSection />
      </PinnedScroll>
    </main>
  );
}