#Ejercicio 3 de Guia Lab

x = int(input("Ingrese el ángulo1: "))
y = int(input("Ingrese el ángulo2: "))
z= 180 - (x+y)

if x == 90 or y == 90 or z==90:
    print("Es un triángulo rectángulo")
elif x < 90 and y < 90 and z < 90:
    print("Es un triángulo acutángulo")
elif x > 90 or y > 90 or z > 90:
    print("Es un triángulo obtusángulo")