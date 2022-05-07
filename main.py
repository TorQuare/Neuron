import pygad
import numpy
import time
import os

# Zad 4 - wybór wartości długości tablicy S oraz procentu mutacji
print("Input selected value: \n1) S len = 15\n2) S len = 25\n3) S len = 35\n4) S len = 45\nPicked: ")
arr_value = int(input())
print("Input selected value of gens percent: \n1) 8%\n2) 5%\n3) 4%\n4) 3%\nPicked: ")
gens_value = int(input())


#Zad 3.C - rozpoczęćie pomiaru czasu
start = time.time()

S = [1, 2, 3, 6, 10, 17, 25, 29, 30, 41, 51, 60, 70, 79, 80]

# Zad 4.A - generowanie nowej tablicy S
if arr_value != 1:
    expand_value = 0
    # wygenerowane losowo liczy podzielne przez 2
    new_values = [24, 24, 92, 92, 34, 70, 82, 70, 80, 30, 6, 78, 18, 26, 50, 38, 14, 22,
                  8, 78, 92, 12, 98, 36, 94, 30, 86, 52, 6, 78]
    if arr_value == 2:
        expand_value = 10
    if arr_value == 3:
        expand_value = 20
    if arr_value == 4:
        expand_value = 30

    for i in range(expand_value):
        S.append(new_values[i])

#definiujemy parametry chromosomu
#geny to liczby: 0 lub 1
gene_space = [0, 1]

#definiujemy funkcję fitness
def fitness_func(solution, solution_idx):
    sum1 = numpy.sum(solution * S)
    solution_invert = 1 - solution
    sum2 = numpy.sum(solution_invert * S)
    fitness = -numpy.abs(sum1-sum2)
    #lub: fitness = 1.0 / (1.0 + numpy.abs(sum1-sum2))
    return fitness

fitness_function = fitness_func

#ile chromsomów w populacji
#ile genow ma chromosom
sol_per_pop = 10
num_genes = len(S)

#ile wylaniamy rodzicow do "rozmanazania" (okolo 50% populacji)
#ile pokolen
#ilu rodzicow zachowac (kilka procent)
num_parents_mating = 5
num_generations = 30
keep_parents = 2

#jaki typ selekcji rodzicow?
#sss = steady, rws=roulette, rank = rankingowa, tournament = turniejowa
parent_selection_type = "sss"

#w il =u punktach robic krzyzowanie?
crossover_type = "single_point"

#mutacja ma dzialac na ilu procent genow?
#trzeba pamietac ile genow ma chromosom
mutation_type = "random"

# Zad 4.B - wybrane poziomy mutacji
if gens_value == 1:
    mutation_percent_genes = 8
if gens_value == 2:
    mutation_percent_genes = 5
if gens_value == 3:
    mutation_percent_genes = 4
if gens_value == 4:
    mutation_percent_genes = 3

# Zad 3.C - pomiar czasu przed algorytmem GA
end_first = time.time()

#inicjacja algorytmu z powyzszymi parametrami wpisanymi w atrybuty
ga_instance = pygad.GA(gene_space=gene_space,
                       num_generations=num_generations,
                       num_parents_mating=num_parents_mating,
                       fitness_func=fitness_function,
                       sol_per_pop=sol_per_pop,
                       num_genes=num_genes,
                       parent_selection_type=parent_selection_type,
                       keep_parents=keep_parents,
                       crossover_type=crossover_type,
                       mutation_type=mutation_type,
                       mutation_percent_genes=mutation_percent_genes,
                       # Zad 3.A
                       stop_criteria=["reach_0"])

#uruchomienie algorytmu
ga_instance.run()

# Zad 3.C - pomiar czasu po wykonaniu algorymtu GA
end_sec = time.time()

#podsumowanie: najlepsze znalezione rozwiazanie (chromosom+ocena)
solution, solution_fitness, solution_idx = ga_instance.best_solution()
print("Parameters of the best solution : {solution}".format(solution=solution))
print("Fitness value of the best solution = {solution_fitness}".format(solution_fitness=solution_fitness))

#tutaj dodatkowo wyswietlamy sume wskazana przez jedynki
prediction = numpy.sum(S*solution)
print("Predicted output based on the best solution : {prediction}".format(prediction=prediction))

# Zad 3.B
if solution_fitness == 0:
    generations = ga_instance.generations_completed - 1
    print("Number of generations until find best solution: {generations}".format(generations=generations))

# Zad 3.C - wypisanie pomiaru czasu
first_timelaps = end_first - start
sec_timelaps = end_sec - start
print("Working before GA: ", first_timelaps, " Working with GA: ", sec_timelaps, " S array length: ", len(S),
      " Mutation percent:", mutation_percent_genes)

# Zad 3.D / Zad 4.C - zapis pomiaru wartości czasu oraz
file = open("Runs.txt", 'a')
file.write("Working before GA: " + str(first_timelaps) + " Working with GA: " + str(sec_timelaps) +
           " S array length: " + str(len(S)) + " Mutation percent: " + str(mutation_percent_genes) + "\n")
file.close()

#wyswietlenie wykresu: jak zmieniala sie ocena na przestrzeni pokolen
ga_instance.plot_fitness()