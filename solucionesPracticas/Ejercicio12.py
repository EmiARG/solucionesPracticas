# Ejercicio 12  ESTRUCTURAS ITERATIVOS

"""
Un profesor de matemática necesita generar la tabla de multiplicar de un número entero comprendido entre 1 y 10. Por ejemplo para el 3 debería aparecer como salida:
3x1=3
3x2=6
3x3=9
…. y así hasta 10

5.1 Resuelva este problema utilizando un mientras y de modo que por la salida se emita la tabla tal como se propone.
5.2 Resuelva este problema utilizando un para y de modo que por la salida se emita la tabla tal como se propone.
"""
"""
#5.1

multiplicador = 1
multiplicando = int(input("Elige un numero del 1 al 10 para conocer su tabla de multiplicación: "))

while multiplicador <= 10 :
    resultado = multiplicador * multiplicando
    print(f"{multiplicador} * {multiplicando} = {resultado}")
    multiplicador += 1
    
"""
#5.2

multiplicando = int(input("Elige un numero del 1 al 10 para conocer su tabla de multiplicación: "))

for i in range(1, 11) :
    print(f"{i} * {multiplicando} = {i * multiplicando}")