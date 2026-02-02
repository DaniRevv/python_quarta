def leggi_registro(nome_file):
    """Restituisce un dizionario {nome: [voti]}."""
    righe = nome_file.readlines()
    dizionario = {}

    for riga in righe:
        campi = riga.split(";")
        nome = campi[0] 
        voti = []

        for voto in campi[1:]:
            voti.append(int(voto))

        dizionario[campi[0]] = voti

    print(dizionario)
    exit()
    return dizionario

def calcola_media(voti):
    """Restituisce la media di una lista di voti."""
    return sum(voti)/len(voti)

def classifica(registro):
    """
    Restituisce una lista di tuple (nome, media) 
    ordinata per media decrescente.
    """
    
    listaVoti = []
    for nome in registro:
        listaVoti.append((nome, calcola_media(registro[nome])))

    listaOrdinata = sorted(listaVoti)

    return registro

def stampa_podio(classifica):
    """Stampa i primi 3 della classifica (usa slicing)."""
    print(classifica[0:3])

def trova_insufficienti(classifica):
    """Restituisce la lista degli studenti con media < 6."""
    insufficienti = []
    for nome, media in classifica:
        if media < 6:
            insufficienti.append((nome, media))
            
    return insufficienti

def main():
    file = open("registro.txt", "r")
    dizionario = leggi_registro(file)
    file.close()
    voti = dizionario["Binachi Mario"]

    media = calcola_media(voti)
    print(media)
    
    classifica_studenti = classifica(registro)

    stampa_podio(classifica_studenti)

    elenco_insufficienti = trova_insufficienti(classifica_studenti)
    print(f"\nStudenti insufficienti: {len(elenco_insufficienti)}")
    for nome, media in elenco_insufficienti:
        print(f"{nome}: {media:.2f}")

if __name__ == "__main__":
    main()