from christofides import tsp
from readfiles import readfiles

if __name__ == '__main__':
    for file, coords in readfiles():
        shortest_path, exec_time, total_distance = tsp(coords)
        print(f'{shortest_path=}')
        print(f'{exec_time=}')
        print(f'{total_distance=}')

