# Ejercicio 7  ESTRUCTURAS CONDICIONALES

"""
4. Condicional completo (if - else) con expresión lógica compuesta (or)
"""

edad = int(input("Ingrese su edad: "))

esEstudiante = input("Si es estudiante ingrese si: ")

if edad < 18 or esEstudiante == "si" :
    print("Tienes descuento en el boleto")
else :
    print("Tienes que pagar la totalidad del boleto")