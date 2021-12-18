#%%

class Szopa:
    pomalowaneBudynki = 0
    def __init__(self, bok_a, bok_b, wys_h):  # class constuctor - konstruktor uruchamia się przy starcie
        self.podstawa_a = bok_a # dobra praktyka to nadanie wartości początkowej 
        self.podstawa_b = bok_b # bok b self.wysokosc_h = wys_h # bok c czyli h
        Szopa.pomalowaneBudynki += 1

    def Pomaluj(self):
            return 2 * (self.podstawa_a + self.podstawa_b) * self.wysokosc_h
            

szopa1 = Szopa(2, 3, 5)
print(szopa1.Pomaluj())
szopa2 = Szopa(5, 1, 2)
print(szopa2.Pomaluj())
print(Szopa.pomalowaneBudynki)

