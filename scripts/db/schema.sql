-- 「최고의 공부」 영상 데이터베이스 (SQLite). 기술지원팀 관리.
CREATE TABLE IF NOT EXISTS concepts (
  id           INTEGER PRIMARY KEY,
  name         TEXT NOT NULL UNIQUE,      -- 개념 이름 (예: 근의 공식)
  subject      TEXT NOT NULL,             -- 수학/물리/화학/생명/지구/유체역학/전기/기계/전자
  level        TEXT NOT NULL,             -- middle / high / univ
  curriculum   TEXT,                      -- 교육과정 위치
  prerequisites TEXT                      -- 선수 개념 (쉼표 구분)
);

CREATE TABLE IF NOT EXISTS episodes (
  id           INTEGER PRIMARY KEY,
  concept_id   INTEGER NOT NULL REFERENCES concepts(id),
  made_on      TEXT NOT NULL,             -- YYYY-MM-DD
  slug         TEXT NOT NULL UNIQUE,      -- 폴더 이름
  title        TEXT NOT NULL,
  duration_sec REAL,
  status       TEXT NOT NULL,             -- 기획/검토/제작/승인대기/공개/보류
  folder       TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS legal_reviews (
  id           INTEGER PRIMARY KEY,
  episode_id   INTEGER NOT NULL REFERENCES episodes(id),
  round        INTEGER NOT NULL,          -- 1: 대본, 2: 완성 영상
  verdict      TEXT NOT NULL,             -- 통과/조건부 통과/보류
  reviewed_on  TEXT NOT NULL,
  notes        TEXT,
  UNIQUE (episode_id, round)
);

CREATE TABLE IF NOT EXISTS assets (
  id           INTEGER PRIMARY KEY,
  episode_id   INTEGER NOT NULL REFERENCES episodes(id),
  type         TEXT NOT NULL,
  files        TEXT,
  source       TEXT,
  author       TEXT,
  license      TEXT
);

CREATE TABLE IF NOT EXISTS distributions (
  id           INTEGER PRIMARY KEY,
  episode_id   INTEGER NOT NULL REFERENCES episodes(id),
  platform     TEXT NOT NULL,
  url          TEXT,
  uploaded_at  TEXT,
  visibility   TEXT                       -- private/unlisted/public/scheduled
);
