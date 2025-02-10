# Datos de las localizaciones
localizaciones = {
    'Chihuahua': {'volumen': 800, 'x': 1450, 'y': 1300},
    'Toluca': {'volumen': 600, 'x': 1520, 'y': 1400},
    'Chiapas': {'volumen': 1200, 'x': 1600, 'y': 730},
    'San Luis Potosí': {'volumen': 900, 'x': 1100, 'y': 890},
    'Querétaro': {'volumen': 1400, 'x': 1720, 'y': 620},
    'Aguascalientes': {'volumen': 1200, 'x': 1730, 'y': 525},
    'Morelia': {'volumen': 640, 'x': 1830, 'y': 720}
}

# Calcular las coordenadas del centro de gravedad
def calcular_centro_de_gravedad(localizaciones):
    suma_volumen = sum(loc['volumen'] for loc in localizaciones.values())
    x_c = sum(loc['volumen'] * loc['x'] for loc in localizaciones.values()) / suma_volumen
    y_c = sum(loc['volumen'] * loc['y'] for loc in localizaciones.values()) / suma_volumen
    return x_c, y_c

# Calcular y mostrar el centro de gravedad
x_c, y_c = calcular_centro_de_gravedad(localizaciones)
print(f'Coordenada X del centro de gravedad: {x_c:.2f}')
print(f'Coordenada Y del centro de gravedad: {y_c:.2f}')