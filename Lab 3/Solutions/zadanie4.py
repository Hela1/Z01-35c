#!/usr/bin/python3
import sys, random, os

wygrane = 0
przegrane = 0
remis = 0

papierKamienNozyce = ['P', 'K', 'N']
print('Witaj!\n')
czyGra = input('Zagramy? (t-TAK n-NIE)\n')
if czyGra.upper() == 'T':
    ileGier = int(input('Podaj ilość rund :'))
    for i in range(ileGier):
        ruchGracza = input('1... 2... 3... \t(P-papier, K-kamień, N-nozyce) ')
        ruchKomputera = random.choice(papierKamienNozyce)
        print("KOMPUTER: \t" + ruchKomputera)
        switcher = {
            ('K', 'K'): 'REMIS',
            ('P', 'P'): 'REMIS',
            ('N', 'N'): 'REMIS',
            ('K', 'N'): 'WYGRANA',
            ('N', 'P'): 'WYGRANA',
            ('P', 'K'): 'WYGRANA',
            ('K', 'P'): 'PRZEGRANA',
            ('P', 'N'): 'PRZEGRANA',
            ('N', 'K'): 'PRZEGRANA'

        }
        if switcher.get((ruchGracza.upper(), ruchKomputera)) == 'REMIS':
            print("\t\t\t Ta runda zakończyła się remisem...\n")
            remis += 1
        elif switcher.get((ruchGracza.upper(), ruchKomputera)) == 'WYGRANA':
            print("\t\t\t Tę rundę udało ci się wygrać...\n")
            wygrane += 1
        elif switcher.get((ruchGracza.upper(), ruchKomputera)) == 'PRZEGRANA':
            print("\t\t\t Przegrałeś, smuteczek\n")
            przegrane += 1
        else:
            print("Błąd")

    if (wygrane > przegrane): print('Wygrana!')
    elif (wygrane == przegrane): print('Remis!')
    else: print('Przegrana!')
    print('Do zobaczenia kiedyś...\n')

else:
    print('Do zobaczenia kiedyś...')
