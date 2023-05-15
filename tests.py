from scripts.characters.Ball import Ball
from scripts.models.Element import Element
from scripts.utils.Vector import Vector

ball = Element()

ball.speed = Vector(10, 0)
ball.acceleration = Vector(1, 0)

cont = 10
while cont > 0:
    cont -= 1
    ball.update()

print(ball)

