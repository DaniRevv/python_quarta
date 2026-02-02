#Una lista contiene dizionari con chiavi titolo, autore, anno, prezzo. Scrivere funzioni
#per: (a) cercare libri di un autore, (b) calcolare il prezzo medio, (c) trovare il libro più recente.


libri = [
    {"titolo": "Il nome della rosa", "autore": "Umberto Eco", "anno": 1980, "prezzo": 15.50},
    {"titolo": "1984", "autore": "George Orwell", "anno": 1949, "prezzo": 12.00},
    {"titolo": "Il pendolo di Foucault", "autore": "Umberto Eco", "anno": 1988, "prezzo": 18.00},
    {"titolo": "Fahrenheit 451", "autore": "Ray Bradbury", "anno": 1953, "prezzo": 11.50},
    {"titolo": "Il mondo nuovo", "autore": "Aldous Huxley", "anno": 1932, "prezzo": 13.00}
    ]

libriTrovati = []

for libro in libri:
    if libro["autore"].lower() == "Umberto Eco":
        libriTrovati.append(libro["titolo"])

return libriTrovati




s = 0

for libro in libri:
    s += libro["prezzo"]

return s / len(libri)

        

nomeRecente = ""
dataRecente = 0

for libro in libri:
    if libro["anno"] > dataRecente:
        dataRecente = libro["anno"]
        nomeRecente = libro["titolo"]





























def cercaLibri(libri, nome):
    libriTrovati = []

    for libro in libri: #ogni libro è un dizionario
        if libro["autore"].lower() == nome.lower():
            libriTrovati.append(libro["titolo"])

    return libriTrovati


def calcolaMedia(libri):
    s = 0

    for libro in libri:
        s += libro["prezzo"]

    return s/len(libri)


def cercaRecente(libri):

    recente = libri[0]["anno"]
    nome = libri[0]["titolo"]

    for libro in libri:
        if libro["anno"] > recente:
            recente = libro["anno"]
            nome = libro["titolo"]

    return nome


def main():

    libri = [
    {"titolo": "Il nome della rosa", "autore": "Umberto Eco", "anno": 1980, "prezzo": 15.50},
    {"titolo": "1984", "autore": "George Orwell", "anno": 1949, "prezzo": 12.00},
    {"titolo": "Il pendolo di Foucault", "autore": "Umberto Eco", "anno": 1988, "prezzo": 18.00},
    {"titolo": "Fahrenheit 451", "autore": "Ray Bradbury", "anno": 1953, "prezzo": 11.50},
    {"titolo": "Il mondo nuovo", "autore": "Aldous Huxley", "anno": 1932, "prezzo": 13.00}
    ]

    #ricerca delle opere di un autore
    nome = input("Inserisci il nome dell'autore -> ")
    libriTrovati = []
    libriTrovati = cercaLibri(libri, nome)
    print(f"L'autore da te inserito ha scritto queste opere: {libriTrovati}")

    #calcolo della media
    media = calcolaMedia(libri)
    print(f"Il prezzo medio è -> {media}")

    #cerca del libro piu recente
    nome = cercaRecente(libri)
    print(f"Il libro più recente è -> {nome}")

if __name__ == "__main__":
    main()

    
