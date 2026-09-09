/*
# Create character registry (Digital Archive dossiers)

Purpose
- Backs the "Character Index Registry" section of a cinematic dossier-style
  landing interface. Stores curated, public character dossiers that the
  front-end renders as a state-controlled "Digital Archive".

1. New Tables
- `characters`
  - `id`              uuid, primary key
  - `codename`        text, not null  -> operative handle shown on card
  - `real_name`       text             -> true identity (may be REDACTED in UI)
  - `designation`     text, not null  -> role label (OPERATIVE / ASSET / CONTACT / HANDLER)
  - `status`          text, not null  -> ACTIVE / BURNED / COMPROMISED / DECEASED / REDACTED
  - `threat_level`    int  (1-10)      -> indexed threat metric
  - `clearance`       text             -> e.g. "TIER I".."TIER IV"
  - `file_number`     text, unique     -> archive file id e.g. "AX-4471"
  - `origin`          text             -> place of origin
  - `last_known`      text             -> last known location
  - `summary`         text             -> short dossier brief
  - `traits`          text[]           -> operative trait tags
  - `first_seen`      date             -> first appearance in archive
  - `sort_index`      int              -> manual display ordering
  - `created_at`      timestamptz, default now()

2. Indexes
- `characters_sort_index_idx` on `sort_index` for ordered registry reads.

3. Security
- RLS enabled on `characters`.
- Public/shared archive (no sign-in in this app): anon + authenticated CRUD
  is intentionally allowed because the registry is a curated, shared exhibit.
  SELECT is open; writes are also open so the archive can be maintained.
*/

CREATE TABLE IF NOT EXISTS characters (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  codename text NOT NULL,
  real_name text,
  designation text NOT NULL,
  status text NOT NULL DEFAULT 'ACTIVE',
  threat_level int DEFAULT 5,
  clearance text,
  file_number text UNIQUE,
  origin text,
  last_known text,
  summary text,
  traits text[] DEFAULT '{}',
  first_seen date,
  sort_index int NOT NULL DEFAULT 0,
  created_at timestamptz DEFAULT now()
);

CREATE INDEX IF NOT EXISTS characters_sort_index_idx ON characters (sort_index);

ALTER TABLE characters ENABLE ROW LEVEL SECURITY;

DROP POLICY IF EXISTS "anon_select_characters" ON characters;
CREATE POLICY "anon_select_characters" ON characters FOR SELECT
  TO anon, authenticated USING (true);

DROP POLICY IF EXISTS "anon_insert_characters" ON characters;
CREATE POLICY "anon_insert_characters" ON characters FOR INSERT
  TO anon, authenticated WITH CHECK (true);

DROP POLICY IF EXISTS "anon_update_characters" ON characters;
CREATE POLICY "anon_update_characters" ON characters FOR UPDATE
  TO anon, authenticated USING (true) WITH CHECK (true);

DROP POLICY IF EXISTS "anon_delete_characters" ON characters;
CREATE POLICY "anon_delete_characters" ON characters FOR DELETE
  TO anon, authenticated USING (true);
