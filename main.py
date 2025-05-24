import yfinance as yf
from twilio.rest import Client
import config

# Define a dictionary with stock symbols and their respective threshold prices
stock_thresholds = {
    "AAPL": 190.00,
    "GOOGL": 130.00,
    "MSFT": 320.00
}

# Set up Twilio client
client = Client(config.account_sid, config.auth_token)

# Loop through each stock and send alert if condition is met
for symbol, threshold in stock_thresholds.items():
    stock = yf.Ticker(symbol)
    stock_price = stock.history(period="1d")['Close'].iloc[-1]

    print(f"Current price of {symbol}: ${stock_price:.2f}")

    if stock_price > threshold:
        message_body = f"Stock Alert: {symbol} is trading at ${stock_price:.2f}, which is above your threshold of ${threshold}."
        message = client.messages.create(
            body=message_body,
            from_=config.from_whatsapp_number,
            to=config.to_whatsapp_number
        )
        print(f"WhatsApp alert sent for {symbol}")
    else:
        print(f"{symbol} price is below ${threshold}")

    print("---")