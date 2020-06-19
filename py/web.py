from googlesearch import search
from requests import get as rget

def init_webpages(topic, language, num):
    pages = []
    for page in search(topic, stop=num, pause=2, lang=language):
        try:
            text = rget(page).text
            pages.append({
                "name": page,
                "string": text
            })
        except:
            print(f"Skipping {page}")

    return pages
