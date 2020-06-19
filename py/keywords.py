from pathlib import Path, PurePath

path = Path(__file__).parent.parent.absolute()

def init_keywords(language):
    return {
        "positive": get_words(language, "positive"),
        "negative": get_words(language, "negative")
    }

def get_words(language, type):
    with open(PurePath(path, "res", language, type)) as f:
        return [word for word in f.read().split('\n') if word != ""]
