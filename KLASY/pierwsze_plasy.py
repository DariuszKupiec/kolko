class MojaKlasa:
    def wyswietl(x):
        return 'Witaj swiecie'

x = MojaKlasa()
print(x.wyswietl())


#%%

class Prostopadloscian:
        def __init__(self):    #class constuctor - konstruktor uruchamia się przy starcie
            self.podstawa_a = 0 # dobra praktyka to nadanie wartości początkowej 
            self.podstawa_b = 0 # bok b 
            self.wysokosc_h = 0 # bok c czyli h

        def Objetosc(self):
            return self.podstawa_a * self.podstawa_b * self.wysokosc_h

wtc=Prostopadloscian()
wtc.podtawa_a=100
wtc.podtawa_b=200
wtc.podtawa_h=400
print(wtc.Objetosc())



