# SolarVision

Open-source solar inverter monitoring platform for Raspberry Pi.

## Features

- USB HID communication
- TommaTech inverter support
- Flask web dashboard
- Responsive mobile interface
- Progressive Web App (PWA)
- SQLite database
- Weather integration
- Real-time charts
- Nginx + Gunicorn deployment
- Tailscale remote access ready

## Requirements

- Raspberry Pi OS Bookworm
- Python 3.11+
- Nginx
- Gunicorn

## Installation

```bash
git clone https://github.com/Pi-MAmi/SolarVision.git
cd SolarVision
chmod +x install.sh
sudo ./install.sh
```

Open your browser:

```
http://RASPBERRY_PI_IP
```

## Update

```bash
sudo ./update.sh
```

## Uninstall

```bash
sudo ./uninstall.sh
```

## Project Structure

```
SolarVision/
├── app.py
├── collector.py
├── config.py
├── database/
├── inverter/
├── nginx/
├── services/
├── static/
├── templates/
├── install.sh
├── update.sh
└── uninstall.sh
```

## Roadmap

- Multi-inverter support
- MQTT integration
- Docker deployment
- Home Assistant integration
- PostgreSQL support
- Plugin system

## License

MIT License

## Author

Muhammed Mert Tayyeli

GitHub:
https://github.com/Pi-MAmi/SolarVision
