def main():
    # un dizionario python è una sequenza di coppie chiave:valore
    elenco = {"A3-32-B4-FF-F4-32": "Luca", "65-A0-AA-11-F4-19":  "Mario"} # prima parte chiave(i numeri), la seconda valore(nomi)
    mac = "A3-32-B4-FF-F4-32"
    if mac in elenco: # controllo sula chiave
        print(elenco[mac]) # la ricerca si puo fare sulla chiave
    else:
        print("MAC non trovato")
    # Aggiungiamo un nuovo elemento al dizionario
    elenco["FF-FF-FF-FF-FF-FF"] = "broadcast"
    print(elenco)
    
    

if __name__ == "__main__":
    main()