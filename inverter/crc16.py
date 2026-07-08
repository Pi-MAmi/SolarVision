# inverter/crc16.py

POLY = 0x1021


def crc16(data: bytes) -> bytes:

    crc = 0

    for b in data:

        crc ^= (b << 8)

        for _ in range(8):

            if crc & 0x8000:
                crc = (crc << 1) ^ POLY
            else:
                crc <<= 1

            crc &= 0xFFFF

    return bytes([crc >> 8, crc & 0xFF])