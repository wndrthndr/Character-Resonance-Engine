'use client';

import * as React from 'react';
import {
  createContext,
  useCallback,
  useContext,
  useEffect,
  useMemo,
  useRef,
  useSyncExternalStore,
} from 'react';
import gsap from 'gsap';
import { ScrollTrigger } from 'gsap/ScrollTrigger';
import { ScrollToPlugin } from 'gsap/ScrollToPlugin';

if (typeof window !== 'undefined') {
  gsap.registerPlugin(ScrollTrigger, ScrollToPlugin);
}

export type ProgressState = {
  /** 0..1 progress across the entire pinned sequence */
  progress: number;
  /** index of the section currently most in view (0-based) */
  activeIndex: number;
  /** total number of sections */
  total: number;
};

/**
 * Lightweight external store for scroll progress.
 *
 * Progress changes at scroll-frame frequency (every scrub tick). Piping that
 * through React state on the provider would re-render every consumer of
 * useArchive() — including ones that only need the stable `goTo` /
 * `registerSection` functions — on every frame. Instead we keep progress in
 * a plain object with a subscriber list, and only components that call
 * useArchiveProgress() re-render, via useSyncExternalStore.
 */
function createProgressStore(total: number) {
  let state: ProgressState = { progress: 0, activeIndex: 0, total };
  const listeners = new Set<() => void>();
  return {
    get: () => state,
    set(next: ProgressState) {
      state = next;
      listeners.forEach((l) => l());
    },
    subscribe(listener: () => void) {
      listeners.add(listener);
      return () => listeners.delete(listener);
    },
  };
}
type ProgressStore = ReturnType<typeof createProgressStore>;

type Ctx = {
  /** jump to a section by index (scrolls the page) */
  goTo: (index: number) => void;
  /** register a section node so the engine knows the count + can animate it */
  registerSection: (el: HTMLElement) => () => void;
  /** force ScrollTrigger to recompute pin distances (e.g. after content resizes) */
  refresh: () => void;
  store: ProgressStore;
};

const ArchiveContext = createContext<Ctx | null>(null);

function useArchiveCtx() {
  const ctx = useContext(ArchiveContext);
  if (!ctx) throw new Error('useArchive must be used within <PinnedScroll>');
  return ctx;
}

/** Stable API (functions only, never changes reference on scroll) */
export function useArchive() {
  const { goTo, registerSection, refresh } = useArchiveCtx();
  return { goTo, registerSection, refresh };
}

/** High-frequency progress. Only components that call this re-render on scroll. */
export function useArchiveProgress(): ProgressState {
  const { store } = useArchiveCtx();
  return useSyncExternalStore(store.subscribe, store.get, store.get);
}

type Props = {
  children: React.ReactNode;
  /**
   * Number of full-screen sections that slide horizontally. If omitted, it's
   * derived from the number of top-level children, which avoids a common
   * class of bugs where this prop drifts out of sync with actual content.
   */
  sections?: number;
  /** optional fixed overlay rendered inside the archive context but outside the transformed track */
  overlay?: React.ReactNode;
};

/**
 * Pinned-Scroll Engine
 * --------------------
 * Translates standard vertical scroll into a horizontal slide across N
 * full-screen sections. The viewport is "pinned" for the duration of the
 * sequence (ScrollTrigger pin), and the horizontal track is translated by
 * -(trackWidth - viewportWidth). Each section reveals as it enters center
 * stage.
 *
 * Layout model:
 *   .archive-pinned        — the pinned wrapper, height = N * 100vh of scroll
 *   .archive-track         — horizontal flex track, width = N * 100vw
 *   .archive-section       — each full-screen panel (100vw x 100vh)
 *
 * Accessibility: respects `prefers-reduced-motion`. When reduced motion is
 * requested, the horizontal pin/scrub is skipped entirely and sections fall
 * back to normal vertical document flow (no scroll-hijacking).
 */


// ... (Keep your ProgressState, createProgressStore, and Context setup here)

export function PinnedScroll({ children, sections, overlay }: Props) {
  const wrapperRef = useRef<HTMLDivElement>(null);
  const sectionEls = useRef<HTMLElement[]>([]);
  const total = sections ?? Math.max(1, React.Children.count(children));
  const store = useRef(createProgressStore(total)).current;

  const registerSection = useCallback((el: HTMLElement) => {
    sectionEls.current.push(el);
    // Apply GPU acceleration styles immediately
    el.style.willChange = 'transform';
    el.style.backfaceVisibility = 'hidden';
    return () => { sectionEls.current = sectionEls.current.filter((s) => s !== el); };
  }, []);

  useEffect(() => {
    const wrapper = wrapperRef.current;
    if (!wrapper || sectionEls.current.length === 0) return;

    // 1. Initial State: Stack absolutely
    gsap.set(sectionEls.current, { 
      position: 'absolute', 
      top: 0, 
      left: 0, 
      width: '100%', 
      height: '100vh' 
    });

    // 2. High-Performance Timeline
    const tl = gsap.timeline({
      scrollTrigger: {
        trigger: wrapper,
        start: 'top top',
        end: () => `+=${total * 800}`,
        pin: true,
        scrub: 0.1, // Near-instant 1:1 tracking
        anticipatePin: 1,
        fastScrollEnd: true, // Optimizes for quick scrolls
        preventOverlaps: true,
        onUpdate: (self) => {
          const active = Math.min(total - 1, Math.round(self.progress * (total - 1)));
          store.set({ progress: self.progress, activeIndex: active, total });
        }
      }
    });

    // 3. Snappy Motion
    sectionEls.current.forEach((sec, i) => {
      if (i === 0) return;
      // Using 'none' ease for 1:1 scroll feel
      tl.fromTo(sec, { xPercent: 100 }, { xPercent: 0, ease: 'none' }, i);
    });

    return () => { tl.scrollTrigger?.kill(); };
  }, [total, store]);

  return (
    <ArchiveContext.Provider value={{ goTo: () => {}, registerSection, refresh: () => ScrollTrigger.refresh(), store }}>
      <div ref={wrapperRef} className="archive-pinned relative h-screen w-full overflow-hidden">
        {children}
        {overlay}
      </div>
    </ArchiveContext.Provider>
  );
}