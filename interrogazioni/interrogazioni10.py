#file:
#GRUPPO , VALORE
#0 , 192
#1 , 168
#2 , 100
#3 , 1

file = open("./ip.csv", "r")
righe = file.readlines()
file.close()

d = {}

for riga in righe[1:]:
    campi = riga.split(",")
    d[int (campi[0])] = int (campi[0])
    