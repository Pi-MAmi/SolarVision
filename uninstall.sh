#!/bin/bash

#################################################
# SolarVision Uninstaller v1.1
#################################################

set -e

echo "=================================="
echo " SolarVision Uninstaller v1.1"
echo "=================================="

if [ "$EUID" -ne 0 ]; then
  echo "Lütfen sudo ile çalıştırın:"
  echo "sudo ./uninstall.sh"
  exit 1
fi

read -p "SolarVision kaldırılsın mı? (E/h): " ANSWER

case "$ANSWER" in
    E|e|Y|y)
        ;;
    *)
        echo "İşlem iptal edildi."
        exit 0
        ;;
esac

echo "[1/6] Servisler durduruluyor..."
systemctl stop solarvision-collector 2>/dev/null || true
systemctl stop solarvision-gunicorn 2>/dev/null || true

echo "[2/6] Servisler devre dışı bırakılıyor..."
systemctl disable solarvision-collector 2>/dev/null || true
systemctl disable solarvision-gunicorn 2>/dev/null || true

echo "[3/6] Service dosyaları siliniyor..."
rm -f /etc/systemd/system/solarvision-collector.service
rm -f /etc/systemd/system/solarvision-gunicorn.service

systemctl daemon-reload

echo "[4/6] Nginx yapılandırması kaldırılıyor..."
rm -f /etc/nginx/sites-enabled/solarvision
rm -f /etc/nginx/sites-available/solarvision

systemctl restart nginx 2>/dev/null || true

echo "[5/6] Proje dosyaları korunuyor."
echo "SolarVision klasörü silinmedi."

echo "[6/6] Tamamlandı."

echo
echo "SolarVision sistem servisleri kaldırıldı."
echo "Projeyi tamamen silmek istersen:"
echo
echo "rm -rf $(pwd)"
