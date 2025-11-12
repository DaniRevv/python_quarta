def main():
    file = open("./mac-vendors-export.csv", "r", encoding = 'utf-8')

    righe = file.readlines()
    file.close()

    macAddress =  []
    vendor = []
    for riga in righe[1:]:
        campi = riga.split(",") #per ogni riga ho una lista di campi
        macAddress.append(campi[0])
        vendor.append(campi[1])

    mac = input("Inserisci il MAC address per intero -> ").upper()
    for m, v in zip(macAddress, vendor):
        if m[0:8] == mac[0:8]:
            print(f"Il produttore è {v}")




if __name__ == "__main__": # __ si chiama dunder
    main()