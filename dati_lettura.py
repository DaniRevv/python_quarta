file = open("./dati.csv", "r") # Oggetto file
righe = file.readlines() # Restituisce una lista di stringhe che contiene le righe
file.close()

# unpacking (=spacchettamento)
titolo1, titolo2, titolo3 = righe[0][:-1].split(",")
print(titolo1)

# Leggere tutte le altre righe del file e stamparle, usare un ciclo for pythonico (NO range)
