from christofides import tsp
from ant_colony_tsp.main import apply as apply_ant_colony

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
        apply_ant_colony(coords, f'result_ant_colony-{file}')
