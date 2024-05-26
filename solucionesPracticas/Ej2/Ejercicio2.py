# Ejercicio 2  ESTRUCTURAS SECUENCIALES
"""
Un pintor de casas debe hacer un presupuesto para un cliente. Lo

que cobra se calcula de acuerdo a los metros cuadrados que debe pintar. El

cliente le indica que necesita conocer el costo de mano de obra para pintar una

pared rectangular de un galpón. El pintor cobra un monto ﬁjo por cada metro

cuadrado. Puedes hacer un algoritmo para calcular el costo de mano de obra para

pintar la pared.
"""



montoFijoM2 = 3000

m2APintar = int(input("Coloque cuantos metros cuadrados desea pintar: "))

calcularCosto = montoFijoM2 * m2APintar

print(f"El costo de mano de obra es de: $ {calcularCosto}")

anchoPared = float(input("Coloque los metros de ancho a pintar: "))
largoPared = float(input("Coloque los metros de largo a pintar: "))
metrosAPintar = anchoPared * largoPared
costoFinal = montoFijoM2 * metrosAPintar
print("El costo de mano de obra es: ", costoFinal)