import requests
from bs4 import BeautifulSoup
import smtplib
from email.message import EmailMessage

URL = "https://www.amazon.in/dp/B08N5WRWNW"  # Replace with your product URL
HEADERS = {"User-Agent": "Mozilla/5.0"}

TARGET_PRICE = 55000

EMAIL = "your_email@example.com"
PASSWORD = "your_app_password"
TO = "receiver@example.com"

def get_price():
    page = requests.get(URL, headers=HEADERS)
    soup = BeautifulSoup(page.content, "html.parser")
    price_tag = soup.find('span', {'class': 'a-price-whole'})

    if price_tag:
        price = float(price_tag.text.replace(',', '').replace('₹', '').strip())
        return price
    return None

def send_email(price):
    msg = EmailMessage()
    msg['Subject'] = '📉 Price Drop Alert!'
    msg['From'] = EMAIL
    msg['To'] = TO
    msg.set_content(f"The price dropped to ₹{price}!\nCheck it here: {URL}")

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL, PASSWORD)
        smtp.send_message(msg)
    print("✅ Email sent!")

if __name__ == "__main__":
    price = get_price()
    print(f"Current Price: ₹{price}")
    if price and price < TARGET_PRICE:
        send_email(price)
