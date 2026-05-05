import json
import os

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



def save_index(index):
    os.makedirs("data", exist_ok=True)
    with open("data/index.json", "w", encoding="utf-8") as f:
        json.dump(index, f)
    print("Index saved to data/index.json")


def load_index():
    with open("data/index.json", "r", encoding="utf-8") as f:
        index = json.load(f)
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