# L'utente inserisce in input una password
# Stampa tutti altri asterischi tranne la prima

password = input("Inserisci una password -> ")
password_blanked = password[0] + '*' * (len(password) - 1)
print(f"Hai inserito la password: {password_blanked}")

# Stampa tutti altri asterischi tranne la prima e l'ultima
password = input("Inserisci una password -> ")
password_blanked = password[0] + '*' * (len(password) - 2) + password[-1]
print(f"Hai inserito la password: {password_blanked}")