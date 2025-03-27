import requests
from bs4 import BeautifulSoup
import csv

def scrape_quotes(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    quotes_data = []
    quotes = soup.find_all('div', class_='quote')

    for quote in quotes:
        text = quote.find('span', class_='text').get_text()
        author = quote.find('small', class_='author').get_text()
        tags = [tag.get_text() for tag in quote.find_all('a', class_='tag')]
        quotes_data.append([text, author, ', '.join(tags)])

    return quotes_data

def save_to_csv(data, filename='quotes.csv'):
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Quote", "Author", "Tags"])
        writer.writerows(data)

if __name__ == "__main__":
    url = "http://quotes.toscrape.com"
    quotes = scrape_quotes(url)
    save_to_csv(quotes)
    print(f"Saved {len(quotes)} quotes to quotes.csv")
