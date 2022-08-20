CREATE SCHEMA IF NOT EXISTS workflows;

CREATE TABLE IF NOT EXISTS workflows.settings (
  id INT GENERATED BY DEFAULT AS IDENTITY,
  name VARCHAR (255) UNIQUE NOT NULL,
  value VARCHAR (255) NOT NULL
);

CREATE TABLE IF NOT EXISTS workflows.fls_events (
  event_ts TIMESTAMP NOT NULL,
  event_location VARCHAR(255) NOT NULL,
  home_team VARCHAR(50) NOT NULL,
  away_team VARCHAR(50) NOT NULL
);

CREATE TABLE workflows.english_learning (
  event_id VARCHAR(50) UNIQUE NOT NULL,
  task_id VARCHAR(50) UNIQUE NOT NULL,
  task_status VARCHAR(50) NOT NULL,
  task_priority INT NOT NULL,
  event_ts TIMESTAMP NOT NULL
)