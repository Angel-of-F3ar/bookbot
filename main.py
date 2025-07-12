from stats import words_in_books, get_book_text

def main():
  text = get_book_text()
  num_words = words_in_books(text)
  print(f"{num_words} words found in the document")

main()