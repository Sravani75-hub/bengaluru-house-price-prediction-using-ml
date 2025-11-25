#!/bin/bash
set -e

echo "📥 Installing gdown..."
pip3 install gdown

echo "📁 Creating models directory..."
mkdir -p models

echo "⬇️ Downloading best_model.pkl..."
gdown --id 1558gV_3VP181uLkp6Kl936xIjZkvUqbG -O models/best_model.pkl

echo "⬇️ Downloading scaler.pkl..."
gdown --id 1aSUzcBE-e4t32YeD-_1O2sQmGvJADEKG -O models/scaler.pkl

echo "✅ Model files downloaded successfully!"
