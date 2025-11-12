n = int(input("Quanti numeri di Fibonacci vui? -> "))
a, b = 1, 1 #inizializzazione NON dichiarazione!!!

if n > 4:

    for i in range(n - 4):
        print(a, end = " - ")
        print(b, end = " - ")
        a, b = a + b, a + b + b
elif n == 3:
    print(a, end = " - ")
    print(b, end = " - ")
    a = a + b
    print(a, end = " - ")

elif n == 2:
    print(a, end = " - ")
    print(b, end = " - ")

elif n == 1:
    print(a)

elif n == 0:
    print("Hai inserito 0")