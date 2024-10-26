# /Users/rroda/workspace/github.com/techseito/bookbot/books/frankenstein.txt

def main():
    book_path = "/Users/rroda/workspace/github.com/techseito/bookbot/books/frankenstein.txt"
    text = get_book_text(book_path)
    print(text)
    cwords = count_words(text)
    print(f"Word count: {cwords}")
    cchars = count_characters(text)
    #cchars.sort(reverse=True,key=sort_on)
    print(cchars)
    for i in cchars:
       #print(i)
       print(f"The {i} character was found {cchars[i]} times")
    #print(f"Character count: {cchars}")
    
#def sort_on(dict)
#   return dict[]

def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    words = text.split()
    i = 0
    for word in words:
        i += 1
    return i

def count_characters(text):
    words = text.lower()
    counter = {}
    #print(words)
    for i in words:
      #print(f"i: {i}")
      if i not in counter:
        counter[i] = 1
      else:
      	counter[i] += 1
    return counter

main()
