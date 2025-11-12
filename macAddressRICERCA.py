def main():
    file = open("./mac-vendors-export.csv", "r", encoding = 'utf-8')

    righe = file.readlines()
    file.close()

    mac =  "C0-4B-24" # input("Inserisci il MAC address -> ")
    for riga in righe:
        if riga[0:8] == mac:
            print(riga)


if __name__ == "__main__": # __ si chiama dunder
    main()