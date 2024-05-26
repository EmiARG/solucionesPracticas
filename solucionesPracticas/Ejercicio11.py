# Ejercicio 11  ESTRUCTURAS ITERATIVOS

"""
En una escuela, luego de tomar un determinado examen, es necesario calcular el promedio de notas (las notas van de 0 a 10) de los alumnos de un curso. Se necesita saber si el rendimiento ha sido elevado (el promedio es mayor a 8), aceptable (el promedio está comprendido entre 6 y 8) o bajo (promedio es inferior a 6). Desarrollar un algoritmo que resuelva este problema. Para tener en cuenta: las autoridades del colegio saben cuántos estudiantes del curso han rendido el examen.
"""

cantidadEstudiantes = 6
notas = 0

for i in range(cantidadEstudiantes) :
    nota = int(input(f"Ingrese la nota del estudiante Nº {i+1}: "))
    notas += nota

promedio = notas / cantidadEstudiantes

if promedio > 8 :
    print(f"El promedio es de : {promedio}, el rendimiento ha sido elevado")
elif promedio >= 6 :
    print(f"El promedio es de : {promedio}, el rendimiento es aceptable")
else :
    print(f"El promedio es de : {promedio}, el rendimiento fue bajo")
    
