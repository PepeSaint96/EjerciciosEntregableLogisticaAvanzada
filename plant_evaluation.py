# Definir los factores y sus pesos relativos
factores = {
    'Proximidad a proveedores': 20,
    'Costos laborales': 25,
    'Transporte': 15,
    'Impuestos': 17,
    'Costos de instalación': 23
}

# Definir las puntuaciones para cada alternativa
alternativas = {
    'A': [6, 5, 8, 3, 4],
    'B': [8, 7, 5, 6, 9],
    'C': [9, 10, 7, 5, 2]
}

# Calcular la puntuación ponderada para cada alternativa
def calcular_puntuacion_ponderada(alternativas, factores):
    puntuaciones = {}
    for alternativa, valores in alternativas.items():
        puntuacion_total = sum(valores[i] * (list(factores.values())[i] / 100) for i in range(len(valores)))
        puntuaciones[alternativa] = puntuacion_total
    return puntuaciones

# Calcular y mostrar las puntuaciones ponderadas
puntuaciones = calcular_puntuacion_ponderada(alternativas, factores)
for alternativa, puntuacion in puntuaciones.items():
    print(f'Puntuación ponderada para {alternativa}: {puntuacion:.2f}')

# Determinar la mejor alternativa
mejor_alternativa = max(puntuaciones, key=puntuaciones.get)
print(f'\nLa mejor opción para la localización de la planta es: {mejor_alternativa}')