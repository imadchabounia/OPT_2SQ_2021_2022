"""

INPUT:
    [[b1, v1], [b2, v2], [b3, v3] ,,, ]

OUTPUT:
    [f1, f2, f3 ,,,]

"""
"""
input = [[2, 10], [3, 10], [4, 20], [5, 20]]

N = len(input)

U = [[i, input[i][1]/input[i][0]] for i in range(N)]


def tri_U(element):
    return element[1]


U.sort(key=tri_U)

print(U)
"""

infinity = 10000000000000

Input = [[1, 1], [30, 50]]
W = 100


class Node:
    def __init__(self, i, x, profit, w, evaluation, node):
        self.i = i
        self.x = x
        self.profit = profit
        self.space = w
        self.evaluation = evaluation
        self.parent = node

    def __str__(self):
        return "x" + str(self.i) + " = " + str(self.x)


def afficher(node):
    print("profit = " + str(node.profit))
    while node.i != 0 and node.parent is not None:
        print(node)
        node = node.parent


def branch_and_bound(capacity, items):
    stack = [Node(0, 0, 0, capacity, infinity, None)]

    candidates = []

    number_of_items = len(items)

    borne_inf = -infinity

    while stack:
        top = stack.pop()
        if top.i == number_of_items:
            candidates.append(top)
            borne_inf = max(borne_inf, top.profit)

        elif top.i < number_of_items:
            new_space = top.space
            new_i = top.i + 1
            xi = 0
            while top.space >= items[top.i][1]*xi:

                new_x = xi
                new_profit = top.profit + items[top.i][0]*xi

                new_space = top.space - items[top.i][1]*xi

                new_evaluation = top.evaluation
                new_parent = top
                if new_profit < new_evaluation:
                    stack.append(Node(new_i, new_x, new_profit, new_space, new_evaluation, new_parent))

                xi += 1
            if new_space > 0:
                if new_i < number_of_items:
                    new_parent = top
                    new_x = xi
                    new_profit = top.profit + items[top.i][0] * xi
                    new_evaluation = min(top.evaluation, (items[new_i][0] / items[new_i][1])*new_space)
                    if new_evaluation > borne_inf:
                        stack.append(Node(new_i, new_x, new_profit, new_space, new_evaluation, new_parent))

    solution = candidates.pop()

    for candidate in candidates:
        if candidate.profit > solution.profit:
            solution = candidate
    afficher(solution)


def tri_a(element):
    return element[0]/element[1]


def worker():
    Input.sort(reverse=True, key=tri_a)
    branch_and_bound(W, Input)


worker()
