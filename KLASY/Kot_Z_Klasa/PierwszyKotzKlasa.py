#%%

class Kot:
    # def __init__(self, Imie, Kolor_oczu, Kolor_siersci, Dlugosc, Wysokosc, Wiek, Waga):  # class constuctor - konstruktor uruchamia się przy starcie
    def __init__(self):  # class constuctor - konstruktor uruchamia się przy starcie
        self.Imie = '' 
        self.Kolor_oczu = ''
        self.Kolor_siersci = ''
        self.Dlugosc = 1
        self.Wysokosc = 1
        self.Wiek = 9
        self.Waga = 6

    def mialczenie(self):
        print('Miau !')
        return "Miau"

    def spanie(self):
        if self.Wiek == 10:
            print('śpi godzinę')
        elif self.Wiek>=10:
            print('śpi godzinę')
    
    def jedzenie(self):
        self.Waga += 10
        print('kot dobrze zjadł')

    def drapanie(self):
        if self.Waga >= 10:
            print('szkody są duże')
        else:
            print('szkody są małe')

# Mialczenie, Jedzenie, Spanie, Drapanie, Mruczenie

# kot1 = Kot('Puszek', 'Zielone', 'Szary', 1.05, 0.95, 5, 5)
# kot2 = Kot('Okruszek', 'Zielono-szare', 'Bury', 0.75, 0.55, 3, 3)
# print(szopa2.Pomaluj())

