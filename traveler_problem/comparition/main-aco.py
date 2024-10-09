
from ant_colony_tsp.main import apply
from readfiles import readfiles

if __name__ == '__main__':
    for file, coords in readfiles():
        apply(coords, f'results/aco/{file}', file, (30, 900, 1, 1, 0.92, 1, 3))
