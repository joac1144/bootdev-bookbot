import sys

from stats import count_words, count_symbols, sorted_count_symbols

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book = sys.argv[1]
    book_text = get_book_text(book)
    num_words = count_words(book_text)
    symbols = sorted_count_symbols(count_symbols(book_text))

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for dict in symbols:
        char = dict["char"]
        if char.isalpha():
            print(f"{char}: {dict["num"]}")
    print("============= END ===============")


def get_book_text(filepath: str):
    with open(filepath) as file:
        return file.read()

if __name__ == "__main__":
    main()