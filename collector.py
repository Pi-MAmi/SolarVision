import time

from inverter.reader import Inverter
from inverter.parser import parse_qpigs
from database.database import Database


def main():

    inverter = Inverter()
    db = Database()

    print("SolarVision Collector başlatıldı.")

    try:

        while True:

            raw = inverter.qpigs()

            data = parse_qpigs(raw)

            db.insert(data)

            print(
                f"PV:{data.pv_power}W | "
                f"Batarya:{data.battery_voltage:.2f}V | "
                f"%{data.battery_capacity}"
            )

            time.sleep(2)

    except KeyboardInterrupt:

        print("\nCollector durduruldu.")

    finally:

        inverter.close()


if __name__ == "__main__":

    main()