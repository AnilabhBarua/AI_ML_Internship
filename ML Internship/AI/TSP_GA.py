#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random
import numpy as np
import matplotlib.pyplot as plt

# Define the coordinates of the cities (you can modify this to your dataset)
cities = {
    "A": (0, 0),
    "B": (1, 5),
    "C": (2, 3),
    "D": (5, 8),
    "E": (7, 2),
}

# Genetic Algorithm Parameters
POPULATION_SIZE = 100
GENERATIONS = 1000
MUTATION_RATE = 0.2

def calculate_distance(city1, city2):
    return np.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def calculate_total_distance(route):
    total_distance = 0
    for i in range(len(route) - 1):
        total_distance += calculate_distance(cities[route[i]], cities[route[i + 1]])
    return total_distance

def create_initial_population(num_cities, population_size):
    population = []
    for _ in range(population_size):
        route = list(cities.keys())
        random.shuffle(route)
        population.append(route)
    return population

def select_parents(population, num_parents):
    parents = []
    for _ in range(num_parents):
        candidate_parents = random.sample(population, 5)  # Randomly select 5 candidates
        parents.append(min(candidate_parents, key=calculate_total_distance))
    return parents

def crossover(parent1, parent2):
    start = random.randint(0, len(parent1) - 1)
    end = random.randint(start + 1, len(parent1))
    child = parent1[start:end] + [city for city in parent2 if city not in parent1[start:end]]
    return child

def mutate(route):
    for _ in range(len(route)):
        if random.random() < MUTATION_RATE:
            idx1, idx2 = random.sample(range(len(route)), 2)
            route[idx1], route[idx2] = route[idx2], route[idx1]
    return route

def plot_route(route):
    x = [cities[city][0] for city in route + [route[0]]]
    y = [cities[city][1] for city in route + [route[0]]]
    plt.plot(x, y, 'bo-')
    for city, (xc, yc) in cities.items():
        plt.text(xc, yc, city, ha='center', va='center', fontweight='bold', color='white', fontsize=12)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Best Route')
    plt.grid(True)
    plt.show()

def genetic_algorithm():
    population = create_initial_population(len(cities), POPULATION_SIZE)
    for generation in range(GENERATIONS):
        parents = select_parents(population, num_parents=2)
        offspring = [crossover(parents[0], parents[1]) for _ in range(POPULATION_SIZE - 2)]
        offspring = [mutate(child) for child in offspring]
        population = parents + offspring
    best_route = min(population, key=calculate_total_distance)
    return best_route, calculate_total_distance(best_route)

if __name__ == "__main__":
    best_route, best_distance = genetic_algorithm()
    print("Best route:", best_route)
    print("Total distance:", best_distance)
    plot_route(best_route)


# In[ ]:




