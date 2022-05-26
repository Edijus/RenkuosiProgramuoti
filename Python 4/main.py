def my_print(sentence):
    print(sentence)


my_print('Hello world')


def my_function(argument1, argument2):
    print(argument1, argument2)


my_function(['hi', 'ola'], 'labas')
my_function(argument2='Pirmas', argument1='Antras')


def my_function_1(argument0, argument1='Antras'):
    print(argument0, argument1)


my_function_1('Su default reikšme')
my_function_1('Su default reikšme', 'perrašomas')


def my_function_2(argument0: str, argument1: str) -> str:
    value = argument0.replace(argument1, 'abc')
    return value


result = my_function_2('Python', 'thon')
print(result)


def my_function_3(*belekas):
    for argument in belekas:
        print(argument)


my_function_3(1, 2, 3, 4, 5, 6)
my_function_3(*range(2, 5))


def my_function_5(**kwargs):
    for key, value in kwargs.items():
        print(key, value)


my_function_5(first='Greeks', mid='for', last='Geeks')

argument0 = {
    'name': 'John',
    'age': 44
}

my_function_5(**argument0)


def _sum(*args):
    return sum(args)


print(_sum(2, 2, 2))


def my_function_6():
    print(argument0)


my_function_6()


def my_function_7():
    local_argument = 1


my_function_7()


# print(local_argument)

def my_docstring_fnk(arg0, arg1, *args, **kwargs):
    '''
    <Documentation>

    :param arg0:
    :param arg1:
    :param args:
    :param kwargs:
    :return:
    '''


f = lambda x, y: x + y

print(f(1, 2))


def _f(x, y):
    return x + y


print(_f(1, 2))


from functions import find_leap_year
from functions import is_leap_year

leap_years = find_leap_year(1900, 2025)
print(leap_years)
print('2001 yra keliamieji:', is_leap_year(2001))
