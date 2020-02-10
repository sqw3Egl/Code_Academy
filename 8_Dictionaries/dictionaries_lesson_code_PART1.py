#Dictionaries Lesson

#9 parts

## 1. Dictionary example and syntax.

sensors =  {"living room": 21, "kitchen": 23, "bedroom": 20, "pantry": 22}
num_cameras = {"backyard": 6, "garage": 2, "driveway": 1}

print(sensors, num_cameras)


## 2. Create a list of words and their translation.

translations = {'mountain': 'orod', 'bread': 'bass', 'friend': 'mellon', 'horse': 'roch'}

## 3. Invalid keys - can only use lists or dictionaries as the 'value' side of a key, not the key itself

children = {"von Trapp": ["Johannes", "Rosmarie", "Eleonore"], "Corleone":["Sonny", "Fredo", "Michael"]}

## 4. Dictionaries can be created as empty.

my_empty_dictionary = {}

## 5. Adding key: value pairs to an empty dictionary

animals_in_zoo = {}

animals_in_zoo["zebras"] = 8
animals_in_zoo["monkeys"] = 12
animals_in_zoo["dinosaurs"] = 0

print(animals_in_zoo)

## 6. Adding multiple key: value pairs to a dictionary

user_ids = {"teraCoder": 9018293, "proProgrammer": 119238}

user_ids.update({"theLooper": 138475, "stringQueen": 85739})

print(user_ids)

## 7. Overwriting existing key: values in a dictionary

oscar_winners = {"Best Picture": "La La Land", "Best Actor": "Casey Affleck", "Best Actress": "Emma Stone", "Animated Feature": "Zootopia"}

oscar_winners["Supporting Actress"] = "Viola Davis"

oscar_winners["Best Picture"] = "Moonlight"

print(oscar_winners)

## 8. List comprehensions to dictionaries (combine 2 lists into dictionary)

drinks = ["espresso", "chai", "decaf", "drip"]
caffeine = [64, 40, 0, 120]

zipped_drinks = zip(drinks, caffeine)
drinks_to_caffeine = {key:value for key, value in zipped_drinks}

## 9. Review

songs = ["Like a Rolling Stone", "Satisfaction", "Imagine", "What's Going On", "Respect", "Good Vibrations"]
playcounts = [78, 29, 44, 21, 89, 5]
plays = {song:playcount for song, playcount in zip(songs, playcounts)}

print(plays)

plays["Purple Haze"] = 1

plays["Respect"] = 94

library = {"The Best Songs": plays, "Sunday Feelings": {}}

print(library)


 


