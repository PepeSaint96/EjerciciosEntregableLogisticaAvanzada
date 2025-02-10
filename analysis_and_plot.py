import matplotlib.pyplot as plt
import numpy as np

# Define constants for each community
cost_fixed = {
    'A': 605000,
    'B': 520000,
    'C': 330000,
    'D': 160000
}

cost_variable = {
    'A': 32,
    'B': 26,
    'C': 37,
    'D': 60
}

# Define the range of quantities
quantities = np.arange(0, 25000, 500)

# Calculate total costs for each community
total_costs = {
    'A': cost_fixed['A'] + cost_variable['A'] * quantities,
    'B': cost_fixed['B'] + cost_variable['B'] * quantities,
    'C': cost_fixed['C'] + cost_variable['C'] * quantities,
    'D': cost_fixed['D'] + cost_variable['D'] * quantities
}

# Plot the total cost curves
plt.figure(figsize=(10, 6))
for community in total_costs:
    plt.plot(quantities, total_costs[community], label=f'Comunidad {community}')

plt.xlabel('Cantidad de Unidades')
plt.ylabel('Costo Total ($)')
plt.title('Curvas del Costo Total para Cada Comunidad')
plt.legend()
plt.grid(True)
plt.show()

# Calculate break-even points
def break_even(cf1, cv1, cf2, cv2):
    return (cf2 - cf1) / (cv1 - cv2)

break_even_points = {
    ('A', 'B'): break_even(cost_fixed['A'], cost_variable['A'], cost_fixed['B'], cost_variable['B']),
    ('A', 'C'): break_even(cost_fixed['A'], cost_variable['A'], cost_fixed['C'], cost_variable['C']),
    ('A', 'D'): break_even(cost_fixed['A'], cost_variable['A'], cost_fixed['D'], cost_variable['D']),
    ('B', 'C'): break_even(cost_fixed['B'], cost_variable['B'], cost_fixed['C'], cost_variable['C']),
    ('B', 'D'): break_even(cost_fixed['B'], cost_variable['B'], cost_fixed['D'], cost_variable['D']),
    ('C', 'D'): break_even(cost_fixed['C'], cost_variable['C'], cost_fixed['D'], cost_variable['D']),
}

# Print break-even points
for pair, point in break_even_points.items():
    print(f'Punto de equilibrio entre Comunidad {pair[0]} y Comunidad {pair[1]}: {point:.2f} unidades')

# Determine the best location for expected demand
expected_demand = 18000
costs_at_expected_demand = {community: cost_fixed[community] + cost_variable[community] * expected_demand for community in cost_fixed}
best_location = min(costs_at_expected_demand, key=costs_at_expected_demand.get)

print(f'\nMejor localización para una demanda de {expected_demand} unidades: Comunidad {best_location}')
print(f'Costo total: ${costs_at_expected_demand[best_location]:.2f}')