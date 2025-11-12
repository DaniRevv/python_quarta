# Chiedere in input una stringa e verificare se è palindroma, letta sia a destra che a sinistra sia uguale

#parola = input("Scrivi una parola -> ")
#parola = parola.Lower()
#if parola == parola[::-1]: 
#    print("è palindroma")
#else: print("Non è palindroma")


# Chiedere all'utente un numero positivo e stampare i quadrati fino al numero scritto

#n = int(print("Inserisci un numero -> "))
#if n >= 0:
#    for i in range(n + 1):
#        print(i * i , end = " ") # i * i si puo anche scrivere i ** 2
#else: print("Il numero è negativo")


# Data una lista l di stringhe, scrivere un programma che scorra la lista e quando trova una parola che inizia con c la stampa

#l = ["ciao", "python", "casa"]

#for parola in l:
#    if parola[0] == 'c':
#        print(parola)


# Data una lista l di stringhe, produca una parola con gli elementi di l

l = ["ciao", "python", "casa"]
stringa = " "
for parola in l:
    stringa = stringa + " " + parola

print(stringa)

# E' uguale, però senza lo spazio iniziale:

l = ["ciao", "python", "casa"]
stringa = l[0]
for parola in l[1:]:
    stringa = stringa + " " + parola

print(stringa)



lista = ["Luca", "Mario", "Antonio"]
nomeMax = ""
lenMax = 0
for nome in lista:
    n = len(nome)
    if(n > lenMax):
        lenMax = n

print(nomeMax)