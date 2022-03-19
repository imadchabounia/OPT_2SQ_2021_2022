infinity = 10000000000000

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


def afficher(node):
    print("profit = " + str(node.profit))
    while node.i != 0 and node.parent is not None:
        print(node)
        node = node.parent
    print("-------------------------------------------------------------------------")

def branch_and_bound(capacity, items):
    stack = [Node(0, 0, 0, capacity, infinity, None, 0)]

    candidates = []

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
    afficher(solution)


def tri_a(element):
    return element[0]/element[1]


def worker():

    file = open("testcases.txt", 'r')
    indice_objet = 0
    benefices = []
    for line in file:
        values = line.split();
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
                branch_and_bound(W, items)

worker()
