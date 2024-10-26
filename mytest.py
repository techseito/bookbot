def add_dict(string):
  print(string)
  string_counter = {}
  for i in string:
    print(f"i: {i}")
    if i not in string_counter:
      string_counter[i] = 1
    else:
      string_counter[i] += 1
  print(string_counter)
  

string="philippines"
add_dict(string)