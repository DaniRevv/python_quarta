n = int(input("Quanti numeri di Fibonacci vui? -> "))
a, b = 1, 1 #inizializzazione NON dichiarazione!!!

if n > 2:

    for i in range(n):
        print(a, end = " - ")
        a, b = b, a + b 

elif n == 0:
    ("Nessun numero inserito")