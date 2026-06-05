#!/bin/bash
set -e

echo "Creating virtual environment..."
python3 -m venv .venv

echo "Installing dependencies..."
.venv/bin/pip install -r requirements.txt

echo "Seeding database..."
.venv/bin/python scripts/seed_data.py

echo "Setup complete!"
echo "To start the server, run: source .venv/bin/activate && uvicorn app.main:app --reload"
