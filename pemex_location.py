# Datos de los distribuidores
distribuidores = {
    'CDMX': {'galones': 4200, 'x': 63.8, 'y': 5.2},
    'Cuernavaca': {'galones': 2300, 'x': 28.3, 'y': 4.7},
    'Querétaro': {'galones': 1420, 'x': 45.3, 'y': 2.9},
    'Oaxaca': {'galones': 780, 'x': 53.4, 'y': 3.9},
    'Toluca': {'galones': 1630, 'x': 40.2, 'y': 5.7}
}

# Calcular las coordenadas del centro de gravedad
def calcular_centro_de_gravedad(distribuidores):
    suma_galones = sum(distribuidor['galones'] for distribuidor in distribuidores.values())
    x_c = sum(distribuidor['galones'] * distribuidor['x'] for distribuidor in distribuidores.values()) / suma_galones
    y_c = sum(distribuidor['galones'] * distribuidor['y'] for distribuidor in distribuidores.values()) / suma_galones
    return x_c, y_c

# Calcular y mostrar el centro de gravedad
x_c, y_c = calcular_centro_de_gravedad(distribuidores)
print(f'Coordenada X del centro de gravedad: {x_c:.2f}')
print(f'Coordenada Y del centro de gravedad: {y_c:.2f}')