def main():
  book_path = "books/frankenstein.txt"
  book_text  = get_book_test(book_path)
  words_count = get_words_count(book_text)
  char_count = get_char_count(book_text)

  print(f"--- Begin report of {book_path} ---")
  print(f"{words_count} words found in the document")
  for key in char_count:
    if not key.isalpha():
            continue
    print(f"The {key} character was found {char_count[key]} times")
  print("--- End report ---")


def get_book_test(path):
  with open(path) as f:
    return f.read()

def get_words_count(book_text):
  words = book_text.split()
  return len(words)

def get_char_count(book_text):
  char_count = {}
  for ch in book_text:
    l_ch = ch.lower()
    if  l_ch in char_count:
      char_count[l_ch] += 1
    else:
      char_count[l_ch] = 1

  return char_count
main()
