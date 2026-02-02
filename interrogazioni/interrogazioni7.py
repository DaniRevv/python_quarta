# 'A0-CC-A1'
# 'A0-DA-A2'

def trova(mac1, mac2)
elemento = 0
elemento1 = indirizzo1.split("-")
elemento2 = indirizzo2.split("-")

for indirizzo1, indirizzo2 in zip.(mac1, mac2):
    if indirizzo1 == indirizzo2:
        print(indirizzo1)
        uguali += 1