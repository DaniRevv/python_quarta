# Data una stringa, costruire un dizionario che associ a ogni carattere il numero di volte
# che compare.

testo = "abracadabra"
caratteri = {}

for carattere in testo:
    if carattere in caratteri:
        caratteri[carattere] += 1
    else:
        caratteri[carattere] = 1

print(caratteri)

