<p align="center">

# ☀️ SolarVision

### Professional Solar Inverter Monitoring Platform



</p>

---

## About

SolarVision is an open-source monitoring platform developed for Raspberry Pi.

It communicates with TommaTech PI30 (Voltronic compatible) solar inverters via USB HID, collects real-time operating data, stores it in SQLite and presents everything through a modern responsive web dashboard.

Designed to be lightweight, fast and suitable for 24/7 operation.

---

## Features

- ☀️ Live Solar Production
- 🔋 Battery Monitoring
- ⚡ Grid Monitoring
- 🔌 Output Monitoring
- 📊 Historical PV Charts
- 🌤 Weather Integration
- ⚙️ Settings Panel
- 📱 Responsive Interface
- 💻 System Monitoring
- 🌐 Tailscale Remote Access
- 🚧 Progressive Web App (PWA)

...

<p align="center">

# ☀️ SolarVision

### Raspberry Pi için Profesyonel Solar İnverter İzleme Platformu


</p>

---

## Hakkında

SolarVision, Raspberry Pi üzerinde çalışan açık kaynaklı bir güneş enerjisi izleme platformudur.

TommaTech PI30 (Voltronic uyumlu) inverterlerle USB HID üzerinden haberleşerek gerçek zamanlı verileri toplar, SQLite veritabanında saklar ve modern bir web arayüzü üzerinden kullanıcıya sunar.

Hafif, hızlı ve 7/24 çalışacak şekilde tasarlanmıştır.

---

## Özellikler

- ☀️ Canlı PV Gücü
- 🔋 Batarya İzleme
- ⚡ Şebeke İzleme
- 🔌 Çıkış Gücü
- 📊 Geçmiş Grafikler
- 🌤 Hava Durumu
- ⚙️ Ayarlar Paneli
- 📱 Mobil Uyumlu Arayüz
- 💻 Sistem Bilgisi
- 🌐 Tailscale Uzaktan Erişim
- 🚧 PWA Altyapısı

---

## Desteklenen Donanım

| Donanım | Durum |
|----------|--------|
| Raspberry Pi Zero W | ✅ |
| Raspberry Pi OS Bookworm Lite | ✅ |
| TommaTech PI30 | ✅ |
| USB HID (0665:5161) | ✅ |

---

## Kurulum

```bash
git clone https://github.com/Pi-MAmi/SolarVision.git

cd SolarVision

python3 -m venv venv

source venv/bin/activate

pip install -r requirements.txt

python app.py
