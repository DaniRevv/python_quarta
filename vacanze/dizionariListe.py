#Un dizionario associa nomi di studenti a liste di date (stringhe) in cui erano presenti.
#Scrivere funzioni per: (a) contare le presenze di uno studente, (b) trovare chi ha più
#presenze, (c) trovare chi era presente in una certa data.

def contaPresenze(nome, presenze):
    date = presenze[nome]
    n = len(date)

    return n

def piuPresenze(presenze):
    max = 0
    maxNome = ""

    for studente in presenze:
        nDate = len(presenze[studente])
        if nDate > max:
            max = nDate
            maxNome = studente

    return maxNome

def presenti(presenze, data):
    alunniPresenti = []

    for studente in presenze:
            if data in presenze[studente]:
                alunniPresenti.append(studente)

    return alunniPresenti

def main():
    
    presenze = {
    "Marco": ["2024-01-10", "2024-01-11", "2024-01-12", "2024-01-15"],
    "Sara": ["2024-01-10", "2024-01-12", "2024-01-15", "2024-01-16", "2024-01-17"],
    "Luca": ["2024-01-10", "2024-01-11"],
    "Elena": ["2024-01-10", "2024-01-11", "2024-01-12", "2024-01-15", "2024-01-16"]
    }

    nPresenze = contaPresenze("Marco", presenze)
    print(nPresenze)

    nome = piuPresenze(presenze)
    print(f"L'alunno con più presenze è: {nome}")
    
    alunniPresenti = []
    alunniPresenti = presenti(presenze, "2024-01-11")
    print(f"Gli alunni presenti sono: {alunniPresenti}")

if __name__ == "__main__":
    main()