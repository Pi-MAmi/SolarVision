import sqlite3
from pathlib import Path

DB_FILE = Path(__file__).parent / "solar.db"


class Database:

    def __init__(self):

        self.conn = sqlite3.connect(DB_FILE, check_same_thread=False)
        self.conn.row_factory = sqlite3.Row

        self.create()

    def create(self):

        self.conn.execute("""

        CREATE TABLE IF NOT EXISTS live_data(

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

        )

        """)

        self.conn.commit()

    def insert(self, data):

        self.conn.execute("""

        INSERT INTO live_data(

            grid_voltage,
            grid_frequency,

            output_voltage,
            output_frequency,

            output_watt,
            load_percent,

            battery_voltage,
            battery_capacity,

            pv_voltage,
            pv_current,
            pv_power,

            temperature

        )

        VALUES(?,?,?,?,?,?,?,?,?,?,?,?)

        """, (

            data.grid_voltage,
            data.grid_frequency,

            data.output_voltage,
            data.output_frequency,

            data.output_watt,
            data.load_percent,

            data.battery_voltage,
            data.battery_capacity,

            data.pv_voltage,
            data.pv_current,
            data.pv_power,

            data.temperature

        ))

        self.conn.commit()

    def last(self):

        row = self.conn.execute("""

        SELECT *

        FROM live_data

        ORDER BY id DESC

        LIMIT 1

        """).fetchone()

        if row is None:
            return None

        return dict(row)