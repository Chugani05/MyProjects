import turtle
import random

screen = turtle.Screen()
screen.bgcolor("black")

t = turtle.Turtle()
t.speed(0)
t.width(2)

def draw_flower(x, y, petals, size, color):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(color)
    angle = 360 / petals
    for _ in range(petals):
        t.circle(size)
        t.right(angle)

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
for _ in range(10):
    x = random.randint(-300, 300)
    y = random.randint(-200, 200)
    petals = random.randint(5, 8)
    size = random.randint(30, 70)
    color = random.choice(colors)
    draw_flower(x, y, petals, size, color)

screen.mainloop()
