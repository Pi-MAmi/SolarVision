import os
import shutil
import subprocess
import platform
from pathlib import Path

DB_FILE = Path("database") / "solar.db"


def service_status(service):

    systemctl = shutil.which("systemctl")

    if systemctl is None:

        for path in (
            "/usr/bin/systemctl",
            "/bin/systemctl"
        ):
            if os.path.exists(path):
                systemctl = path
                break

    if systemctl is None:
        return "systemctl not found"

    try:

        result = subprocess.run(
            [systemctl, "is-active", service],
            capture_output=True,
            text=True,
            timeout=5
        )

        return result.stdout.strip() or result.stderr.strip()

    except Exception as e:

        return str(e)


def cpu_temperature():

    try:

        with open("/sys/class/thermal/thermal_zone0/temp") as f:

            temp = float(f.read()) / 1000

        return round(temp, 1)

    except Exception:

        return 0.0


def memory_usage():

    try:

        with open("/proc/meminfo") as f:

            lines = f.readlines()

        total = int(lines[0].split()[1])
        available = int(lines[2].split()[1])

        used = total - available

        return round((used / total) * 100, 1)

    except Exception:

        return 0


def disk_usage():

    total, used, free = shutil.disk_usage("/")

    return {

        "total": round(total / (1024**3), 1),
        "used": round(used / (1024**3), 1),
        "free": round(free / (1024**3), 1),
        "percent": round((used / total) * 100, 1)

    }


def database_size():

    if DB_FILE.exists():

        size = DB_FILE.stat().st_size

        return round(size / (1024 * 1024), 2)

    return 0


def uptime():

    try:

        with open("/proc/uptime") as f:

            seconds = float(f.readline().split()[0])

        days = int(seconds // 86400)
        hours = int((seconds % 86400) // 3600)
        minutes = int((seconds % 3600) // 60)

        return f"{days} Gun {hours} Saat {minutes} Dakika"

    except Exception:

        return "-"


def info():

    disk = disk_usage()

    return {

        "version": "v1.3",

        "python": platform.python_version(),

        "collector": service_status("solarvision-collector"),

        "gunicorn": service_status("solarvision-gunicorn"),

        "nginx": service_status("nginx"),

        "database": database_size(),

        "cpu_temp": cpu_temperature(),

        "memory": memory_usage(),

        "disk": disk["percent"],

        "uptime": uptime()

    }


if __name__ == "__main__":

    from pprint import pprint

    pprint(info())