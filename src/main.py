from crawler import crawl
from indexer import build_index, save_index, load_index
from search import find, print_word

def main():
    index = None

    while True:
        command = input(">> ").strip()

        if command == "build":
            print("Building index...")
            pages = crawl()
            index = build_index(pages)
            save_index(index)
            print("Index built and saved.")

        elif command == "load":
            try:
                index = load_index()
                print("Index loaded.")
            except:
                print("No index file found. Please run build first.")

        elif command.startswith("print"):
            if index is None:
                print("Please load or build index first.")
                continue

            parts = command.split()
            if len(parts) < 2:
                print("Usage: print <word>")
                continue

            print_word(index, parts[1])

        elif command.startswith("find"):
            if index is None:
                print("Please load or build index first.")
                continue

            parts = command.split()
            if len(parts) < 2:
                print("Usage: find <query>")
                continue

            query = " ".join(parts[1:])
            results = find(index, query)

            if results:
                print(results)
            else:
                print("No results found.")

        elif command == "exit":
            print("Goodbye!")
            break

        else:
            print("Unknown command")

if __name__ == "__main__":
    main()