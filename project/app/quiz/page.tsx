'use client';

import { useSearchParams } from 'next/navigation';
import { QuizComponent } from '@/components/QuizComponent';

export default function QuizPage() {
  const searchParams = useSearchParams();
  const franchise = searchParams.get('franchise');

  if (!franchise) {
    return (
      <main className="min-h-dvh bg-[#11110f] text-[#e9e4d7]">
        <div className="flex min-h-dvh items-center justify-center">
          Missing franchise.
        </div>
      </main>
    );
  }

  return (
    <main className="min-h-dvh bg-[#11110f]">
      <QuizComponent franchise={franchise} />
    </main>
  );
}