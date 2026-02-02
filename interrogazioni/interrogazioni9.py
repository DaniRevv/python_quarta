# creare un IP unico

dizionario = {0 : 192, 1 : 168, 2 : 100, 3 : 1}
ip = ""

for i in dizionario:
    ip += str(dizionario[i]) + "."

print(ip[:-1])