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

        packet = b"\x00" + cmd + crc16(cmd) + b"\r"
        #print("TX:", packet.hex())

        self.dev.write(packet)

        time.sleep(0.5)

        data = bytearray()

        while True:

            chunk = self.dev.read(8, timeout=1000)

            if not chunk:
                break

            data.extend(chunk)

            if 0x0D in chunk:
                break
            #print("RX:", bytes(data).hex())

        return bytes(data)

    def close(self):
        self.dev.close()


if __name__ == "__main__":

    inv = Inverter()

    try:

        print("QPI   :", inv.send("QPI"))
        print("QPIGS :", inv.send("QPIGS"))

    finally:

        inv.close()