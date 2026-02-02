import turtle

def main():
    file = open("./logoMiniLinguaggio.csv", "r")
    righe = file.readlines()
    file.close()

    comandi = []
    k = 0

    for riga in righe:
        campi = riga.append(" ")
        campi[0] = comandi[k]
        k += 1

    if comandi == "avanti":
        turtle.forward(100)

    if comandi == "destra":
        turtle.right(90)

    # rosso
    #if comandi == ""

    # salta 

    # cerchio

    print(comandi)

    turtle.mainloop()

if __name__ == "__main__":
    main()