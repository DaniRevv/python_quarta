def main():
    listaNomi = ["Alice", "Luca", "Giovanni", "Mario"]
    listaVoti = [[6, 7, 8], 
                [7, 3],
                [5, 6, 5],
                [1, 4, 2, 3]]
    # Voglio stampare il voto a fianco di ogni nome

    for nome, voti in zip(listaNomi, listaVoti):
        somma = 0
        nVoti = len(voti)
        votoMax = 0
        votoMin = 10

        for voto in voti:
            somma += voto

            if voto > votoMax:
                votoMax = voto
        
            if voto < votoMin:
                votoMin = voto

        media = somma / nVoti
        print(f"{nome}: media dei voti-> {media}, numero dei voti -> {nVoti}")
        print(f"Il voto maggiore è {votoMin}")
        print(f"Il voto minore è {votoMax}")


    # zip permette di ciclare in parallelo su due o piu liste

# Modificare il codice:
# stampare la media di ognuno
# stampare il numero di voti per ognuno
# stampare il voto massimo e il minimo

if __name__ == "__main__": # __ si chiama dunder
    main()