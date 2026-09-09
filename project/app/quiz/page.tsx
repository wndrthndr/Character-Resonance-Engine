'use client';
import { useSearchParams } from 'next/navigation';
import { QuizComponent } from '@/components/QuizComponent';
import { Suspense } from 'react';

export default function QuizPage() {
  const searchParams = useSearchParams();
  const franchise = searchParams.get('franchise');

  if (!franchise) return <div>Invalid selection.</div>;

  return (
    <main className="min-h-screen bg-black">
      {/* QuizComponent stays the same as before */}
      <Suspense fallback={<div>Loading Quiz...</div>}>
        <QuizComponent franchise={franchise} />
      </Suspense>
    </main>
  );
}