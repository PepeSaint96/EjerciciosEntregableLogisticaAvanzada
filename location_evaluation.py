# Definir los factores y sus ponderaciones
factores = {
    'Disponibilidad de Mano de Obra': 22,
    'Calidad de vida': 20,
    'Sistema de transporte': 16,
    'Proximidad a los mercados': 24,
    'Proximidad de los materiales': 15,
    'Impuestos': 18,
    'Servicios públicos': 13
}

# Definir las puntuaciones para cada alternativa
alternativas = {
    'A': [6, 3, 2, 3, 4, 2, 4],
    'B': [5, 4, 2, 2, 5, 3, 6],
    'C': [5, 3, 4, 4, 2, 3, 4],
    'D': [4, 3, 1, 2, 2, 5, 2]
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
print(f'\nLa mejor alternativa para la localización de la segunda instalación es: {mejor_alternativa}')