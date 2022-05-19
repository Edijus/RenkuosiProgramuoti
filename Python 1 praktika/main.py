# Pirma užduotis
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

input1 = input('Įveskite sveikąjį/trupmeninį skaičių:')
if is_number(input1) == False:
    print(input1, 'nėra sveikasis/trupmeninis skaičius', type(input1))
    exit(2)

input2 = input('Įveskite sveikąjį/trupmeninį skaičių:')
if is_number(input2) == False:
    print(input2, 'nėra sveikasis/trupmeninis skaičius', type(input2))
    exit(2)

if input1 < input2:
    print(input1, '<', input2)
elif input1 == input2:
    print(input1, '=', input2)
else:
    print(input1, '>', input2)

# Antra užduotis
sentence = 'Zen of Python'
arr = sentence.split(' ')
print('Paskutinis antro žodžio simbolis:', arr[1][-1])
print('Pirmas trečio žodžio simbolis:', arr[2][0])
print('Pirmas žodis:', arr[0])
print('Paskutinis žodis:', arr[-1])
arr.reverse()
print('Visa frazė atbulai:', arr)
print('Visa frazė atbulai:', ' '.join(arr))
print('Pakeičia žodį:', ' '.join(arr).replace('Python', 'Programming'))

# Trečia užduotis
print('Upper:', sentence.upper())
print('CaseFold:', sentence.casefold())
print('Capitalize:', sentence.capitalize())
print('Count y:', sentence.count('y'))


# Ketvirta užduotis
input1 = input('Įveskite sveikąjį/trupmeninį skaičių:')
if is_number(input1) == False:
    print(input1, 'nėra sveikasis/trupmeninis skaičius', type(input1))
    exit(2)

input2 = input('Įveskite sveikąjį/trupmeninį skaičių:')
if is_number(input2) == False:
    print(input2, 'nėra sveikasis/trupmeninis skaičius', type(input2))
    exit(2)

action = input('Įveskite kokį veiksmą atlikti:')
if action == '+':
    print(input1, '+', input2, '=', float(input1) + float(input2))
elif action == '-':
    print(input1, '-', input2, '=', float(input1) - float(input2))
elif action == '*':
    print(input1, '*', input2, '=', float(input1) * float(input2))
elif action == '/':
    print(input1, '/', input2, '=', float(input1) / float(input2))
else:
    print('Galimi veiksmai: + - * /')
    exit(2)

# Penkta užduotis
input1 = input('Įveskite sveikąjį/trupmeninį skaičių:')
if is_number(input1) == False:
    print(input1, 'nėra sveikasis/trupmeninis skaičius', type(input1))
    exit(2)

if (float(input1) % 2) == 0:
    print('Skaičius', input1, 'yra lyginis')
else:
    print('Skaičius', input1, 'yra nelyginis')

if (float(input1) % 3) == 0:
    print('Skaičius', input1, 'dalinasi iš 3')