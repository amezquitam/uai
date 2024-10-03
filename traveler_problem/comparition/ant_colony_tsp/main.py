import math
import multiprocessing.pool
import timeit
import statistics
import numpy as np, pandas as pd
import multiprocessing


from .aco import ACO, Graph
from .plot import plot
import matplotlib.pyplot as plt


def distance(city1: dict, city2: dict):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)


def exec(args):
    cost_matrix, rank = args
    start_time = timeit.default_timer() #Para tomar el tiempo de ejecución
    #ant_countt, generations, alpha, beta, rho, q, sategy)
    #aco = ACO(20, 600, 1, 2, 0.5, 1, 3)
    #aco = ACO(20, 800, 1, 2, 0.85, 1, 3)
    aco = ACO(20, 800, 1, 2, 0.85, 1, 3)
    graph = Graph(cost_matrix, rank)

    path, cost, sln, n_gen = aco.solve(graph)

    stop_time = timeit.default_timer()
    end_time = stop_time - start_time
    
    print('cost: {}, path: {}'.format(cost, path))
    print("running_time: ",format(end_time, '.8f'))
    print("Encontró la solución en %d iteraciones" % n_gen)
    return end_time, cost, n_gen, sln

def apply(coords, out_file):
    cost_matrix = []
    rank = len(coords)
    for i in range(rank):
        row = []
        for j in range(rank):
            row.append(distance(coords[i], coords[j]))
        cost_matrix.append(row)
    
    
    
    res = []
    end_times = [] 
    n_gens = []
    
    nejecuciones = 20

    pool = multiprocessing.Pool(4)
            
    end_times, res, n_gens, plots = zip(*pool.map(exec, [(cost_matrix, rank) for _ in range(nejecuciones)])) 
    
    # for i in range(nejecuciones):
        
    #    start_time = timeit.default_timer() #Para tomar el tiempo de ejecución
    #    #ant_countt, generations, alpha, beta, rho, q, sategy)
    #    aco = ACO(20, 600, 1, 2, 0.5, 1, 3)
    #    #aco = ACO(20, 300, 1, 2, 0.8, 1, 3)
    #    graph = Graph(cost_matrix, rank)

    #    path, cost, sln, n_gen = aco.solve(graph)

    #    stop_time = timeit.default_timer()
    #    end_time = stop_time - start_time
    #    end_times.append(end_time)
    #    res.append(cost)
    #    n_gens.append(n_gen)
       
    #    print('cost: {}, path: {}'.format(cost, path))
    #    print("running_time: ",format(end_time, '.8f'))
    #    print("Encontró la solución en %d iteraciones" % n_gen)

    plt.plot(plots[0])
    plt.ylabel("Fitness")
    plt.xlabel("Iteration")
    plt.show()


    print("Costo total promedio =", round(statistics.mean(res), 2))
    varianza = statistics.variance(res)
    print("Varianza: ", round(varianza,3))
    print("Mejor distancia total encontrada en %d correidas: %f" % (nejecuciones, min(res)))

    df = pd.DataFrame(res, columns =['Costo_total'], dtype = float)
    df['Time'] = end_times
    df['Iteracion'] = n_gens
    print(df.head())
    df.to_excel(out_file)
