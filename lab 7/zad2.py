class Przystanek():
    def __init__(self, nazwa, przesiadka, czas_postoju):
        self._nazwa = nazwa
        self._przesiadka = przesiadka
        self._czas = czas_postoju

    def getname(self):
        return self._nazwa

    def przesiadka(self):
        return self._przesiadka

    def czas_postoju(self):
        return self._czas


class Pozycja():
    def __init__(self, przystanek, czas_przejazdu):
        self._przystanek = Przystanek(*przystanek)
        self._czas = czas_przejazdu

    def getprzystanek(self):
        return self._przystanek

    def czas_dojazdu(self):
        return self._czas


class Trasa():
    def __init__(self, nazwa, pozycje):
        self._nazwa = nazwa
        self._pozycje = []
        for pozycja in pozycje:
            self._pozycje.append(Pozycja(*pozycja))

    def getname(self):
        return self._nazwa

    def total_time(self):
        time = 0
        for pozycja in self._pozycje:
            time += pozycja.getprzystanek().czas_postoju() + pozycja.czas_dojazdu()
            print(pozycja.getprzystanek().czas_postoju() + pozycja.czas_dojazdu())
        print(time)
        return time

    def add_time(self, time, interval):
        godzina = time[0]
        minuty = time[1] + interval
        godzina += int(minuty / 60)
        minuty = minuty % 60
        godzina = godzina % 24
        return (godzina, minuty)

    def time_str(self, time):
        return str(time[0]) + ':' + str(time[1])

    def generuj_rozklad(self, czas):
        czas = list(czas)
        czas_odjazdu = czas
        koniec = self.add_time(czas, self.total_time())
        print(self.getname())
        print(self.time_str(czas), '-', self.time_str(koniec))
        for pozycja in self._pozycje:
            czas_przyjazdu = self.add_time(czas_odjazdu, pozycja.czas_dojazdu())
            czas_odjazdu = self.add_time(czas_przyjazdu, pozycja.getprzystanek().czas_postoju())
            print(pozycja.getprzystanek().getname(),self.time_str(czas_przyjazdu),'-', self.time_str(czas_odjazdu), pozycja.getprzystanek()._przesiadka)


zajezdnia = ('Stajnia choszczowka', False, 0)
rondo = ('rondo Dawida', True, 2)
warszawska = ('Warszawska', False, 2)
mickiewicza = ('Adama Mickiewicza', False, 2)
reymonta = ('Reymonta', False, 2)
belwederska = ('Belwederska', True, 1)
pętla = ('Rondo ptak', False, 13)

pozycje = [(zajezdnia, 0), (rondo, 5), (warszawska, 5), (mickiewicza, 5), (reymonta, 4), (belwederska, 10), (pętla, 10)]
trasa_N01 = Trasa('N01', pozycje)
trasa_N01.generuj_rozklad((23, 48))