#!/usr/bin/python3
import sys
import os

def wciecia (n):
    for i in range(n+1):
        if (i==n):
            print('|---',end='')
        else:
            print('    ',end = '')

def listowanieKatalogu(m):
    n = m
    scierzka = os.getcwd()
    lista = os.listdir(scierzka)
    if len(lista) is not 0:
        for element in lista:
            n += 1
            wciecia(n)
            print(element)
            if os.path.isdir(element):
                os.chdir(element)
                listowanieKatalogu(n)
                os.system('cd ..')
            n -= 1

print('KATALOG\n')       
listowanieKatalogu(0)
print()
