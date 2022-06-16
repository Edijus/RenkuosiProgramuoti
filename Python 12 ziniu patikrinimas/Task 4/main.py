# Sukurkite klasę "Movie", kuri gebės sukurti objektus 3 savybėm ir 1 metodu. 
# Naudojant šią klasę sukurkite bent du skirtingus objektus.

# Savybės:
# title: string
# director: string
# budget: number

# Metodas: 
# was_expensive() - jeigu filmo "budget" yra daugiau nei 100 000 000 mln USD, tada grąžins True, kitu atveju False.


class Movie:
    def __init__(self, title: str, director: str, budget: float):
        self.__title = title
        self.__director = director
        self.__budget = budget

    def was_expensive(self) -> bool:
        return self.__budget > 100000000



men_in_black = Movie('Men in black', 'Barry Sonnenfeld', 90000000)
print(men_in_black.was_expensive())

edijs_help = Movie('Edijaus pagalba', 'Edijs Kole', 10000000000)
print(edijs_help.was_expensive())

