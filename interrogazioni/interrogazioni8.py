# Stampare il voto dell'alunno con il voto piu alto

voti = {"Luca" : 7, "Marco" : 8, "Giovanni" : 6}
max = 0
alunno = ""
for i in voti:
    if voti[i] > max:
        max = voti[i]
        alunno = i

print(alunno)