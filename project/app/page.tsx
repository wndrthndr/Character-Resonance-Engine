'use client';

import { useState } from 'react';
import { PinnedScroll } from '@/components/pinned-scroll';
import { AtmosphereSection } from '@/components/sections/atmosphere-section';
import { UniverseSection } from '@/components/sections/briefing-section';
import { ThesisSection } from '@/components/sections/thesis-section';
import { CharacterIndexSection } from '@/components/sections/character-index-section';
import { QuizComponent } from '@/components/QuizComponent';

const SECTION_COUNT = 4;

export default function Page() {
  const [stage, setStage] = useState<'SELECT' | 'QUIZ'>('SELECT');
  const [franchise, setFranchise] = useState<string | null>(null);

  const handleFranchiseSelection = (selectedFranchise: string) => {
    setFranchise(selectedFranchise);
    setStage('QUIZ');
  };

  if (stage === 'QUIZ') {
    return (
      <main className="min-h-dvh bg-ink">
        <QuizComponent franchise={franchise!} />
      </main>
    );
  }

  return (
    <main className="archive-shell relative bg-ink">
      <PinnedScroll sections={SECTION_COUNT}>
        <AtmosphereSection />
        <UniverseSection onSelectFranchise={handleFranchiseSelection} />
        <CharacterIndexSection />
        <ThesisSection />
      </PinnedScroll>
    </main>
  );
}
