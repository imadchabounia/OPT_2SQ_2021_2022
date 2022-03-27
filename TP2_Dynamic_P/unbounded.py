import time
def knapSack(W, wt, val):
    n = len(val)
    table = [[0 for x in range(W + 1)] for x in range(n + 1)]
    optimal_items = list()
    Items = list()
    for i in range(n + 1):
        for j in range(W + 1):
            if i == 0 or j == 0:
                table[i][j] = 0
            elif wt[i - 1] <= j:
                table[i][j] = max(val[i - 1] + table[i - 1][j - wt[i - 1]], table[i - 1][j])
            else:
                table[i][j] = table[i - 1][j]
    res = table[n][W]
    w = W
    for i in range(n, 0, -1):
        if res <= 0:
            break
        if res == table[i - 1][w]:
            continue
        else:
            optimal_items.append(wt[i - 1])
            Items.append("élément " + str(i))
            res = res - val[i - 1]
            w = w - wt[i - 1]

    return table[n][W],optimal_items, Items



capacity= int(input("Donnez la capacité du sac à dos: "))
nbr= int(input("Donnez le nombre d'objets: "))
#items= []
wt=[]
val=[]

for i in range(nbr):
    wt.append(int(input("poids de l\'objet: ")))
    val.append(int(input("valeur de l\'objet: ")))

print("poid list= ",wt)
print("valeur list= ",val)
#print (knapsack_dp(items,capacity))
start = time.time()
resTab, sol, items = knapSack(capacity,wt,val)
fin = time.time()
print("solution = ",items)
print("time = ", (fin-start)*100)
#print("TAB = ",resTab)
#print("Items = ",sol)