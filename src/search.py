def print_word(index, word):
    word = word.lower()
    if word in index:
        print(index[word])
    else:
        print("Word not found")


def find(index, query):
    words = query.lower().split()

    results = None

    for word in words:
        if word not in index:
            return []

        urls = set(index[word].keys())

        if results is None:
            results = urls
        else:
            results = results.intersection(urls)

    return list(results)


if __name__ == "__main__":
    from crawler import crawl
    from indexer import build_index

    pages = crawl()
    index = build_index(pages)

    print(find(index, "life"))
    print(find(index, "good friends"))