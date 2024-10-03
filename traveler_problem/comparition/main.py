from christofides import tsp
from ant_colony_tsp.main import apply as apply_ant_colony
from simulated_annealing_tsp.test import apply as apply_simulated_annealing

if __name__ == '__main__':
    args = []
    coords = []
    with open("tiny.csv") as f:
        for line in f:
            x, y = line.split(',')
            coords.append([float(x), float(y)])
    
    args.append(list(coords))

    coords = []
    with open("coord.txt") as f:
        for line in f:
            x, y = line.split(' ')
            coords.append([float(x), float(y)])
    
    args.append(list(coords))
    
    coords = []
    with open("TSP51.txt") as f:
        for line in f:
            i, x, y = line.split(' ')
            coords.append([float(x), float(y)])
    
    args.append(list(coords))

    for coords in args:
        print(tsp(coords))
        apply_ant_colony(coords, 'result_ant_colony.xlsx')
        apply_simulated_annealing(coords, 'result_sumulated_annealing.xlsx')
