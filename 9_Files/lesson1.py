# Chapter_9 Files

## READING A FILE
# opens a text file, reads the contents and saves the content to a new variable.Lastly, prints the variable.

with open('welcome.txt') as text_file:
  text_data = text_file.read()
print(text_data)

## ITERATNG THROUGH LINES

with open('how_many_lines.txt') as lines_doc:
  for line in lines_doc.readlines():
    print(line)

## READING A LINE

with open('just_the_first.txt') as first_line_doc:
  first_line = first_line_doc.readline()
  print(first_line)

#given example:
with open('millay_sonnet.txt') as sonnet_doc:
  first_line = sonnet_doc.readline() #first call of .readline reads the first line only
  second_line = sonnet_doc.readline() # second call of .readline within the same statement reads the 2nd line only.
  print(second_line)

# a 3rd call would read the 3rd row only and so on......

## WRITING A FILE

#given example:
with open('generated_file.txt', 'w') as gen_file:                #passing the 'w' argument to open() open a new file in write mode 				
	gen_file.write("What an incredible file!")              #(rather than the default 'r' read mode when no argument is given

## APPENDING TO A FILE

# as above using the 'a' switch with open() will open a file in append mode. then use xxxxx.write() to append onto existing text.

with open('cool_dogs.txt', 'a') as cool_dogs_file:
  cool_dogs_file.write('Air Buddy')
print(cool_dogs_file)

## WHAT's WITH "with"

#as the text file exists 'outside' of python the 'with' controls the connection between python and the file - making sure to close the connection once the script has finished. Old format is to use xxx.close to end the connection.

#example code:
fun_cities_file = open('fun_cities.txt', 'a')

# We can now append a line to "fun_cities".
fun_cities_file.write("Montréal")

# But we need to remember to close the file
fun_cities_file.close() 

#*** the preferred way is to use 'with'!!
with open('fun_file.txt') as close_this_file:
  setup = close_this_file.readline()
  punchline = close_this_file.readline()

print(setup)

## CSV FILES

with open('logger.csv') as log_csv_file:
  print(log_csv_file.read())
#the csv file is parsed as a string.

## READING A CSV FILE

#Example:
import csv

list_of_email_addresses = []
with open('users.csv', newline='') as users_csv:
  user_reader = csv.DictReader(users_csv)
  for row in user_reader:
    list_of_email_addresses.append(row['Email'])

'''In the above code we first import our csv library, which gives us the tools to parse our CSV file. We then create the empty list list_of_email_addresses which we’ll later populate with the email addresses from our CSV. Then we open the users.csv file with the temporary variable users_csv.

We pass the additional keyword argument newline='' to the file opening open() function so that we don’t accidentally mistake a line break in one of our data fields as a new row in our CSV (read more about this in the Python documentation).

After opening our new CSV file we use csv.DictReader(users_csv) which converts the lines of our CSV file to Python dictionaries which we can use access methods for. The keys of the dictionary are, by default, the entries in the first line of our CSV file. Since our CSV’s first line calls the third field in our CSV “Email“, we can use that as the key in each row of our DictReader.

When we iterate through the rows of our user_reader object, we access all of the rows in our CSV as dictionaries (except for the first row, which we used to label the keys of our dictionary). By accessing the 'Email' key of each of these rows we can grab the email address in that row and append it to our list_of_email_addresses.'''





