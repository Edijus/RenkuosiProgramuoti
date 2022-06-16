# Importuokite reikiamus modulius, kad veiktų žemiau nurodytos funkcijos
from modules.numbers.numbers import one, two, three, four, five
from modules.math.composition import composition
from modules.math.division import division
from modules.math.subtraction import substraction
from modules.math.multiplication import multiplication


def addition(a, b):
    return composition(a, b)


def divivsion(a, b):
    return division(a, b)


# Kitų failų ir žemiau esančio kodo nekeiskite
a = addition(one, four)
b = divivsion(four, two)
c = substraction(three, two)
d = multiplication(five, two)

print(a)
print(b)
print(c)
print(d)
