infinity = 10000000000000

import time

def tri_a(element):
    return element[0]/element[1]

def changeProfit(items, current_capacity, current_profit, solution, i, x):

    init_x = solution[i]
    diff = init_x-x
    ni = -1
    nxi = 0
    current_capacity += items[i][1]*diff
    current_profit -= items[i][0]*diff
    best_profit = 0
    j = i+1

    while j < len(items):
        if(current_capacity >= items[j][1]):
            xj = int(current_capacity/items[j][1])
            if(best_profit < xj*items[j][0]):
                best_profit = xj*items[j][0]
                ni = j
                nxi = xj
        j += 1
    return best_profit+current_profit, ni, nxi


def heuristique2(capacity, items, k):

    #Pahse 1
    items.sort(reverse=True, key=k)
    result = 0
    n = len(items)
    i = int(0)
    solution = [0]*n #les valeurs de x
    W = capacity
    m = n #est un paramètre à choisir

    while i < m:
        x = 0
        while W-items[i][1] > 0:
            result += items[i][0]
            W -= items[i][1]
            x += 1
        solution[items[i][2]] = x
        i += 1

    #Phase 2
    i = 0;
    while i < n:
        xi = solution[i];
        while xi > 0:
            xi = xi-1
            new_profit, ni, xni = changeProfit(items, W, result, solution, i, xi)
            if ni == -1:
                continue
            if new_profit > result:
                result = new_profit
                solution[i] = xi
                solution[ni] = xni
                W = W - items[ni][1]*xni
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
                heuristique2(W, items, tri_a)
                time_end = time.time()
                print(time_end - time_start)
worker()
