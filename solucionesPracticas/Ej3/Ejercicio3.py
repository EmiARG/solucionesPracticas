# Ejercicio 3  ESTRUCTURAS SECUENCIALES

"""
Un hincha de fútbol desea conocer la cantidad de puntos que su

equipo lleva acumulados en el campeonato, para ello recibe cada semana la

información de la cantidad total de partidos, desde el inicio del campeonato, que

el equipo ha perdido, ha empatado y ha ganado. Por cada partido empatado

recibe un punto, por cada partido ganado tres puntos y por los perdidos cero

puntos.    
"""

partidoGanado = 3
partidoEmpatado = 1
partidoPerdido = 0

cantidadGanados = int(input("Coloque cuantos partidos ganaron en la temporada: "))
cantidadEmpatados = int(input("Coloque cuantos partidos empataron en la temporada: "))
cantidadPerdidos = int(input("Coloque cuantos partidos perdieron en la temporada: "))

puntosConseguidos = (cantidadGanados * partidoGanado) + ( cantidadEmpatados * partidoEmpatado)

print("La cantidad de puntos conseguidos en la temporada: ",puntosConseguidos)