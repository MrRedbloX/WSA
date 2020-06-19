from multiprocessing import Pool, cpu_count

def compute_sentiment(keywords, pages):
    sentiment = {}
    positives = keywords["positive"]
    negatives = keywords["negative"]

    for page in pages:
        name = page["name"]
        content = page["string"]
        sentiment[name] = create_pool(positives, content) / len(positives) - create_pool(negatives, content) / len(negatives)

    return sentiment

def get_sentiment_score(sentiment):
    total_score = 0
    pages = sentiment.keys()

    for page in pages:
        total_score += sentiment[page]

    return total_score / len(pages)

def create_pool(words, content):
    pool = Pool(cpu_count())
    results = [pool.apply_async(count_occurrences, args=(word, content)) for word in words]
    output = [p.get() for p in results]

    pool.close()
    pool.join()

    return sum(output)

def count_occurrences(word, content):
    return content.count(word)
