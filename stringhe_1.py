# In Python possiamo delimitare con "" oppure ''
stringa = "Ciao mondo!"
print(stringa)

# Esempio di indicizzazione della stringa
print(f"L'utlimo carattere della stringa è {stringa[-1]}")

# Esempio di slicing delle stringhe
print(f"La sottostringa 2-5 è {stringa[2:5]}.")
# L'indice di SINISTRA è incluso, quello di DESTRA è escluso

# Assegnazione multipla (vale per ogni tipo di dato)
nome, cognome = "Mario", "Rossi"

# Concatenazione tra stringhe
x = nome + " " + cognome
print(x)

# Concatenazione di una stringa con se stessa più volte
y = nome * 5
print(y)