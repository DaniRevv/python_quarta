a = input("Inserisci una stringa -> ")
n = int(input("Inserisci un numero -> "))

lunghezza = len(a)

if lunghezza >= n:
    asterisco = lunghezza - n
    modificata = a[lunghezza] + ('*' * asterisco)
    print(f"La frase è {modificata}")