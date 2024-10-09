
def readfiles():
    args = []
    coords = []
    with open("tiny.csv") as f:
        for line in f:
            x, y = line.split(',')
            coords.append((float(x), float(y)))
    
    args.append(("tiny.csv", list(coords)))

    coords = []
    with open("coord.txt") as f:
        for line in f:
            x, y = line.split(' ')
            coords.append((float(x), float(y)))
    
    args.append(("coord.txt", list(coords)))
    
    coords = []
    with open("TSP51.txt") as f:
        for line in f:
            _, x, y = line.split(' ')
            coords.append((float(x), float(y)))
    
    args.append(("TSP51.txt", list(coords)))

    return args