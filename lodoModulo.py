import turtle

def sposta(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()


def poligono(lati, lung):
    angolo = 360 / lati

    for i in range(lati):
        turtle.forward(lung)
        turtle.left(angolo)


def main():
    nPoligoni = 4
    lunghezzaLato = 80
    shift = 180
    x0, y0 = -350, -lunghezzaLato/2

    for i in range(nPoligoni):
        y = y0
        x = x0 + shift * i
        sposta(x, y)
        poligono(i + 3, lunghezzaLato)
    


    turtle.mainloop()

if __name__ == "__main__":
    main()