def main():
  #Read file
  with open('/Users/rroda/bootdev/github.com/techseito/bookbot/books/frankenstein.txt') as f:
    file_contents = f.read()
    print(file_contents)
    print("End of the book - Frankenstein...")

    #Count the words
    print("Calling words function....")
    words(file_contents)

    #Count the characters
    print("Calling character function...")
    chars(file_contents)

def words(v_str):
    num_words = len(v_str.split())
    #num_words = len(words)
    print(f"Number: {num_words}")

def chars(v_str):
   num_char = {}

   for i in v_str.lower():
      if i in num_char:
        num_char[i] += 1
      else:
         num_char[i] = 1

   for i in num_char:
      print(f"The '{i}' character was found {num_char[i]} times.")



   #print(num_char)

   


      

main()
