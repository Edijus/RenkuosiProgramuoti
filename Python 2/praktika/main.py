# Task 1
from ast import _new

_list = ['cat', 'house', 'bike', 'car', 'house', 1]

_cat = {
    'name': 'John',
    'color': 'black',
    'length': 50,
    'eyes': {
        'color': 'blue',
        'size': 'average'
    },
    'has_owner': False
}

print(_list[0])
print(_cat['name'])

_list.append('dog')
print(_list)
_cat['tag'] = '54SD'
print(_cat)

_list.remove('cat')
print(_list)
_cat.pop('length')
print(_cat)

_list[0] = 'spider'
print(_list)
_cat['name'] = 'Susana'
print(_cat)

# Task 2
def is_integer(n):
    try:
        float(n)
    except ValueError:
        return False
    else:
        return float(n).is_integer()

def is_float(n):
    try:
        float(n)
    except ValueError:
        return False
    else:
        return True

def is_number(n):
    if is_integer(n) == True:
        return True
    else:
        return is_float(n)

def ask_number():
    input1 = input('Įveskite skaičių:')
    if is_number(input1) == False:
        print(input1, 'nėra sveikasis/trupmeninis skaičius', type(input1))
        exit(2)
    if float(input1) > 0:
        ask_number()

ask_number()

# Task 3
_list = []
word_count = input('Įveskite žodžių skaičių:')
if is_integer(word_count) == False:
    print(word_count, 'nėra sveikasis skaičius', type(word_count))
    exit(2)

for x in range(int(word_count)):
   word = input('Įveskite žodį ' + str(x + 1) + ': ')
   _list.append(word)

print(_list)

for word in _list:
    print(word, len(word), _list.index(word))

# Task 4
import random
_numbers = []
for x in range(3):
    random_number = random.randint(1, 6)
    _numbers.append(random_number)

print(_numbers)
_contains5 = False
for _number in _numbers:
    if _number == 5:
        _contains5 = True

if _contains5:
    print('Pralaimėjai')
else:
    print('Laimėjai')

# Task 5
import calendar
_year = input('Įveskite metus: ')
if is_integer(_year) == False:
    print(_year, 'nėra sveikasis', type(_year))
    exit(2)

if calendar.isleap(int(_year)):
    print('Keliamieji metai')
else:
    print('Nekeliamieji metai')

# Task 6
for _year in range(1900, 2100):
    if calendar.isleap(int(_year)):
        print(_year)

