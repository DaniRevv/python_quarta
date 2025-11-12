# MODULARITA': suddividere il codice in funzioni.

# COSTANTE è una variabile globale
# ATTENZIONE: COSTANTE è accessibile da tutte le funzioni soltanto in lettura

COSTANTE = 3.14

def primaLetteraMaiuscola(stringa):
    # DOCUMENTAZIONE DELLA STRINGA
    """ 
    La funzione restituisce stringa con la lettera maiuscola
    """
    # stringa è una variabile locale alla funzione 
    s = stringa[0].upper() + stringa[1:].lower()
    return s

def media(lista):
    """
    La funzione restituisce la media dei valori presenti in lista e il numero di elementi di lista 
    """
    somma = 0.
    nLista = len(lista)
    for val in lista:
        somma += val

    return somma / nLista, nLista


def main():
    # print(help(primaLetteraMaiuscola))

    #nome = input("Inserisci una parola -> ")
    #print(primaLetteraMaiuscola(nome))

    voti = [4.5, 10, 8.25, 7, 6]
    m, n = media(voti)

    print(f"La media dei voti è {m} e il numero di voti è {n}")
    if m >= 6:
        print("Sei sufficiente")
    else: print("Sei insufficiente")

if __name__ == "__main__":
    main()