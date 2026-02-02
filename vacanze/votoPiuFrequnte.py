# Dato un dizionario che associa nomi di studenti ai loro voti (un voto per studente),
# trovare quale voto compare più spesso.

studenti_voti = {
"Marco": 7,
"Sara": 8,
"Luca": 6,
"Elena": 8,
"Paolo": 7,
"Giulia": 8,
"Andrea": 6,
"Chiara": 7
}

frequenze = {}

for studente in studenti_voti:
    voto = studenti_voti[studente]
    if voto in frequenze:
        frequenze[voto] += 1
    else:
        frequenze[voto] = 1

maxFrequenza = 6

for frequenze[voto] in frequenze:
    if frequenze[voto] > maxFrequenza:
        maxFrequenza = frequenze[voto]

print(f"Il voto più frequente è: {maxFrequenza}")