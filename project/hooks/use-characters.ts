'use client';

import { useEffect, useState } from 'react';
import { supabase } from '@/lib/supabase';
import type { Character } from '@/lib/types';

type State = {
  characters: Character[];
  loading: boolean;
  error: string | null;
};

export function useCharacters(): State {
  const [characters, setCharacters] = useState<Character[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    let active = true;
    setLoading(true);
    supabase
      .from('characters')
      .select('*')
      .order('sort_index', { ascending: true })
      .then(({ data, error: err }) => {
        if (!active) return;
        if (err) {
          setError(err.message);
        } else {
          setCharacters((data as Character[]) ?? []);
        }
        setLoading(false);
      });
    return () => {
      active = false;
    };
  }, []);

  return { characters, loading, error };
}
