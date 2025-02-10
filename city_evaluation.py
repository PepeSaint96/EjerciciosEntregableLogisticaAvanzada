# Define the factors, their weights, and the scores for each city
factors = {
    'Incentivo': {'weight': 0.6, 'Atlanta': 75, 'Charlotte': 50},
    'Satisfacción del Jugador': {'weight': 0.7, 'Atlanta': 30, 'Charlotte': 42},
    'Interés en los deportes': {'weight': 0.3, 'Atlanta': 50, 'Charlotte': 55},
    'Tamaño de la ciudad': {'weight': 0.2, 'Atlanta': 65, 'Charlotte': 40}
}

# Function to calculate the total score for a city
def calculate_total_score(city, factors):
    total_score = sum(factor['weight'] * factor[city] for factor in factors.values())
    return total_score

# Calculate scores for Atlanta and Charlotte
atlanta_score = calculate_total_score('Atlanta', factors)
charlotte_score = calculate_total_score('Charlotte', factors)

# Determine the best city
best_city = 'Atlanta' if atlanta_score > charlotte_score else 'Charlotte'
best_score = max(atlanta_score, charlotte_score)

# Print the results
print(f'Puntuación total para Atlanta: {atlanta_score:.2f}')
print(f'Puntuación total para Charlotte: {charlotte_score:.2f}')
print(f'\nLa mejor ciudad para llevar a los Coolers es: {best_city}')
print(f'Puntuación total de la mejor ciudad: {best_score:.2f}')