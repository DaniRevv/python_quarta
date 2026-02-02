def main():
    file = open("./mac-vendors-export.csv", "r", encoding = "utf-8")
    righe = file.readlines() # righe è una lista di stringhe
    file.close()

    elenco = {}

    for riga in righe[1:]: # riga è una stringa
        campi = riga.split(",") # campi è una lista di stringhe
        elencoMac[campi[0]] = campi[1]
        elencoData[campi[1]] = campi[4]


    cercaMac = input("Inserisci il MAC da cercare -> ")

    if cerca in elenco:
        print(f"Il vendor del MAC: {cerca}, è {elencoMac[cerca]}")
    else:
        print(f"Il MAC {cerca} non è presente nell'elenco")

if __name__ == "__main__":
    main()