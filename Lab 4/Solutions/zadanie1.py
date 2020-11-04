#!/usr/bin/python
from decimal import Decimal

class Node:
    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data

    def PrintTree(self):
        print(self.data, end = " ")
        if self.left:
            self.left.PrintTree()
        
        if self.right:
            self.right.PrintTree()
        
    

     

def nawiasy(wyrazenie):

    elem = []
    otw = 0
    zam = 0
    odp = []
    isAdded = False

    for i in range (len(wyrazenie)):
        if not isAdded:
            if (wyrazenie[i] != '(' and otw == 0):
                odp.append(wyrazenie[i])
            elif (wyrazenie[i] == "(" and otw == 0):
                otw += 1
            elif (wyrazenie[i] == "("):
                elem.append(wyrazenie[i])
            elif (otw > 0 and wyrazenie[i] != ")"):
                elem.append(wyrazenie[i])
            elif (wyrazenie[i] == ")"):
                zam += 1
                if (otw == zam):
                    odp.append(elem)
                    isAdded = True
                else:
                    elem.append(")")
        else:
            odp.append(wyrazenie[i])
    return odp


def simplifyTheMath(wyrazenie):
    ifContains = False
    if  '(' in wyrazenie:
        ifContains = True
    i = 0
    while ifContains:
        wyrazenie = nawiasy(wyrazenie)
        ifContains = False
        if '(' not in wyrazenie:
            ifContains = False
        i += 1
    return wyrazenie


def toTree(wyrazenieFIRST):

    def share(wyrazenie, index):
        return (wyrazenie[:(index)], wyrazenie[index], wyrazenie[(index+1):])


    def findIndex(wyrazenie):
        pIndex = -1
        minIndex = -1
        mIndex = -1
        dIndex = -1
    
        if type(wyrazenie[0]) == list:
            wyrazenie = wyrazenie[0]
        wyrazenie.reverse()

        if '+' in wyrazenie:
            pIndex = len(wyrazenie) - 1 - wyrazenie.index('+') 
        if '-' in wyrazenie:
            minIndex = len(wyrazenie) - 1 - wyrazenie.index('-')
        if '*' in wyrazenie:
            mIndex = len(wyrazenie) - 1 - wyrazenie.index('*')
        if '/' in wyrazenie:
            dIndex = len(wyrazenie) - 1 -  wyrazenie.index('/')
        wyrazenie.reverse()
        if pIndex == -1 and mIndex == -1 and minIndex == -1 and dIndex == -1:
            return -1
        if pIndex != -1 and minIndex != -1:
            if pIndex < minIndex:
                return minIndex
            else:
                return pIndex
        if pIndex != -1:
            return pIndex
        if minIndex != -1:
            return minIndex

        if dIndex != -1 and mIndex != -1:
            if dIndex < mIndex:
                return mIndex
            else:
                return dIndex
        if dIndex != -1:
            return dIndex
        if mIndex != -1:
            return mIndex


    def tree(node):
        node.data = simplifyTheMath(node.data)
        if findIndex(node.data) != -1:
            TTree = share(node.data, findIndex(node.data))
            operation = node.data[findIndex(node.data)]
            node.data = operation
            node.left = Node(TTree[0])
            tree(node.left)
            node.right = Node(TTree[2])
            tree(node.right)


    def licz(node):
        if node.data == "+":
            return licz(node.left) + licz(node.right)
        if node.data == "-":
            return licz(node.left) - licz(node.right)
        if node.data == "*":
            return licz(node.left) * licz(node.right)
        if node.data == "/":
            return licz(node.left) / licz(node.right)
        else:
            value = node.data[0]
            node.data = node.data[0]
            return Decimal(value)

    root = Node(wyrazenieFIRST)
    tree(root)
    wynik = licz(root)
    print('WYNIK = ', end = " ")
    print(wynik)
    print('DRZEWO')
    root.PrintTree()



if __name__ == "__main__":

    wyrazenie = input("Podaj wyrazenie ze spacjami: ")
    print(wyrazenie)
    wyrazenie = wyrazenie.split(" ")
    toTree(wyrazenie)
    print()
