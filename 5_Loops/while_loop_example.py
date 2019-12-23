all_students = ["Alex", "Briana", "Cheri", "Daniele", "Dora", "Minerva", "Alexa", "Obie", "Arius", "Loki"]
students_in_poetry = []

index = 0
while len(students_in_poetry) < 6:
  new = all_students.pop()
  students_in_poetry.append(new)
  
print(students_in_poetry)