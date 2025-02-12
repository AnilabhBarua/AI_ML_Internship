#!/usr/bin/env python
# coding: utf-8

# In[16]:


import random

# Genetic Algorithm Parameters
target_string = "Hello, Genetic Algorithm!"
population_size = 100
mutation_rate = 0.01

# Function to generate a random individual
def generate_individual():
    return ''.join(random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ ,!') for _ in range(len(target_string)))

# Function to create an initial population
def create_population(size):
    return [generate_individual() for _ in range(size)]

# Function to calculate the fitness of an individual (Lower score is better)
def calculate_fitness(individual):
    return sum(1 for i, j in zip(individual, target_string) if i != j)

# Function to select parents for mating using tournament selection
def select_parents(population, tournament_size=5):
    tournament = random.sample(population, tournament_size)
    return min(tournament, key=calculate_fitness)

# Function to perform crossover between two parents to produce a new child
def crossover(parent1, parent2):
    crossover_point = random.randint(0, len(target_string))
    return parent1[:crossover_point] + parent2[crossover_point:]

# Function to perform mutation on an individual
def mutate(individual):
    return ''.join(c if random.random() > mutation_rate else random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ ,!') for c in individual)

# Main Genetic Algorithm function
def genetic_algorithm(target_string, population_size, mutation_rate):
    population = create_population(population_size)
    generation = 1

    while True:
        population = sorted(population, key=calculate_fitness)
        best_individual = population[0]

        if calculate_fitness(best_individual) == 0:
            break

        new_population = [best_individual]

        while len(new_population) < population_size:
            parent1 = select_parents(population)
            parent2 = select_parents(population)
            child = crossover(parent1, parent2)
            child = mutate(child)
            new_population.append(child)

        population = new_population
        generation += 1

    return best_individual, generation

# Run the Genetic Algorithm
best_individual, generation = genetic_algorithm(target_string, population_size, mutation_rate)
print(f"Generation: {generation}")
print(f"Best Individual: {best_individual}")


# In[ ]:




