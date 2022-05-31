# Task 1

class Sakinys:
    def __init__(self, tekstas: str):
        self.teksas = tekstas

    def tekstas_atbulai(self):
        return self.teksas[len(self.teksas)::-1]

    def tekstas_mazosiomis(self):
        return self.teksas.lower()

    def tekstas_didziosiomis(self):
        return self.teksas.upper()

    def zodis_pagal_eiles_nr(self, nr: int):
        zodziai = self.teksas.split()
        return zodziai[nr - 1]

    def kiek_pasikartojimu(self, fraze: str):
        return self.teksas.count(fraze)

    def pakeisti(self, senas: str, naujas: str):
        return self.teksas.replace(senas, naujas)

    def informacija(self):
        zodziai = self.teksas.split()
        print('žodžių:', len(zodziai))

        skaiciu = 0
        for zodis in zodziai:
            if zodis.isnumeric():
                skaiciu = skaiciu + 1

        print('Skaičių:', skaiciu)

        didziuju = 0
        mazuju = 0
        for zodis in zodziai:
            for simbolis in zodis:
                if simbolis.isupper():
                    didziuju = didziuju + 1
                elif simbolis.islower():
                    mazuju = mazuju + 1

        print('Didžiųjų:', didziuju)
        print('Mažųjų:', mazuju)



mano_sakinys = Sakinys('Labas, mano vardas Edijs. Gimiau 1988')
print('Atbulai:', mano_sakinys.tekstas_atbulai())
print('Mažosiomis:', mano_sakinys.tekstas_mazosiomis())
print('Didžiosiomis:', mano_sakinys.tekstas_didziosiomis())
print('Žodis pagal numerį:', mano_sakinys.zodis_pagal_eiles_nr(2))
print('"as" pasikartojimų:', mano_sakinys.kiek_pasikartojimu('as'))
print('"as" pakeista į "LL":', mano_sakinys.pakeisti('as', 'LL'))
mano_sakinys.informacija()

tavo_sakinys = Sakinys('Kitas klasės objektas')
print('Atbulai:', tavo_sakinys.tekstas_atbulai())
print('Mažosiomis:', tavo_sakinys.tekstas_mazosiomis())
print('Didžiosiomis:', tavo_sakinys.tekstas_didziosiomis())
print('Žodis pagal numerį:', tavo_sakinys.zodis_pagal_eiles_nr(2))
print('"as" pasikartojimų:', tavo_sakinys.kiek_pasikartojimu('as'))
print('"as" pakeista į "LL":', tavo_sakinys.pakeisti('as', 'LL'))
tavo_sakinys.informacija()


# Task 2
import datetime
import sys
import calendar

class Sukaktis:
    def __init__(self, **kwargs):
        self.metai = self.__supildyti_data('metai', 1, sys.maxsize, **kwargs)
        self.menuo = self.__supildyti_data('menuo', 1, 12, **kwargs)
        self.diena = self.__supildyti_data('diena', 1, 31, **kwargs)
        self.valanda = self.__supildyti_data('valanda', 1, 24, **kwargs)
        self.minute = self.__supildyti_data('minute', 1, 60, **kwargs)
        self.sekunde = self.__supildyti_data('sekunde', 1, 60, **kwargs)

        self.data = datetime.datetime(self.metai, self.menuo, self.diena, self.valanda, self.minute, self.sekunde)

    @staticmethod
    def __supildyti_data(pavadinimas: str, min_reiksme: int, max_reiksme: int, **kwargs):
        rez = 0
        arg_value = kwargs.get(pavadinimas)
        # print(pavadinimas, type(pavadinimas), arg_value)
        if type(arg_value) == 'NoneType':
            rez = min_reiksme
        elif not (arg_value is None):
            rez = kwargs.get(pavadinimas)

        rez = min(max(rez, min_reiksme), max_reiksme)
        return rez


    def kiek_praejo(self):
        date_diff = self.data - datetime.datetime.now()
        days_diff = abs(date_diff.days)
        print('Nuo', self.data, 'praėjo', int(days_diff / 365), 'metai',
              int(days_diff / 365 * 12), 'mėnesiai',
              days_diff, 'dienų',
              days_diff * 24, 'valandų',
              days_diff * 24 * 60, 'minučių',
              days_diff * 24 * 60 * 60, 'sekundžių')

    def ar_keliamieji(self):
        return calendar.isleap(self.metai)

mano_data = Sukaktis(metai=1988, diena=6, menuo=55, minute=59, sekunde=2)
mano_data.kiek_praejo()
print('Ar metai keliamieji:', mano_data.ar_keliamieji())