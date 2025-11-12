# Crea un programma in python che chiede all'utente il suo nome 
# E lo stampa sempre con l'iniziale maiuscola e il resto tutto minuscolo

nome = input("Inserisci il nome -> ")
nome = nome.lower()
nome = nome.upper()[0] + nome[1:]
rint(f"Il nome con l'iniziale maiuscola è: {nome}")



# Crea un programma in python che chiede all'utente un numero intero 
# E stampa se il numero è divisibile per 2, per 3 o per 5. (Hint: usare operatore % per il resto della divisione)

n = int(input("Inserisci un numero intero -> "))
if n % 2 == 0:
    print("Il numero è divisibile per 2")
elif n % 3 == 0:
    print("Il numero è divisibile per 3")
elif n % 5 == 0:
   print("Il numero è divisibile per 5")

else:
    print("Il numero non è divisibie ne con 2, ne 3, ne con 5")




# Crea un programma in python che chiede all'utente una frase e stampi la stringa un carattere si e uno no (caratteri altrernati)

frase = input("Inserisci una frase -> ")
print(f"La frase un carattere si e uno è {frase[0::2]}")     # Vuol dire che dal carattere numero 0 stampa i caratteri in posizione pari



# Crea un programma in python che chiede all'utente una frase e la stampi al contrario

frase = input("Inserisci una frase -> ")
print(f"La frase al contrario è {frase[::-1]}")   # Vuol dire che prende tutta la stringa e la stampa al contrario
                                                  # Se metto 1 me la ristampa uguale