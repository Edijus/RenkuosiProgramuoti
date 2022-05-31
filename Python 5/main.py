from abc import ABC, abstractmethod

class DummyClass:
    def __init__(self, parameter: int, parameter2: str):  # Constructor
        self.parameter = parameter
        self.parameter2 = parameter2

    @staticmethod
    def dummy_static_method(parameter0: str):
        print('dummy_static_method called', parameter0)

    def dummy_method(self):
        print('dummy_method called', self.parameter)


print(type(DummyClass))
dummy_object = DummyClass(69, 'Edijs')
print(type(dummy_object))
print(dummy_object.parameter)
dummy_object.parameter = 5
print(dummy_object.parameter)
dummy_object.dummy_method()
dummy_object.dummy_static_method('555')


class Flower(ABC):
    def __init__(self, blossom_color: str, has_spikes: bool = False):
        self.__blossom_color = blossom_color  # private
        self.has_spikes = has_spikes

    @staticmethod
    @abstractmethod
    def bloom():
        pass


class Rose(Flower):
    def __init__(self, blossom_color: str, has_spikes: bool = True):
        self.blossom_color = blossom_color  # public
        self._blossom_color = blossom_color  # protected
        self.__blossom_color = blossom_color  # private
        self.has_spikes = has_spikes
        super().__init__(blossom_color, has_spikes)

    @staticmethod
    def bloom():
        print('Rose blooms')

    def get_blossom_color(self):
        return self.__blossom_color


class Tulip(Flower):
    def __init__(self, blossom_color: str, has_spikes: bool = False):
        self.__blossom_color = blossom_color  # private
        self.has_spikes = has_spikes
        super().__init__(blossom_color, has_spikes)

    @staticmethod
    def bloom():
        print('Tulip blooms')

    def get_blossom_color(self):
        return self.__blossom_color


#  flower = Flower('orange')

red_rose = Rose('red')
print('public attribute:', red_rose.blossom_color)
print('protected attribute:', red_rose._blossom_color)
#  print('private attribute:', red_rose.__blossom_color)
print('private attribute2:', red_rose.get_blossom_color())
red_rose.bloom()

blue_tulip = Tulip('blue')
blue_tulip.bloom()
print('blue_tulip blossom color:', blue_tulip.get_blossom_color())
