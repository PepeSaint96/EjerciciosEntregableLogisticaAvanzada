import matplotlib.pyplot as plt

# Datos de las localizaciones y volumen esperado
volumen_esperado = 1850
precio_venta = 145

localizaciones = {
    'Akron': {'costo_fijo': 42000, 'costo_variable': 55},
    'Bowling Green': {'costo_fijo': 57000, 'costo_variable': 35},
    'Chicago': {'costo_fijo': 85000, 'costo_variable': 15}
}

# Calcular los costos totales para cada localización
def calcular_costos_totales(localizacion, volumen):
    costo_fijo = localizacion['costo_fijo']
    costo_variable = localizacion['costo_variable']
    return costo_fijo + (costo_variable * volumen)

costos_totales = {loc: calcular_costos_totales(data, volumen_esperado) for loc, data in localizaciones.items()}

# Graficar las opciones
volumenes = range(0, 2001, 100)
costos_akron = [calcular_costos_totales(localizaciones['Akron'], v) for v in volumenes]
costos_bowling_green = [calcular_costos_totales(localizaciones['Bowling Green'], v) for v in volumenes]
costos_chicago = [calcular_costos_totales(localizaciones['Chicago'], v) for v in volumenes]

plt.figure(figsize=(10, 6))
plt.plot(volumenes, costos_akron, label='Akron')
plt.plot(volumenes, costos_bowling_green, label='Bowling Green')
plt.plot(volumenes, costos_chicago, label='Chicago')
plt.axvline(volumen_esperado, color='gray', linestyle='--', label='Volumen Esperado')
plt.xlabel('Volumen de Producción (unidades)')
plt.ylabel('Costos Totales ($)')
plt.title('Análisis del Punto de Equilibrio de Localización')
plt.legend()
plt.grid(True)
plt.show()

# Mostrar los costos totales para el volumen esperado
for loc, costo in costos_totales.items():
    print(f'Costo total para {loc} con {volumen_esperado} unidades: ${costo:.2f}')

# Determinar la mejor opción
mejor_opcion = min(costos_totales, key=costos_totales.get)
print(f'\nLa mejor opción con el volumen de venta esperado es: {mejor_opcion}')