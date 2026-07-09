# SolarVision

## Türkçe Dokümantasyon

SolarVision, Raspberry Pi üzerinde çalışan açık kaynaklı bir güneş enerjisi izleme sistemidir.

### Özellikler

- USB HID destekli TommaTech inverter
- Flask tabanlı web arayüzü
- Mobil uyumlu (Responsive)
- PWA desteği
- SQLite veritabanı
- Hava durumu entegrasyonu
- Gerçek zamanlı grafikler
- Tailscale ile uzaktan erişim

## Gereksinimler

- Raspberry Pi OS Bookworm
- Python 3.11+
- Nginx
- Gunicorn
- USB HID destekli inverter

## Kurulum

```bash
git clone https://github.com/Pi-MAmi/SolarVision.git
cd SolarVision
chmod +x install.sh
sudo ./install.sh
```

Kurulum tamamlandıktan sonra tarayıcıdan:

```
http://RASPBERRY_PI_IP
```

adresini açın.

## Güncelleme

```bash
sudo ./update.sh
```

## Kaldırma

```bash
sudo ./uninstall.sh
```

## Varsayılan Dizin Yapısı

```
SolarVision/
├── app.py
├── collector.py
├── database/
├── inverter/
├── services/
├── nginx/
├── static/
├── templates/
└── install.sh
```

## Lisans

MIT License

## Geliştirici

Muhammed Mert Tayyeli

GitHub:
https://github.com/Pi-MAmi/SolarVision
