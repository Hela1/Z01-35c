#!/usr/bin/python3
import sys, os

if len(sys.argv) == 3:
    obecnaSciezka = os.getcwd()
    os.chdir(sys.argv[2])
    komenda = 'ls ./*' + str(sys.argv[1])
    os.system(komenda)
    os.chdir(obecnaSciezka)

else:
    print("Błędna liczba algorytmów!")
