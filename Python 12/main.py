from datetime import date


sarasas = [5, 1, 3]
sarasas.sort(reverse=True)
print(sarasas)
print(5 == 6 or 72 > 2)


try:
    print(12/0)
except:
    print('fd')

print('Don')



a = 5
i = 0
while a < 100:
    print(a)
    a = 5
    i = i + 1
    if i > 150:
        print('daug')
        break


class Zmogus:
    def __init__(self, vardas, amzius):
        self.vardas = vardas
        self.amzius = amzius

    def begti(self):
        print('Begu')

zmogus1 = Zmogus("Jonas", 15)
zmogus1.begti()

something = {"data": "Value"}
print(type(something))


skaicius = 12
if skaicius % 2 == 0:
    print("Skaicius lyginis")