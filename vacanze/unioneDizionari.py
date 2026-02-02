# Dati due dizionari, crearne uno nuovo che contenga tutte le chiavi. Se una chiave è
# presente in entrambi, sommare i valori.

def unisciDizionari(vG, vF):
    nD = {}

    for prodotto in vG:
        nD[prodotto] = vG[prodotto]

    for prodotto in vF:
        if prodotto in nD:
            nD[prodotto] += vF[prodotto]
        else:
            nD[prodotto] = vF[prodotto]

    return nD


def main():
    vendite_gennaio = {"mele": 120, "pere": 85, "arance": 200}
    vendite_febbraio = {"mele": 95, "banane": 150, "arance": 180}

    nuovoDizionario = unisciDizionari(vendite_gennaio, vendite_febbraio)
    print(nuovoDizionario)

if __name__ == "__main__":
    main()

        
