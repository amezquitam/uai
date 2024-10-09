
from simulated_annealing_tsp.test import apply
from readfiles import readfiles


config = {
    'coord.txt': (10, 0.998, 1e-20, 8000),
    'tiny.csv': (8, 0.95, 1e-20, 5000),
    'TSP51.txt': (20, 0.999, 1e-15, 10000),
}


if __name__ == '__main__':
    for file, coords in readfiles():
        apply(coords, f'results/sa/{file}', file, config[file]) # T, Alpha, stopping_T, stopping_it
