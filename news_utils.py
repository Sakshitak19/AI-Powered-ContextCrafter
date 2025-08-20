import requests
from bs4 import BeautifulSoup

def extract_text_from_links(urls):
    texts = []
    for url in urls:
        try:
            res = requests.get(url, timeout=10)
            soup = BeautifulSoup(res.text, 'html.parser')
            paragraphs = [p.get_text() for p in soup.find_all('p')]
            article_text = "\n".join(paragraphs[:20])  # Limit to first 20 paragraphs
            texts.append(article_text)
        except Exception as e:
            texts.append(f"[Error extracting from {url}]: {str(e)}")
    return texts
