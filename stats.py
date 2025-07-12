def get_book_text():
  with open("books/frankenstein.txt") as f:
    return f.read()

def words_in_books(words):
  num_of_words = len(words.split())
  return num_of_words

def all_char(words):
  chars = {}
  for char in words:
    low_char = char.lower()
    if low_char in chars:
      #update count
      chars[low_char] += 1
    else:
      chars[low_char] = 1
  return chars