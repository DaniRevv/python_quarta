#stampa tutti ig gruppi diversi da FF

m = 'A0-FF-51-B3-D1-FF'
m2 = m.split("-")
for c in m2:
    if c != "FF":
        print(c)