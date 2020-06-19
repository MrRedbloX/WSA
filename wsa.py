import sys
from time import perf_counter

from py.utils import params_to_obj
from py.keywords import init_keywords
from py.web import init_webpages
from py.sentiment import compute_sentiment, get_sentiment_score

def wsa(topic, language="en", num=10):
    return get_sentiment_score(compute_sentiment(init_keywords(language), init_webpages(topic, language, num)))

if __name__ == "__main__":
    params = params_to_obj(sys.argv[1:])
    try:
        topic = params["topic"]
        t = perf_counter()
        print(f"WSA score: {wsa(topic):.2f} in {(perf_counter() - t):.2f} sec.")
    except KeyError:
        print("usage: python main.py topic=<your topic>")
