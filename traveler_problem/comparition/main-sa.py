from christofides import tsp
from simulated_annealing_tsp.test import apply as apply_simulated_annealing

if __name__ == '__main__':
    args = []
    coords = []
    with open("tiny.csv") as f:
        for line in f:
            x, y = line.split(',')
            coords.append([float(x), float(y)])
    
    args.append(("tiny.csv", list(coords)))

    coords = []
    with open("coord.txt") as f:
        for line in f:
            x, y = line.split(' ')
            coords.append([float(x), float(y)])
    
    args.append(("coord.txt", list(coords)))
    
    coords = []
    with open("TSP51.txt") as f:
        for line in f:
            i, x, y = line.split(' ')
            coords.append([float(x), float(y)])
    
    args.append(("TSP51.txt", list(coords)))

    for file, coords in args:
        apply_simulated_annealing(coords, f'result_sumulated_annealing-{file}.xlsx')
