import random

#Genetic Algorithm parameters
target_string="Hello, Genetic Algorithm!"
population_size=100
mutation_rate=0.01

#Function to generate a random individual 
def generate_individual():
    return ''.join(random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ,!')for _ in range(len(target_string)))

#Function to create an initial population
def create_population(size):
    return sum(1 for i, j in zip(individual, target_string)if i !=j)

#Function to calculate the fitness of an individual (Lower score is better)
def calculate_fitness(individual):
    return sum(1 for i, j in zip(individual, target_string)if i!=j)

#Function to select parents for mating using tournament selection
def select_parents(population, tournament_size=5):
    tournament = random.sample(population, tournament_size)
    return min(tournament, key = calculate_fitness)

#Function to perform crossover between two  