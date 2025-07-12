from stats import words_in_books, get_book_text, all_char

def main():
  text = get_book_text()
  num_words = words_in_books(text)
  num_letters = all_char(text)
  print(f"{num_words} words found in the document")
  print(num_letters)

main()