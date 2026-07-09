#!/bin/bash

# SolarVision Installer v1.1 (Starter)

set -e

echo "=================================="
echo " SolarVision Installer v1.1"
echo "=================================="

if [ "$EUID" -ne 0 ]; then
  echo "Lütfen sudo ile çalıştırın:"
  echo "sudo ./install.sh"
  exit 1
fi

PROJECT_DIR="$(cd "$(dirname "$0")" && pwd)"

echo "[1/6] Paketler kuruluyor..."
apt update
apt install -y python3 python3-pip python3-venv git nginx sqlite3

echo "[2/6] Virtual environment..."
if [ ! -d "$PROJECT_DIR/venv" ]; then
  python3 -m venv "$PROJECT_DIR/venv"
fi

source "$PROJECT_DIR/venv/bin/activate"

pip install --upgrade pip

if [ -f "$PROJECT_DIR/requirements.txt" ]; then
    pip install -r "$PROJECT_DIR/requirements.txt"
fi

echo "[3/6] Database..."
mkdir -p "$PROJECT_DIR/database"

if [ -f "$PROJECT_DIR/database/schema.sql" ]; then
    sqlite3 "$PROJECT_DIR/database/solar.db" < "$PROJECT_DIR/database/schema.sql"
fi

echo "[4/6] Reloading services..."
systemctl daemon-reload || true

echo "[5/6] Restarting services..."
systemctl restart nginx || true
systemctl restart solarvision-gunicorn || true
systemctl restart solarvision-collector || true

echo "[6/6] Done."

IP=$(hostname -I | awk '{print $1}')

echo
echo "SolarVision hazır."
echo "http://$IP"
