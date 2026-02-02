file = open("./nomeFile", "r")
contenuto = file.readline()
for riga in contenuto:
    if(riga[0] == '#'){
        print(riga)
    }
close(file)