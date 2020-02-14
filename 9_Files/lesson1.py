# Chapter_9 Files

## READING A FILE
# opens a text file, reads the contents and saves the content to a new variable.Lastly, prints the variable.

with open('welcome.txt') as text_file:
  text_data = text_file.read()
print(text_data)

## ITERATNG THROUGH LINES
#  
