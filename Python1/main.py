py1_string = 'Hello'
py1_int = -99
py1_float = 1.5
py1_bool = False
print(py1_int * 10)
print(py1_float * 10)
print(type(py1_string))
print(type(py1_float))
print(0.1 + 0.1 + 0.1 == 0.3)

py1_name = 'Edijs'
print(py1_string + ' ' + py1_name)

_my_string = 'Šiandiena' #input('Įveskite žodį: ')
print(_my_string)

if 1 == 1:
    print('Veinas')
    print('Du')

print('Žodžio ilgis:', len(_my_string))
print('Pirma žodžio raidė:', _my_string[0])
print('Paskutinė žodžio raidė:', _my_string[-1])
print('Priešpaskutinė žodžio raidė:', _my_string[-2])
print('Priešpaskutinė žodžio raidė:', _my_string[-3])

if py1_bool and 1 == 1:
    print('Tiesa')

if py1_bool or True:
    if 1 == 1:
        print('Labai tiesa')

if py1_bool:
    print('Tiesaaaa')
else:
    print('neteisa')

if py1_bool:
    print('Tiesaaaa')
elif 5 < 6:
    print('Šeši')
else:
    print('neteisa')

print('Pakelta laipsniu:', 3 ** 2)
print('Liekana mod:', 1 % 5)
print('Liekana mod:', 7 % 2)
print('Liekana mod:', 10 % 5)
print('Dalyba:', 1 / 5)

print('Padaugina stringą ' * 2)
s = 'Labas'
print('Pakeisti raidę "a" į raidę "A"', s.replace('a', 'A'))

sentence = 'Life long  sentence'
print('Sakinys į mąsyvą:', sentence.split(' '))
print('Pirmas mąsyvo elementas:', sentence.split(' ')[0])
print('Paskutinis mąsyvo elementas:', sentence.split(' ')[-1])

arr = sentence.split(' ')
sentence2 = '_'.join(arr)
print('Mąsyvas į stringą:', sentence2)

exit(4)
