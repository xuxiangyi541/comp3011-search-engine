def tokenize(text):
    return text.lower().split()


def build_index(pages):
    index = {}

    for url, text in pages.items():
        words = tokenize(text)

        for pos, word in enumerate(words):
            if word not in index:
                index[word] = {}

            if url not in index[word]:
                index[word][url] = []

            index[word][url].append(pos)

    return index



if __name__ == "__main__":
    from crawler import crawl

    pages = crawl()
    index = build_index(pages)

    print("Total words:", len(index))

    for i, (word, data) in enumerate(index.items()):
        print(word, "->", data)
        if i == 5:
            break