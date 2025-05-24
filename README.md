# Stock Alert WhatsApp Bot 📈

This Python-based bot monitors real-time stock prices and sends WhatsApp alerts if the price crosses user-defined thresholds.

## Features
- Real-time stock price fetching using yfinance
- WhatsApp alerts powered by Twilio
- Configurable thresholds per stock

## How it Works
1. Fetches latest closing price of given stocks
2. Compares price to user-defined threshold
3. Sends WhatsApp alert if threshold is crossed

## Setup Instructions
1. Clone this repo
2. Create a `config.py` with your Twilio credentials
3. Run `pip install -r requirements.txt`
4. Execute `main.py`

## Example Output
Current price of AAPL: $195.27
WhatsApp alert sent for AAPL
