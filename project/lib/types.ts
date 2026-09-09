export type CharacterStatus =
  | 'ACTIVE'
  | 'BURNED'
  | 'COMPROMISED'
  | 'DECEASED'
  | 'REDACTED';

export type CharacterDesignation =
  | 'OPERATIVE'
  | 'ASSET'
  | 'CONTACT'
  | 'HANDLER';

export interface Character {
  id: string;
  codename: string;
  real_name: string | null;
  designation: string;
  status: string;
  threat_level: number;
  clearance: string | null;
  file_number: string | null;
  origin: string | null;
  last_known: string | null;
  summary: string | null;
  traits: string[];
  first_seen: string | null;
  sort_index: number;
  created_at: string;
}
