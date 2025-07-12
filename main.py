import sys
from stats import words_in_books, get_book_text, all_char, sort_on

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

path = sys.argv[1]

def main():
    text = get_book_text(path)
    num_words = words_in_books(text)
    num_letters = all_char(text)
    sorted_chars = sort_on(num_letters)

    print("============ BOOKBOT ============")
    print(F"Analyzing book found at {path}...")
    print("------------- Word Count ------------")
    print(f"Found {num_words} total words")
    print("---------- Character Count -----------")

    for item in sorted_chars:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']}")

    print("============ END ============")


main()