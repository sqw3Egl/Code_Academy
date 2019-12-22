def contains(big_string, little_string):
  return little_string in big_string

def common_letters(string_one, string_two):
  new_string = []
  for character in string_one:
    if character in string_two:
      if character not in new_string:
        new_string.append(character)
  return new_string

print(common_letters('manhattan', 'san fransisco'))