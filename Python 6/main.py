import random


class CustomException(Exception):
    pass


def my_function():
    random_number = random.randint(0, 2)
    print(random_number)
    if random_number == 1:
        print('OK')
    elif random_number == 2:
        raise CustomException
    else:
        raise TypeError


try:
    my_function()
except (CustomException, TypeError):
    print('Expected exception')
except TypeError:
    print('Unexpected exception')


class Plant:
    def __init__(self, name: str):
        self.name = name
        self.say_hello()

    def grow(self):
        print(self.name, 'grows')

    def age(self):
        print(self.name, 'ages')

    def say_hello(self):
        print(self.name, 'says hello')


class Flower(Plant):
    def __init__(self, name: str):
        super().__init__(name)

    @staticmethod
    def grow():
        print('Overridden in Child')


flower = Flower('Rose')
flower.grow()
flower.age()


Flower.grow()
Flower('Tulip').grow()


class CompanyAddress:
    def __init__(self, street: str, house_number: int, postal_code: str):
        self.street = street
        self.house_number = house_number
        self.postal_code = postal_code
        self.make_address_object()

    def get(self) -> dict:  # funkcijos return tipas
        return self.__address

    def make_address_object(self):
        self.__address = {
            'street': self.street,
            'house_number': self.house_number,
            'postal_code': self.postal_code
        }


class Company:
    def __init__(self, name: str, company_address: CompanyAddress):
        self.name = name
        self.company_address = company_address

    def get_copmany_information(self):
        information = self.company_address.get()
        information['name'] = self.name
        return information



company_address0 = CompanyAddress('Kalvarijų', 43, '12345')
company0 = Company('Lidl', company_address0)
print('company0 info:', company0.get_copmany_information())


company1 = Company('Maxima', 1)
company_address1 = CompanyAddress('Žalgirio', 43, '54321')
company1.company_address = company_address1
company1.get_copmany_information()
