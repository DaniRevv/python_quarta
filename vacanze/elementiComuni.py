#Date due liste, restituire una nuova lista con gli elementi presenti in entrambe.

def trovaComuni(lista_a, lista_b):
    listaNuova = []
    for a in lista_a:
            if a in lista_b:
                listaNuova.append(a)

    return(listaNuova)


def trovaComuni2(lista_a, lista_b):
    listaNuova = []
    for a in lista_a:
        for b in lista_b:
            if b == a:
                listaNuova.append(b)

    return(listaNuova)

def main():
    lista_a = [1, 5, 8, 12, 15, 20]
    lista_b = [3, 5, 10, 12, 18, 20, 25]
    listaNuova = []
    listaNuova = trovaComuni(lista_a, lista_b)
    print(listaNuova)

if __name__ == "__main__":
    main()

