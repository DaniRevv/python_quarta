# attributi: lato, x, y del vertice di un lato a sinistra
# funzioni: area, perimetro, disegna(colore pieno)
# disegna 100 quadrati casuali

import turtle
import random

class Quadrato():
    def __init__(self, x, y, lato, colore): # self è come this. in java
        # Attributi (in Python tutto è pubblico)
        self.x = x
        self.y = y
        self.lato = lato
        self.colore = colore

    def __str__(self):
        return f"({self.x}, {self.y}, {self.lato}, {self.colore})"
    
    def area(self):
        return self.lato**2
    
    def perimetro(self):
        return self.lato * 4
        
    def disegna(self):
        turtle.penup()
        turtle.goto(self.x, self.y)
        turtle.pendown()
        turtle.fillcolor(self.colore) 

        turtle.begin_fill() 
        for _ in range(4):
            turtle.forward(self.lato)
            turtle.right(90)
        turtle.end_fill()

    def casuali(self):
        for _ in range(100):
            
            turtle.penup()
            turtle.goto(random.randint(0, 250), random.randint(0, 250))
            turtle.pendown()
            for _ in range(4):
                turtle.forward(self.lato)
                turtle.right(90)
        



def main():
    q = Quadrato(3, 4, 10, "blue")

    a = q.area()
    print(f"Area: {a}")

    p = q.perimetro()
    print(f"Perimetro: {p}")

    q.disegna()

    turtle.speed(0)
    COLORI = ["red", "blue", "green", "yellow"]
    for _ in range(100):
        colore = (random.random(), random.random(), random.random())
        #colore = random.choice(COLORI)
        lato = random.randint(10, 40)
        x = random.randint(-300, 300)
        y = random.randint(-200, 200)
        quadrato = Quadrato(x, y, lato, colore)
        quadrato.disegna()

    turtle.mainloop()



if __name__ == "__main__":
    main()