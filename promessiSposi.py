alfabeto = "abcdefghijklmnopqrstuvwxyz"

def stampaFrequenze(lettere):
    """La funzione stampa le frequenze delle lettere fornite.
    Input:
        - dizionario: contiene le frequenze assolute per tutte le lettere
        - alfabeto: stringa contenente le lettere di interesse
    Output:
        - none
    """

    for lettera in alfabeto:
        if lettera in lettere:
            print(f"{lettera} - {lettere[lettera]} - {percentuali[lettera]:.2f}")
        else:
            print(f"{lettera} - 0,00%")

    for lettera in lettere:
        print(f"{lettera} - {lettere[lettera]}")

def calcolaPercentuale(lettere, nLettere):
    # Calcoliamo percentuali usando una COMPREHENSION
    percentuali = {lettera: (lettere[lettera] * 100) / nLettere for lettera in lettere}

def main():
    print("Apertura file...")
    file = open("./testo.txt", "r", encoding = "utf-8")
    testo = file.read()
    file.close()
    print(f"Letti {len(testo)} caratteri.")
    print()

    lettere = {}
    nLettere = 0

    print("=" * 78)

    for riga in testo:
        minuscola = riga.lower()
        for carattere in minuscola:
            if str.isalpha(carattere) and carattere in alfabeto:
                if carattere in lettere:
                    lettere[carattere] += 1
                    nLettere += 1
                else:
                    lettere[carattere] = 1
                    nLettere += 1

    stampaFrequenze(nLettere, lettere)

    # Calcoliamo percentuali usando una COMPREHENSION

    percentuali = calcolaPercentuale(lettere, nLettere)
    stampaFrequenze(lettere, percentuali)

    print("=" * 78)


if __name__ == "__main__":
    main()