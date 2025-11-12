import math


# pag.55 es.10

liste_voti = [2, 3, 4, 5, 6, 7, 8]

print(liste_voti[1:-1])

for elemento in liste_voti:
    if liste_voti[4]:
        print(10)

    else: print(elemento)

print(f"I primi tre voti sono: {liste_voti[0], liste_voti[1], liste_voti[2]}")


# pag.73 es.3

sel = int(input("SCEGLI: 0 SOMMA, 1 SOTTRAZIONE, 2 MOLTIPLICAZIONE, 3 DIVISIONE -> "))

a = int(input("Inserisci il primo numero -> "))
b = int(input("Inserisci il secondo numero -> "))

if sel == 0:
    ris = a + b
elif sel == 1:
    ris = a - b
elif sel == 2:
    ris = a * b
elif sel == 3:
    ris = a / b

print(f"Il sirultato è {ris}")


# pag.73 es.4

print("I quadrati perfetti minori di 200 sono: ")
quadrati = 0

for n in range(0, 200):
    radice = math.isqrt(n) 
    if radice * radice == n:
        quadrati += 1

print(quadrati)

        