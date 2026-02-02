# in Python tutto è un oggetto! anche int o float sono oggetti!
# Anche le funzioni sono oggetti

# Creare classi ci permette di creare nuovi oggetti

import math
import turtle

class Punto():
    # costruttore viene chiamato da Punto()
    def __init__(self, x, y): # self è come this. in java
        # Attributi (in Python tutto è pubblico)
        self.x = x
        self.y = y
    
    def  __str__(self):
        # deve returnare una stringa 
        return f"({self.x}, {self.y})"
    
    def distanza_origine(self):
        # ritorna la distanza dal punto dell'origine 1, 2
        return math.sqrt(self.x**2 + self.y**2)# ** vuol dire elevato

    def scambia_coordinate(self):
        # Questo metodo ritorna un nuovo punto con x e y scambiati
        return Punto(self.y, self.x)


    def disegna(self):
        # Questo metodo usa Turtle per disegnare il punto
        turtle.penup()
        turtle.goto(self.x, self.y)
        turtle.pendown()
        turtle.dot(10)

    def distanza(self, altro):
        # Questo metodo restituisce la distanza tra il punto e altro
        # altro è una istanza di un altro punto
        dx = self.x - altro.x
        dy = self.y - altro.y
        return math.sqrt(dx**2 + dy**2)

def main():
    a = Punto(100, 200)
    print(a)
    print(f"Il punto dista {a.distanza_origine():.2f} dall'origine")

    b = a.scambia_coordinate()
    print(f"{b}")

    a.disegna()

    dis = a.distanza(b)
    print(f"La distanza tra il punto A e B è {dis:.2f}")

    turtle.mainloop()


if __name__ == "__main__":
    main()