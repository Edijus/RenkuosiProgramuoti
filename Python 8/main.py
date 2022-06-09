from functools import reduce


_numbers = [5, 7, 12, 1, -4, -8, 0, 43]
_numbers2 = set(_numbers)
_numbers_after = []

for _number in _numbers:
    _numbers_after.append(_number + 1)

print('for', _numbers_after)
print('map list', list(map(lambda x: x + 1, _numbers)))
print('map set', set(map(lambda x: x + 1, _numbers2)))

print('Remove elements <= 1', list(filter(lambda x: x > 1, _numbers)))
print('Sum list using reduce:', reduce(lambda x, y: x + y, _numbers))
print('Sum :', sum(_numbers))

joined = ";".join(list(map(lambda x: str(x), _numbers2)))
print('Numbers to string separated with ;', joined)

myTuple = ("John", "Peter", "Vicky")
x = "#".join(myTuple)
print(x)


print('Split joined numbers', joined.split(';'))

_numbers.sort()
print(_numbers)
_numbers.sort(reverse=True)
print(_numbers)

def order_function(x):
    return x


def descending_order_function(x):
    return -x


_numbers.sort(key=order_function)
print(_numbers)
_numbers.sort(key=descending_order_function)
print(_numbers)

_numbers.sort(key=lambda x: -abs(x))
print(_numbers)

