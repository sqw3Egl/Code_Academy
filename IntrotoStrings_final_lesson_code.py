def username_generator(first_name, last_name):
  username = first_name[:3] + last_name[:4]
  return username

def password_generator(username):
  password = (username[-1])
  for i in username[0:len(username) -1]:
    password += i
  return password
  
print(username_generator('Andy', 'Field'))


print(password_generator('AndFiel'))  
