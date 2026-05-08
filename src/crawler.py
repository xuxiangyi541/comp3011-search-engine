import requests
from bs4 import BeautifulSoup
import time

BASE_URL = "https://quotes.toscrape.com"

def crawl():
    url = BASE_URL
    pages = {}

    while url:
        print(f"Crawling: {url}")

        try:
            response = requests.get(url)
            response.raise_for_status()
        except Exception as e:
            print(f"Error fetching {url}: {e}")
            break

        soup = BeautifulSoup(response.text, "html.parser")

        quotes = soup.find_all("span", class_="text")
        text_list = [q.get_text() for q in quotes]

        pages[url] = " ".join(text_list)

        # next page
        next_btn = soup.find("li", class_="next")
        if next_btn:
            next_page = next_btn.find("a")["href"]
            url = BASE_URL + next_page
        else:
            url = None

        time.sleep(6)

    return pages


