# Ejercicio 9  ESTRUCTURAS ITERATIVOS

"""
Mostrar sólo los números pares desde 0 hasta el número ingresado
"""

numero = int(input("Ingrese un numero: "))

for i in range(numero + 1) :
    if i%2 == 0 :
        print(i)