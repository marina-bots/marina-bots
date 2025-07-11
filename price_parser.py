import requests
from bs4 import BeautifulSoup

def get_price(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Здесь пример для сайта с классом цены 'price-tag', нужно заменить под реальный сайт
    price_tag = soup.find(class_='price-tag')
    if price_tag:
        return price_tag.text.strip()
    else:
        return "Цена не найдена"

if __name__ == "__main__":
    url = 'https://example.com/product'
    print(f"Цена товара: {get_price(url)}")
