import time
import hid

from inverter.crc16 import crc16


class Inverter:

    VID = 0x0665
    PID = 0x5161

    def __init__(self):
        self.dev = hid.Device(vid=self.VID, pid=self.PID)

    def send(self, command: str):

        cmd = command.encode()

        packet = cmd + crc16(cmd) + b"\r"

        # Debug için istersen açabilirsin
        # print("TX:", (b"\x00" + packet).hex())

        self.dev.write(b"\x00" + packet)

        time.sleep(0.1)

        data = bytearray()

        while True:

            chunk = self.dev.read(8, timeout=1000)

            if not chunk:
                break

            data.extend(chunk)

            # Debug için istersen açabilirsin
            # print("RX:", bytes(data).hex())

            if 0x0D in chunk:
                break

        return bytes(data)

    def qpi(self):
        return self.send("QPI")

    def qpigs(self):
        return self.send("QPIGS")

    def qpiri(self):
        return self.send("QPIRI")

    def qmod(self):
        return self.send("QMOD")

    def qflag(self):
        return self.send("QFLAG")

    def qid(self):
        return self.send("QID")

    def close(self):
        self.dev.close()


if __name__ == "__main__":

    inv = Inverter()

    try:

        print("QPI   :", inv.qpi())
        print("QPIGS :", inv.qpigs())

    finally:

        inv.close()