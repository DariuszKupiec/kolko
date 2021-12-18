#%%


class Zwierze:
    def __init__(self, nazwa, wiek, waga): #pobawmy się atrybutami przy inicjowaniu obiektu
        self.nazwa = nazwa
        self.waga = waga
        self.wiek = wiek
    
    def podaj_dane(self):
        print(f'Jestem zwierzęciem {self.nazwa}, mam {self.wiek} lat i ważę {self.waga} kg.')

class Slon(Zwierze):
    pass

class Lew(Zwierze):
    def __init__(self):
        self.iloscKlow = 4

class Papuga(Zwierze):
    def __init__(self, nazwa, dlg_skrzydel):
        self.iloscPior = 500
        self.nazwa = nazwa
        self.dlg_skrzydel = dlg_skrzydel

class Hybryda(Lew, Papuga): #przykład wielodziedziczenia
    pass

Dumbo = Slon('Slonik Dumbo', 300, 60)
# Dumbo.nazwa = 'Slonik Dumbo' # Tak nie możemy podać wartości bo w Zwierze wymusiliśmy podanie parametrów, natomiast w Lew nadpisaliśmy przez użycie __init__
# Dumbo.waga = 300
# Dumbo.wiek = 60

Simba = Lew()
Simba.iloscKlow = 4
Simba.wiek = 34
Simba.nazwa = 'Lew Simba'
Simba.waga = 340





