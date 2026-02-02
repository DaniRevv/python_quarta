# Data una lista, restituire una nuova lista contenente gli stessi elementi ma senza duplicati,
# mantenendo l’ordine di prima apparizione.

elementi = ["mela", "pera", "mela", "banana", "pera", "arancia", "mela"]
singoli = []
duplicati = []

for e in elementi:
    if e in singoli:
        duplicati.append(e)
    else:
        singoli.append(e)

print(singoli)