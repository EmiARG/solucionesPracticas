# Ejercicio 10  ESTRUCTURAS ITERATIVOS

"""
Pedir que el usuario ingrese (input) nombre de personas y mostrarlos hasta que el valor de lo que ingresa sea “fin”
"""

nombres = []

while True:
    nombre = input("Ingresar nombres, escribe 'fin' para finalizar: ")
    if nombre == "fin":
        break
    nombres.append(nombre)
    
for nombre in nombres:
    print(nombre)