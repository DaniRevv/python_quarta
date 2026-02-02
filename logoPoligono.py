import turtle

# chiedere un numero intero n e disgnare il poligono regolare di n lati

def main():
    lati = 0
    
    while(lati < 2):
        lati = int(input("Inserisci un numero -> "))

    for lato in range(lati):
        turtle.forward(70)
        turtle.right(360/lati)

    turtle.mainloop()

if __name__ == "__main__":
    main()