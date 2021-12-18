#%%
# tworzę grę kółko-krzyżyk
# tworzymy słownik który jest naszą planszą do gry - tworzymy słownik PlanszaDoGry

PlanszaDoGry = {'7':' ','8':' ','9':' ',
                '4':' ','5':' ','6':' ',
                '1':' ','2':' ','3':' '}

klawiszeGry=[]

for key in PlanszaDoGry:
    klawiszeGry.append(key)

print(klawiszeGry)

def drukujPlansze(pole):
    print(f"{pole['7']}|{pole['8']}|{pole['9']}")
    print('-+-+-')
    print(f"{pole['4']}|{pole['5']}|{pole['6']}")
    print('-+-+-')
    print(f"{pole['1']}|{pole['2']}|{pole['3']}")

def gra():
    
    gracz='X'
    licznik = 0 # licznik ruchów, po 5 ma zacząć sprawdzać wynik gry, wszystkich jest 9 ruchów

    for i in range(10):
        drukujPlansze(PlanszaDoGry)
        # print(f"Twój ruch, {gracz}. Wybierz gdzie stawiasz znak ") # tę linię zastapimy od razu wczytaniem do zmiennej move
        move=input(f"Twój ruch, {gracz}. Wybierz gdzie stawiasz znak ")

        if PlanszaDoGry[move] == ' ':
            PlanszaDoGry[move]=gracz
            licznik += 1
        else:
            Print('Pole zajęte, wybierz inne\n Wybierz inne miejsce')
            continue

        if licznik >= 5:
            if PlanszaDoGry['7']==PlanszaDoGry['8']==PlanszaDoGry['9'] != ' ':
                drukujPlansze(PlanszaDoGry)
                print(f'\nKoniec gry, wygrał gracz" {gracz}')
                break
            elif PlanszaDoGry['4']==PlanszaDoGry['5']==PlanszaDoGry['6'] != ' ':
                drukujPlansze(PlanszaDoGry)
                print(f'\nKoniec gry, wygrał gracz" {gracz}')
                break
            elif PlanszaDoGry['1']==PlanszaDoGry['2']==PlanszaDoGry['3'] != ' ':
                drukujPlansze(PlanszaDoGry)
                print(f'\nKoniec gry, wygrał gracz" {gracz}')
                break
            # koniec wygranych poziomych
            elif PlanszaDoGry['7']==PlanszaDoGry['4']==PlanszaDoGry['1'] != ' ':
                drukujPlansze(PlanszaDoGry)
                print(f'\nKoniec gry, wygrał gracz" {gracz}')
                break
            elif PlanszaDoGry['8']==PlanszaDoGry['5']==PlanszaDoGry['2'] != ' ':
                drukujPlansze(PlanszaDoGry)
                print(f'\nKoniec gry, wygrał gracz" {gracz}')
                break
            elif PlanszaDoGry['9']==PlanszaDoGry['6']==PlanszaDoGry['3'] != ' ':
                drukujPlansze(PlanszaDoGry)
                print(f'\nKoniec gry, wygrał gracz" {gracz}')
                break
            # koniec wygranych pionowych
            elif PlanszaDoGry['7']==PlanszaDoGry['5']==PlanszaDoGry['3'] != ' ':
                drukujPlansze(PlanszaDoGry)
                print(f'\nKoniec gry, wygrał gracz" {gracz}')
                break
            elif PlanszaDoGry['1']==PlanszaDoGry['5']==PlanszaDoGry['9'] != ' ':
                drukujPlansze(PlanszaDoGry)
                print(f'\nKoniec gry, wygrał gracz" {gracz}')
                break
            # koniec wygranych przekątnych
            if  licznik == 9:
                print('\n Koniec gry\n Remis\n')

        if gracz == 'X':
            gracz = 'O'
        else:
            gracz = 'X'

    restart = input('Czy chcesz zagrać ponownie : (t/n) :')
    if restart == 't' or restart == "T":
        for key in klawiszeGry:
            PlanszaDoGry[key] = ' '
        gra()

if __name__ == '__main__':
    gra()










# drukujPlansze(PlanszaDoGry)

# %%
