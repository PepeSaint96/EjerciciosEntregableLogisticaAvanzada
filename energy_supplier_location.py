# Datos de los clientes
clientes = {
    'Three Rivers, MI': {'toneladas': 45500, 'x': 9, 'y': 14},
    'Fort Wayne, IN': {'toneladas': 86300, 'x': 6, 'y': 8},
    'Columbus, OH': {'toneladas': 103250, 'x': 12, 'y': 15},
    'Ashland, KY': {'toneladas': 32000, 'x': 13, 'y': 8},
    'Kinssport, TN': {'toneladas': 77000, 'x': 14, 'y': 10},
    'Akron, OH': {'toneladas': 114600, 'x': 11, 'y': 12},
    'Wheeling, WV': {'toneladas': 81000, 'x': 15, 'y': 4},
    'Roanoke, VA': {'toneladas': 66400, 'x': 10, 'y': 8}
}

# Calcular el centro de gravedad
def calcular_centro_de_gravedad(clientes):
    suma_toneladas = sum(cliente['toneladas'] for cliente in clientes.values())
    x_c = sum(cliente['toneladas'] * cliente['x'] for cliente in clientes.values()) / suma_toneladas
    y_c = sum(cliente['toneladas'] * cliente['y'] for cliente in clientes.values()) / suma_toneladas
    return round(x_c, 1), round(y_c, 1)

# Calcular la puntuación carga-distancia
def calcular_puntuacion_carga_distancia(clientes, centro_gravedad):
    x_c, y_c = centro_gravedad
    puntuacion = sum(cliente['toneladas'] * (abs(cliente['x'] - x_c) + abs(cliente['y'] - y_c)) for cliente in clientes.values())
    return puntuacion

# Calcular y mostrar el centro de gravedad
centro_gravedad = calcular_centro_de_gravedad(clientes)
print(f'Centro de gravedad (X, Y): {centro_gravedad}')

# Calcular y mostrar la puntuación carga-distancia
puntuacion_carga_distancia = calcular_puntuacion_carga_distancia(clientes, centro_gravedad)
print(f'Puntuación carga-distancia: {puntuacion_carga_distancia}')