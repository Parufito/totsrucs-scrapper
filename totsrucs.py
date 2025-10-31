import requests
from bs4 import BeautifulSoup
import re
import time
import sys
from urllib.parse import urljoin

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}

def get_links_from_table(url):
    try:
        resp = requests.get(url, headers=HEADERS)
        resp.raise_for_status()
    except Exception as e:
        print(f"[ERROR] No s'ha pogut accedir a la pàgina inicial: {e}")
        return []

    soup = BeautifulSoup(resp.text, "html.parser")
    links = []

    tables = soup.find_all("table")
    for table in tables:
        for a in table.find_all("a", href=True):
            full_url = urljoin(url, a["href"])
            links.append(full_url)

    return links

def extract_http_texts_from_page(url):
    try:
        resp = requests.get(url, headers=HEADERS)
        resp.raise_for_status()
        matches = re.findall(r'"(ed2k://[^"]+)"', resp.text)
        return matches
    except Exception as e:
        print(f"[ERROR] No s'ha pogut accedir a {url}: {e}")
        return []

def main(start_url):
    fitxa_links = get_links_from_table(start_url)
    results = {}

    for i, link in enumerate(fitxa_links, 1):
        print(f"\n[{i:02d}] Processant: {link}")
        extracted = extract_http_texts_from_page(link)
        results[link] = extracted

        for j, e in enumerate(extracted, 1):
            print(f"    ({j}) {e}")

        time.sleep(1.5)

    return results

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Ús: python3 totsrucs.py \"https://url-inicial\"")
        sys.exit(1)

    url_inicial = sys.argv[1]
    main(url_inicial)
