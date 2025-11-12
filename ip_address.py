ip = input("Inserisci un indirizzo IP -> ")
# .split è un metodo delle stringhe che suddivide una stringa cercando il carattere il carattere separatore SEP
ottetti_str = ip.split(".") 
print(ottetti_str)

ottetti = [] # lista vuota

for s in ottetti_str:
    ottetti.append(int(s))

for numero in ottetti:
    print(bin(numero)[2:])

# per togliere il 0b dopo aver convertito il numero in binario [2:]

# Chiedere all'utente il numero di bit e chiede un numero binario gestito come stringa, se la lung del numero binario è minore del
# numero di bit aggiungi tanti zeri quanti mancano per raggiungere 8

