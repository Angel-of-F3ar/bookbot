
def get_book_text(path):
  with open(path) as f:
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

def sort_by_num(item):
  return item["num"]

def sort_on(char_dict):
  report = []
  for char, num in char_dict.items():
    report.append({"char": char, "num": num})
  report.sort(key=sort_by_num, reverse = True)
  return report