# Ejercicio 13  ESTRUCTURAS DE DATOS

"""
Pedir al usuario que ingrese 10 nombres de personas (input en un ciclo) no repetidas, guardarlos en una lista y mostrarlos.
"""
"""
#1
nombres = []

for i in range(10):
    nombre = input(f"Ingrese el nombre Nº{i+1}: ")
    while nombre in nombres:
        print("Ese nombre ya fue ingresado, ingresa otro")
        nombre = input(f"Ingrese el nombre Nº{i+1}: ")
    nombres.append(nombre)

print("Los nombres que has ingresado son: ")
for nombre in nombres:
    print(nombre)
    
#2 
del nombres[2]
del nombres[-1]
nombres.sort()

print("La lista actualizada es: ")
for nombre in nombres:
    print(nombre)
    
#3
persona = {}

persona["Nombre"] = input("Ingrese su nombre: ")
persona["Apellido"] = input("Ingrese su apellido: ")
persona["Dni"] = int(input("Ingrese su numero de DNI: "))
persona["Email"] = input("Ingrese su email: ")
persona["Fecha de nacimiento"] = input("Ingrese su fecha de nacimiento DD/MM/AAAA: ")


#4
familia = {}

for i in range(1, 5):
    persona = {}
    print("Ingresar los datos: ")
    persona["Nombre"] = input("Ingrese su nombre: ")
    persona["Apellido"] = input("Ingrese su apellido: ")
    persona["Dni"] = int(input("Ingrese su numero de DNI: "))
    persona["Email"] = input("Ingrese su email: ")
    persona["Fecha de nacimiento"] = input("Ingrese su fecha de nacimiento DD/MM/AAAA: ")
    familia[f"Persona{i}"] = persona
    
print(familia)
"""
#5
valorN = int(input("Ingrese un numero: "))

numerosPares = []

for i in range(1, valorN * 2 + 1) :
    if i % 2 == 0 :
        numerosPares.append(i)
print(numerosPares)
tuplaNumerosPares = tuple(numerosPares)

print(tuplaNumerosPares)

