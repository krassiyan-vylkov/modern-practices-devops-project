CREATE TABLE operators (
  id SERIAL PRIMARY KEY,
  name TEXT NOT NULL,
  attack INTEGER,
  damage_type TEXT
);

CREATE TABLE bosses (
  id SERIAL PRIMARY KEY,
  name TEXT NOT NULL,
  defense INTEGER,
  resistance INTEGER
);