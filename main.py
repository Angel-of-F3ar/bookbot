from stats import words_in_books, get_book_text, all_char, sort_on

def main():
    text = get_book_text()
    num_words = words_in_books(text)
    num_letters = all_char(text)
    sorted_chars = sort_on(num_letters)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("------------- Word Count ------------")
    print(f"Found {num_words} total words")
    print("---------- Character Count -----------")

    for item in sorted_chars:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']}")

    print("============ END ============")


main()