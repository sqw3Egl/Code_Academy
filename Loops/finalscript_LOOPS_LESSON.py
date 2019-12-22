single_digits = list(range(10))
squares = []

for i in single_digits:
  sq = i ** 2
  squares.append(sq)
print(squares)

cubes = [i ** 3 for i in single_digits]
print(cubes)