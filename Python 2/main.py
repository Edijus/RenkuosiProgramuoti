'''
- masyvai: List, array, tuple, set
- žodynas: dict
- ciklai: for, while
'''

import json
import random

words = ['cat', 'house', 'bike', 'car', 'house', 1] #list rašomas tarp []
coordinates = (1,2,2,'sky') #tuple rašomas tarp ()
_set = {1, 2, 2}
objects = [1, 1.2,'table',[1,2,3]]
print('words type:', type(words))
print('Words original:', words)
print('Words extended with "firework:', words.append('firework'))
print('words type:', type(coordinates))
print('words type:', type(objects))
print('words to set:', set(words))
print('Tuple to set:', set(coordinates))
print('Last element from words:', words[-1])
print('3rd and 4th element of words:', words[2:4])
print('_set:', _set)

cat = {
    'name': 'Joe',
    'color': 'black',
    'length': 40,
    'eyes': {
        'color': 'blue',
        'size': 'average'
    },
    'has_owner': True
}

print('cat type:', type(cat))
print('cat name (can raise exception when key does not exit):', cat['name'])
print('cat name (no exception):', cat.get('name'))

cat['eye_color'] = 'green'
print('cat eye color:', cat['eye_color'])

cat['name'] = 'John'
print('name:', cat['name'])
print('cat:', cat)
print('cat eyes size:', cat['eyes']['size'])
print('cat eyes size:', cat.get('eyes').get('size'))
print('cat json', json.dumps(cat))

json_cat = json.dumps(cat)
cat_new = json.loads(json_cat)
print('json_cat to dict:', cat_new)
print('cat eyes size:', cat_new['eyes']['size'])

for word in words:
    print(word, type(word))

for coordinate in coordinates:
    print(coordinate)

for _object in objects:
    print(type(_object))

# def print_instance_key(ref):
#     for key, value in ref:
#         print('fnk', key, value)
#         if isinstance(value, dict):
#             print_instance_key(value)
#
# for key, value in cat.items():
#     print_instance_key(value)

for key, value in cat.items():
    print(key, value)
    if isinstance(value, dict):
        for key1, value1 in value.items():
            print('2', key1, value1)

for key in cat:
    print(key)

for key in cat['eyes']:
    print(key)

while True:
    random_number = random.randint(0, 9)
    print(random_number)
    if random_number == 7:
        break

for iteration in range(10):
    print(iteration)

words_filtered = [word  for word in words if type(word) == str] # list comprehension
print(words_filtered)

word_lengths = [len(word) for word in words_filtered]
print(word_lengths)

cat0 = {
    'name': 'John',
    'color': 'black',
    'length': 50,
    'eyes': {
        'color': 'blue',
        'size': 'average'
    },
    'has_owner': False
}

cats = [cat, cat0]
print(cats)

'''
Keliamieji metai:
- ieškome skaičių, kurie:
  a) Dalinasi iš 400
  b) bet nesidalina iš 100
  c) ir dalinasi iš 4
'''


for word in words[0:3]:
    print('ek', word, type(word))


for x in range(3):
    print(words[x])

i = 0
for word in words:
    i = i + 1
    if i == 3:
        break
    print('važiuojam', word, type(word))