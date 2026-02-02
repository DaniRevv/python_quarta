# Secondo massimo
# Scrivere una funzione che trovi il secondo valore più grande in una lista di numeri (senza
# usare sort o sorted).

valori = [45, 12, 78, 34, 67, 23, 89, 56]

max = valori[0]
min = valori[0]

for v in valori:
    if v > max:
        max = v
    if v < min:
        min = v

# assegno a secondo massimo il valore piu piccolo dell'arrey, per essere sicuro che il valore 0 non sia il maggiore
secondoMax = min

for v in valori:
    if (v > secondoMax) and (v != max):
        secondoMax = v 

print(secondoMax)