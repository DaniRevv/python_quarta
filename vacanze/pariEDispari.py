#Data una lista di interi, scrivere una funzione che restituisca due liste separate: una con
#i numeri pari e una con i dispari.

def separaParieDispari(lista):
    lP = []
    lD = []

    for numero in lista:
        if numero % 2 == 0:
            lP.append(numero)
        else:
            lD.append(numero)
    
    return lP, lD


def main():
    numeri = [3, 8, 12, 7, 2, 15, 20, 9, 4]

    lPari, lDispari = separaParieDispari(numeri)
    print(lPari, lDispari)


if __name__ == "__main__":
    main()