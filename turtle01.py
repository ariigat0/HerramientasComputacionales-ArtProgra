from turtle import*
import math

speed(1)

#Tortuga
color('red')
fillcolor('green')

s=200 #tamaño de cuadrado

#Cuadrado
for i in range(4):
    fd(s)
    left(90)

#Triángulo
theta=63.44
r=math.sqrt((s**2)+((s/2)**2))
left(theta)
fd(r)
rt(theta*2)
fd(r)
rt(theta*2)

#Circulo

done()