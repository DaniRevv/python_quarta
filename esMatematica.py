import math

# Se si sommano i primi n dispari è sempre un quadrato perfetto

n = int(input("Inserisci il numero di numeri dispari da moltiplicare -> "))
s = 0
for i in range(1, 2 * n + 1, 2):
    print(i)
    s += i

radiceIntera = math.isqrt(s)
print(f"La somma dei primi {n} numeri è {s}, quadrato perfetto: {radiceIntera ** 2 == s}")