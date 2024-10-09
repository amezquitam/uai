import math
import multiprocessing.pool
import timeit
import statistics
import pandas as pd
import multiprocessing


from .aco import ACO, Graph
import matplotlib.pyplot as plt


def distance(city1: dict, city2: dict):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)


# (ant_count, generations, alpha, beta, rho, q, sategy)

_config = [(30, 900, 1, 1, 0.92, 1, 3)]
#config = (40, 1000, 1, 1, 0.96, 1, 3)


def exec_aco(args):
    cost_matrix, rank = args
    start_time = timeit.default_timer()
    aco = ACO(*(_config[0]))
    graph = Graph(cost_matrix, rank)

    path, cost, sln, n_gen = aco.solve(graph)

    stop_time = timeit.default_timer()
    end_time = stop_time - start_time
    
    print('cost: {}, path: {}'.format(cost, path))
    print("running_time: ",format(end_time, '.8f'))
    print("Encontró la solución en %d iteraciones" % n_gen)
    return end_time, cost, n_gen, sln

def apply(coords, out_file, file, config):
    _config[0] = config
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
    
    nejecuciones = 40

    pool = multiprocessing.Pool(4)

    end_times, res, n_gens, plots = zip(*pool.map(exec_aco, [(cost_matrix, rank) for _ in range(nejecuciones)])) 

    plt.plot(plots[0])
    plt.ylabel("Fitness")
    plt.xlabel("Iteration")
    plt.savefig(f"captures/aco/{file}-{str(config)}.png")

    print("Costo total promedio =", round(statistics.mean(res), 2))
    varianza = statistics.variance(res)
    print("Varianza: ", round(varianza, 3))
    print("Mejor distancia total encontrada en %d corridas: %f" % (nejecuciones, min(res)))

    df = pd.DataFrame(res, columns=['Costo_total'], dtype = float)
    df['Time'] = end_times
    df['Iteracion'] = n_gens
    print(df.head())
    df.to_excel(out_file + str(config) + '.xlsx')
