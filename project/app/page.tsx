return (
  <main className="min-h-dvh bg-ink">
    {stage === 'SELECT' ? (
      <PinnedScroll
        key="landing"
        sections={SECTION_COUNT}
      >
        <AtmosphereSection />

        <UniverseSection
          onSelectFranchise={handleFranchiseSelection}
        />

        <CharacterIndexSection />

        <ThesisSection />
      </PinnedScroll>
    ) : (
      <div key="quiz" className="min-h-dvh">
        <QuizComponent franchise={franchise!} />
      </div>
    )}
  </main>
);
