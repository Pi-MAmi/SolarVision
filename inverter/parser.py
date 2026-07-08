from dataclasses import dataclass


@dataclass
class LiveData:

    grid_voltage: float
    grid_frequency: float

    output_voltage: float
    output_frequency: float

    output_watt: int
    load_percent: int

    battery_voltage: float
    battery_capacity: int

    pv_voltage: float
    pv_current: float
    pv_power: int

    temperature: float


def parse_qpigs(raw: bytes) -> LiveData:

    text = raw.decode(errors="ignore")

    text = text.strip("\r\n\x00")

    if text.startswith("("):
        text = text[1:]

    parts = text.split()

    return LiveData(

        grid_voltage=float(parts[0]),
        grid_frequency=float(parts[1]),

        output_voltage=float(parts[2]),
        output_frequency=float(parts[3]),

        output_watt=int(parts[4]),
        load_percent=int(parts[6]),

        battery_voltage=float(parts[8]),
        battery_capacity=int(parts[10]),

        pv_voltage=float(parts[13]),
        pv_current=float(parts[9]),

        pv_power=int(parts[19]),

        temperature=float(parts[11]) / 10

    )


if __name__ == "__main__":

    from inverter.reader import Inverter

    inv = Inverter()

    try:

        raw = inv.qpigs()

        print(raw)
        print()

        data = parse_qpigs(raw)

        print("Grid Voltage      :", data.grid_voltage)
        print("Grid Frequency    :", data.grid_frequency)
        print("Output Voltage    :", data.output_voltage)
        print("Output Frequency  :", data.output_frequency)
        print("Output Watt       :", data.output_watt)
        print("Load              :", data.load_percent)
        print("Battery Voltage   :", data.battery_voltage)
        print("Battery Capacity  :", data.battery_capacity)
        print("PV Voltage        :", data.pv_voltage)
        print("PV Current        :", data.pv_current)
        print("PV Power          :", data.pv_power)
        print("Temperature       :", data.temperature)

    finally:

        inv.close()