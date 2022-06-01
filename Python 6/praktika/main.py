# Užduotis 1
class Automobilis:
    def __init__(self, metai: int, modelis: str, kuro_tipas: str):
        self.__metai = metai
        self.__modelis = modelis
        self.__kuro_tipas = kuro_tipas
        print(self.__metai, self.__modelis, self.__kuro_tipas)

    def vaziuoti(self):
        print('Važiuoja')

    def stoveti(self):
        print('Priparkuota')

    def pildyti_degalu(self):
        print('Degalai įpilti')


class Elektromobilis(Automobilis):
    def __init__(self, metai: int, modelis: str, kuro_tipas: str):
        super().__init__(metai, modelis, kuro_tipas)

    def pildyti_degalu(self):
        print('Baterija įkrauta')

    def vaziuoti_autonomiskai(self):
        print('Važiuoja autonomiškai')


auto0 = Automobilis(2012, 'Audi A4', 'Benzinas')
auto0.vaziuoti()
auto0.stoveti()
auto0.pildyti_degalu()

ev0 = Elektromobilis(2012, 'Tesla S', 'Elektra')
ev0.vaziuoti()
ev0.stoveti()
ev0.pildyti_degalu()
ev0.vaziuoti_autonomiskai()

# Užduotis 2
import datetime


class Darbuotojas:
    def __init__(self, vardas: str, valandos_ikainis: float, dirba_nuo: datetime):
        self._vardas = vardas
        self._valandos_ikainis = valandos_ikainis
        self._dirba_nuo = dirba_nuo

    def kiek_nudirbo(self):
        date_diff = datetime.datetime.now() - self._dirba_nuo
        days_diff = date_diff.days
        if days_diff < 0:
            return 0
        else:
            return days_diff

    def paskaiciuoti_atlyginima(self):
        return round(self._valandos_ikainis * (self.kiek_nudirbo() * 8), 2)


darbuotojas0 = Darbuotojas('Edijs', 10, datetime.datetime(2022, 5, 1))
print('Nudirbta', darbuotojas0.kiek_nudirbo(), 'dienų')
print('Edijs uždirbo', darbuotojas0.paskaiciuoti_atlyginima())


class NormalusDarbuotojas(Darbuotojas):
    def __init__(self, vardas: str, valandos_ikainis: float, dirba_nuo: datetime):
        super().__init__(vardas, valandos_ikainis, dirba_nuo)

    def paskaiciuoti_atlyginima(self):
        return round(self._valandos_ikainis * ((self.kiek_nudirbo() * 8) / 7 * 5), 2)


normalus0 = NormalusDarbuotojas('John', 10, datetime.datetime(2022, 5, 1))
print('John uždirbo', normalus0.paskaiciuoti_atlyginima())
