infinity = 10000000000000

import time

def tri_a(element):
    return element[0]/element[1]

def tri_b(element):
    return element[1]

def heuristique1(capacity, items, k):

    items.sort(reverse=True, key=k)

    result = 0
    n = len(items)
    i = int(0)
    solution = [0]*n #les valeurs de x
    W = capacity

    while i < n:
        x = 0
        while W-items[i][1] > 0:
            result += items[i][0]
            W -= items[i][1]
            x += 1

        solution[items[i][2]] = x
        i += 1

    print(solution)
    print("Solution : ", result)





def worker():

    file = open("testcases.txt", 'r')
    benefices = []
    for line in file:
        values = line.split()
        if len(values) == 0:
            continue
        else:
            if values[0] == "$1":
                W = int(values[-1])
            elif values[0] == "$2":
                benefices = values[1:]
            elif values[0] == "$3":
                items = []
                values = values[1:]
                for i in range(0, len(benefices)):
                    items.append([int(benefices[i]), int(values[i]), i])
                time_start = time.time()
                #branch_and_bound(W, items)
                heuristique1(W, items, tri_a)
                heuristique1(W, items, tri_b)
                time_end = time.time()
                print(time_end - time_start)
worker()
