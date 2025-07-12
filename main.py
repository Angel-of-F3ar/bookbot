def get_book_text():
  with open("books/frankenstein.txt") as f:
    return f.read()

def words_in_books(words):
  num_of_words = len(words.split())
  return num_of_words
  
def main():
  text = get_book_text()
  num_words = words_in_books(text)
  print(f"{num_words} words found in the document")

main()