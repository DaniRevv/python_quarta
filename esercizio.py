# Chiedere all'utente un nummero intero, un carattere e creare un stringa con il carattere ripetuto n volte, cioè l'input

n = int(input("Quante volte vuoi ripetere una parola -> "))
carattere = input("Inserisci la parola -> ")

stringa = (carattere + " ") * n
print(stringa)