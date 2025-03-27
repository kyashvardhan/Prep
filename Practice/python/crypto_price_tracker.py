import requests
import time
import logging

API_URL = "https://api.coingecko.com/api/v3/simple/price"
TOKEN = "your_telegram_bot_token"
CHAT_ID = "your_chat_id"
CRYPTOCURRENCIES = ["bitcoin", "ethereum", "dogecoin"]

logging.basicConfig(level=logging.INFO)

def get_crypto_prices(cryptos):
    params = {'ids': ','.join(cryptos), 'vs_currencies': 'usd'}
    response = requests.get(API_URL, params=params)
    response.raise_for_status()
    return response.json()

def send_telegram_message(message):
    telegram_url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {'chat_id': CHAT_ID, 'text': message}
    requests.post(telegram_url, json=payload)

def format_prices(prices):
    return "\n".join([f"{crypto.title()}: ${prices[crypto]['usd']}" for crypto in prices])

if __name__ == "__main__":
    previous_prices = {}
    while True:
        try:
            current_prices = get_crypto_prices(CRYPTOCURRENCIES)
            if current_prices != previous_prices:
                message = "📈 Crypto Prices Update:\n" + format_prices(current_prices)
                send_telegram_message(message)
                logging.info("Prices updated and notification sent.")
                previous_prices = current_prices
            time.sleep(300)  # 5-minute interval
        except Exception as e:
            logging.error(f"Error: {e}")
            time.sleep(60)
