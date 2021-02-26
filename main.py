import turtle as t

screen = t.Screen()
tim = t.Turtle()
tim.shape("arrow")

def decagono():
    for i in range(10):
        tim.right(36)
        tim.forward(50)

def eneagono():
    for i in range(9):
        tim.right(40)
        tim.forward(50)
    decagono()

def octogono():
    for i in range(8):
        tim.right(45)
        tim.forward(50)
    eneagono()

def heptagono():
    for i in range(7):
        tim.right(51)
        tim.forward(50)
    octogono()


def hexagono():
    for i in range(6):
        tim.right(60)
        tim.forward(50)
    heptagono()


def pentagono():
    for i in range(5):
        tim.right(72)
        tim.forward(50)
    hexagono()

def quadrado():
    for i in range(4):
        tim.right(90)
        tim.forward(50)
    pentagono()

def triangulo():
    for i in range(3):
        tim.right(120)
        tim.forward(50)
    quadrado()





triangulo()
screen.exitonclick()

