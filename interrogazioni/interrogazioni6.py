#luca, A5-B2-45
#antonio, .....

file = open("./elenco.csv", "r")

mac = input("Inserisci un MAC -> ")
righe = file.readlines()
trovato = false
for elemento in riga:
    riga = elemento.split(",")
    if mac == riga[1]:
        print(riga[0])
        trovato = true

if trovato: 
    print("MAC trovato")
else:
    print("MAC non trovato")