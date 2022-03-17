infinity = 10000000000000

Input = [[10, 1, 0], [40, 3, 1], [50, 4, 2], [70, 5, 3]]
W = 8

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
    Input.sort(reverse=True, key=tri_a)
    branch_and_bound(W, Input)


worker()
