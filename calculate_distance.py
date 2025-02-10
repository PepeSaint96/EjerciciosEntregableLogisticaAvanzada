import math

# Coordenadas
centro_gravedad = {'x': 48.84, 'y': 4.75}
queretaro = {'x': 45.3, 'y': 2.9}
toluca = {'x': 40.2, 'y': 5.7}

# Calcular la distancia euclidiana
def calcular_distancia(coord1, coord2):
    return math.sqrt((coord1['x'] - coord2['x'])**2 + (coord1['y'] - coord2['y'])**2)

# Distancias
distancia_queretaro = calcular_distancia(centro_gravedad, queretaro)
distancia_toluca = calcular_distancia(centro_gravedad, toluca)

# Mostrar distancias
print(f'Distancia a Querétaro: {distancia_queretaro:.2f}')
print(f'Distancia a Toluca: {distancia_toluca:.2f}')

# Determinar la ciudad más cercana
if distancia_queretaro < distancia_toluca:
    print('La mejor ubicación es Querétaro.')
else:
    print('La mejor ubicación es Toluca.')