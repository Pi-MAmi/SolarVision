PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS live_data (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,

    grid_voltage REAL,
    grid_frequency REAL,

    output_voltage REAL,
    output_frequency REAL,

    output_watt INTEGER,
    load_percent INTEGER,

    battery_voltage REAL,
    battery_capacity INTEGER,

    pv_voltage REAL,
    pv_current REAL,
    pv_power INTEGER,

    temperature REAL
);

CREATE INDEX IF NOT EXISTS idx_live_timestamp
ON live_data(timestamp);

CREATE TABLE IF NOT EXISTS settings (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    key TEXT UNIQUE NOT NULL,
    value TEXT
);

INSERT OR IGNORE INTO settings(key,value) VALUES
('city','Bursa'),
('refresh_interval','5'),
('electric_price','3.24'),
('theme','dark');

CREATE TABLE IF NOT EXISTS daily_energy (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    day TEXT UNIQUE,
    energy_kwh REAL DEFAULT 0,
    income REAL DEFAULT 0
);

CREATE TABLE IF NOT EXISTS alarms (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    level TEXT,
    title TEXT,
    message TEXT,
    acknowledged INTEGER DEFAULT 0
);

CREATE TABLE IF NOT EXISTS inverter_info (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    model TEXT,
    protocol TEXT,
    serial TEXT,
    firmware TEXT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);
