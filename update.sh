#!/bin/bash

#################################################
# SolarVision Update Script v1.1
#################################################

set -e

PROJECT_DIR="$(cd "$(dirname "$0")" && pwd)"

echo "=================================="
echo " SolarVision Updater v1.1"
echo "=================================="

if [ "$EUID" -ne 0 ]; then
  echo "Lütfen sudo ile çalıştırın:"
  echo "sudo ./update.sh"
  exit 1
fi

cd "$PROJECT_DIR"

echo "[1/7] GitHub'dan güncelleniyor..."
git pull

echo "[2/7] Virtual environment..."
if [ ! -d venv ]; then
    python3 -m venv venv
fi

source venv/bin/activate

echo "[3/7] Pip güncelleniyor..."
python -m pip install --upgrade pip

echo "[4/7] Python paketleri kuruluyor..."
if [ -f requirements.txt ]; then
    pip install -r requirements.txt
fi

echo "[5/7] Database güncelleniyor..."
if [ -f database/schema.sql ]; then
    sqlite3 database/solar.db < database/schema.sql || true
fi

echo "[6/7] Servisler yeniden başlatılıyor..."
systemctl restart solarvision-collector || true
systemctl restart solarvision-gunicorn || true
systemctl restart nginx || true

echo "[7/7] Durum"

systemctl --no-pager --full status solarvision-collector | head -n 5 || true
systemctl --no-pager --full status solarvision-gunicorn | head -n 5 || true

echo
echo "SolarVision başarıyla güncellendi."
