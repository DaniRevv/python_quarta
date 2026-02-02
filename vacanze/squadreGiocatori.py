#Un dizionario associa nomi di squadre a liste di giocatori. Scrivere funzioni per: (a)
#trovare la squadra con più giocatori, (b) verificare se un giocatore è in una squadra, (c)
#trasferire un giocatore da una squadra all’altra.

def squadraMaxGiocatori(lista):
    numeroMax = 0
    nomeMax = ""
    for squadra in lista:
        if numeroMax < len(lista[squadra]):
            numeroMax = len(lista[squadra])
            nomeMax = squadra

    return nomeMax


def cercaGiocatore(lista, nome):
    for squadra in lista:
        for giocatore in lista[squadra]:
            if giocatore.lower() == nome.lower():
                return True

    return False

def trasferisciGiocatore(lista, nomeGiocatore, nomeSquadra):
    for squadra in lista:
        if squadra.upper() == nomeSquadra.upper():
            lista[squadra].append(nomeGiocatore)
            return lista[squadra]
        
    return False

def main():
    squadre = {
    "Juventus": ["Vlahovic", "Chiesa", "Locatelli", "Bremer"],
    "Inter": ["Lautaro", "Thuram", "Barella", "Bastoni", "Calhanoglu"],
    "Milan": ["Leao", "Theo", "Reijnders"]
    }

    nomeSquadra = squadraMaxGiocatori(squadre)
    print(nomeSquadra)

    if cercaGiocatore(squadre, "lautaro"):
        print("Giocatore presente")
    else:
        print("Giocatore non presente")

    nuovaSquadra = trasferisciGiocatore(squadre, "Leao", "Juventus")
    print(nuovaSquadra)

if __name__ == "__main__":
    main()