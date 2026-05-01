#!/bin/bash

# 1. Use the secret GitHub Token to clone your private repo securely
echo "Downloading strategy..."
git clone https://${GITHUB_PAT}@github.com/juand89/RNN.git /app/strategy

# 2. Enter the folder, install dependencies, and run
cd /app/strategy/polymarket_arbitrage_trading
pip install -r requirements.txt
python polymarket_btc_5m_open_strategy.py
