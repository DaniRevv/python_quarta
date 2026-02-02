import random

# primo giocare vince se esce pari, secondo se esce dispari

def generaNumeri(nPartite):
    lanci = []

    for i in range(nPartite):
        lanci.append(random.randint(0, 5))

    return lanci

def main():

    nPartite = int(input("Inserisci il numero di partite -> "))

    giocatore1 = input("Inserisci il nome del primo giocatore -> ")
    giocatore2 = input("Inserisci il nome del secondo giocatore -> ")

    diz = {giocatore1: generaNumeri(nPartite), giocatore2: generaNumeri(nPartite)}

    vincitori = []

    for i in range(nPartite):
        if(diz[giocatore1][i] + diz[giocatore2][i] & 2 == 0):
            vincitori.append(giocatore1)
        else:
            vincitori.append(giocatore2)
        
    print(vincitori)

if __name__ == "__main__": 
    main()





