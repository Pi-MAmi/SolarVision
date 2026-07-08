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

        self.conn.execute("""

        CREATE TABLE IF NOT EXISTS settings(

            key TEXT PRIMARY KEY,

            value TEXT

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

    def today_energy(self):

        rows = self.conn.execute("""

        SELECT pv_power

        FROM live_data

        WHERE date(timestamp)=date('now','localtime')

        ORDER BY timestamp ASC

        """).fetchall()

        if len(rows) < 2:
            return 0.0

        interval = 2

        energy_wh = 0.0

        for row in rows:
            energy_wh += row["pv_power"] * interval / 3600

        return round(energy_wh / 1000, 3)

    def today_income(self):

        price = float(self.get_setting("electric_price", "3.24"))

        return round(self.today_energy() * price, 2)

    def today_stats(self):

        return {

            "today_energy": self.today_energy(),

            "today_income": self.today_income()

        }

    def history(self, limit=720):

        rows = self.conn.execute("""

        SELECT

            timestamp,
            pv_power,
            battery_voltage,
            output_watt,
            temperature

        FROM live_data

        ORDER BY id DESC

        LIMIT ?

        """, (limit,)).fetchall()

        result = []

        for row in reversed(rows):
            result.append(dict(row))

        return result

    # -----------------------------
    # SETTINGS
    # -----------------------------

    def get_setting(self, key, default=""):

        row = self.conn.execute(

            "SELECT value FROM settings WHERE key=?",

            (key,)

        ).fetchone()

        if row:
            return row["value"]

        return default

    def set_setting(self, key, value):

        self.conn.execute("""

        INSERT INTO settings(key,value)

        VALUES(?,?)

        ON CONFLICT(key)

        DO UPDATE SET value=excluded.value

        """, (key, str(value)))

        self.conn.commit()

    def settings(self):

        return {

            "city": self.get_setting("city", "Bursa"),

            "electric_price": self.get_setting("electric_price", "3.24"),

            "refresh": self.get_setting("refresh", "5")

        }