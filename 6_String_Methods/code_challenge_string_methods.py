letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
# Write your unique_english_letters function here:

def unique_english_letters(word):
  counter = 0
  for i in letters:
    if i in word:
      counter += 1
  return counter
    

# Uncomment these function calls to test your function:
print(unique_english_letters("mississippi"))
# should print 4
print(unique_english_letters("Apple"))
# should print 4

##############################################

# Write your count_char_x function here:

def count_char_x(word, x):
  count = 0
  for i in word:
    if i == x:
      count += 1
  return count
    

# Uncomment these function calls to test your tip function:
print(count_char_x("mississippi", "s"))
# should print 4
print(count_char_x("mississippi", "m"))
# should print 1

################################################

# Write your count_multi_char_x function here:

def count_multi_char_x(word, x):
  return word.count(x)

# Uncomment these function calls to test your function:
print(count_multi_char_x("mississippi", "iss"))
# should print 2
print(count_multi_char_x("apple", "pp"))
# should print 1

######################################################

# Write your substring_between_letters function here:

def substring_between_letters(word, start, end):
  s = word.find(start)
  e = word.find(end)
  if s == -1:
    return word
  if e == -1:
    return word
  else:
    return word[(s +1):e]
  
# Uncomment these function calls to test your function:
print(substring_between_letters("apple", "p", "e"))
# should print "pl"
print(substring_between_letters("apple", "p", "c"))
# should print "apple"

######################################################

# Write your x_length_words function here:

def x_length_words(sentence, x):
  list_split = []
  list_split.append(sentence.split(' '))
  for i in list_split:
    for e in i:
      if len(e) >= x:
        return True
      return False

# Uncomment these function calls to test your tip function:
print(x_length_words("i like apples", 2))
# should print False
print(x_length_words("he likes apples", 2))
# should print True

########################################################
#checks for name in sentence whther the name is in upper, lower or nmixed case letters

# Write your check_for_name function here:

def check_for_name(sentence, name):
    return name.lower() in sentence.lower()
  
  
print(check_for_name("My name is jamie", "Jamie"))
# should print True
print(check_for_name("My name is Samantha", "Jamie"))
# should print False

########################################################

# Write your every_other_letter function here:
def every_other_letter(word):
  every_other = ""
  for i in range(0, len(word), 2):
    every_other += word[i]
  return every_other

# Uncomment these function calls to test your tip function:
print(every_other_letter("Codecademy"))
# should print Cdcdm
print(every_other_letter("Hello world!"))
# should print Hlowrd
print(every_other_letter(""))
# should print 

##########################################################

# Write your make_spoonerism function here:

def make_spoonerism(word1, word2):
  w1 = word1.replace(word1[0], word2[0])
  w2 = word2.replace(word2[0], word1[0])
  #w1 = word2[0] + word1[1:]
  #w2 = word1[0] + word2[1:]
  
  return (w1, w2)

#SOLUTION FROM CODEACADEMEY:
def make_spoonerism(word1, word2):
  return word2[0]+word1[1:]+" "+word1[0]+word2[1:]


# Uncomment these function calls to test your function:
print(make_spoonerism("Codecademy", "Learn"))
# should print Lodecademy Cearn
print(make_spoonerism("Hello", "world!"))
# should print wello Horld!

########################################################

# Write your add_exclamation function here:

def add_exclamation(word):
  while len(word) < 20:
    word += '!'
  return word

# Uncomment these function calls to test your function:
print(add_exclamation("Codecademy"))
# should print Codecademy!!!!!!!!!!
print(add_exclamation("Codecademy is the best place to learn"))
# should print Codecademy is the best place to learn

print(make_spoonerism("a", "b"))
# should print b a






