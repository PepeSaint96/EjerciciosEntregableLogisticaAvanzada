# Datos de las tiendas
tiendas = {
    'Chicago': {'demanda': 835, 'x': 40, 'y': 150},
    'Pittsburgh': {'demanda': 2650, 'x': 50, 'y': 120},
    'New York': {'demanda': 1820, 'x': 85, 'y': 90},
    'Atlanta': {'demanda': 1530, 'x': 50, 'y': 70}
}

# Calcular las coordenadas del centro de gravedad
def calcular_centro_de_gravedad(tiendas):
    suma_demanda = sum(tienda['demanda'] for tienda in tiendas.values())
    x_c = sum(tienda['demanda'] * tienda['x'] for tienda in tiendas.values()) / suma_demanda
    y_c = sum(tienda['demanda'] * tienda['y'] for tienda in tiendas.values()) / suma_demanda
    return x_c, y_c

# Calcular y mostrar el centro de gravedad
x_c, y_c = calcular_centro_de_gravedad(tiendas)
print(f'Coordenada X del centro de gravedad: {x_c:.2f}')
print(f'Coordenada Y del centro de gravedad: {y_c:.2f}')