infinity = 10000000000000

import time

class SolutionCLass:

    def __init__(self):
        self.solution_vector = list()
        self.solution_fitness = list()
        self.solution_time = list()
        self.executions = list()

    def addSolutionVector(self, s_v):
        self.solution_vector.append(s_v)

    def addSolutionFitness(self, s_f):
        self.solution_fitness.append(s_f)

    def addSolutionTime(self, s_t):
        self.solution_time.append(s_t)

    def addExecution(self, exec):
        self.executions.append(exec)

class Node:
    def __init__(self, i, x, profit, w, evaluation, node, index):
        self.i = i
        self.x = x
        self.profit = profit
        self.space = w
        self.evaluation = evaluation
        self.parent = node
        self.index = index

    def __str__(self):
        return "x" + str(self.index) + " = " + str(self.x)


def constructSolution(node):
    solution_vector = list()
    eval = node.profit
    while node.i != 0 and node.parent is not None:
        solution_vector.append(node.x)
        node = node.parent

    return solution_vector, eval

def branch_and_bound(capacity, items):
    stack = [Node(0, 0, 0, capacity, infinity, None, 0)]

    number_of_items = len(items)

    borne_inf = -infinity

    solution = stack[-1]

    while stack:
        top = stack.pop()
        if top.i == number_of_items:
            if(top.profit > borne_inf):
                solution = top
                borne_inf = top.profit

        elif top.i < number_of_items:
            new_space = top.space
            new_i = top.i + 1
            new_index = items[top.i][2]+1
            xi = 0
            while top.space >= items[top.i][1]*xi:

                new_x = xi
                new_profit = top.profit + items[top.i][0]*xi
                new_space = top.space - items[top.i][1]*xi
                new_evaluation = top.evaluation
                new_parent = top
                if new_i < number_of_items:
                    new_evaluation = min(top.evaluation, new_profit + (items[new_i][0] / items[new_i][1])*new_space)
                    if new_evaluation >= borne_inf:
                        stack.append(Node(new_i, new_x, new_profit, new_space, new_evaluation, new_parent, new_index))
                else:
                    stack.append(Node(new_i, new_x, new_profit, new_space, new_evaluation, new_parent, new_index))

                xi += 1
    return constructSolution(solution)


def tri_a(element):
    return element[0]/element[1]


def worker():
    solutions = SolutionCLass()
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
                items.sort(reverse=True, key=tri_a)
                time_start = time.perf_counter()
                S_etoile, fitness = branch_and_bound(W, items)
                time_end = time.perf_counter()
                time_spent = time_end-time_start
                solutions.solution_vector.append(S_etoile)
                solutions.solution_time.append(time_spent)
                solutions.solution_fitness.append(fitness)
    return solutions
