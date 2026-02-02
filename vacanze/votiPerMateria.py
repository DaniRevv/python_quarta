#Un dizionario associa nomi di materie a liste di voti. Scrivere funzioni per: (a) calcolare
#la media di una materia, (b) trovare la materia con media più alta, (c) aggiungere un
#voto a una materia.

def calcolaMedia(voti_materie, cerca):
    voti = voti_materie[cerca]
    somma = 0

    for voto in voti:
        somma += voto

    return somma / len(voti)


def mediaPiuAlta(lista):
    medie = []
    max = 0
    nMateria = ""

    for materia in lista:
        somma = 0
        for voto in lista[materia]:
            somma += voto

        media = somma / len(lista[materia])
        if max < media:
            max = media
            nMateria = materia

    return max, nMateria


def addVoto(lista, addMateria, addVoto):
    for materia in lista:
        if materia.upper() == addMateria.upper():
            lista[materia].append(addVoto)
            return lista[materia]

    return 0

def main():
    voti_materie = {
    "Matematica": [6, 7, 5, 8, 7],
    "Italiano": [7, 8, 7, 6],
    "Inglese": [8, 8, 9, 7, 8],
    "Informatica": [9, 8, 9, 10, 8]
    }

    media = calcolaMedia(voti_materie, "Matematica")
    print(media)

    mediaHigh, materiaHigh = mediaPiuAlta(voti_materie)
    print(mediaHigh, materiaHigh)

    listaNuova = addVoto(voti_materie, "Inglese", 4)
    print(listaNuova)

if __name__ == "__main__":
    main()