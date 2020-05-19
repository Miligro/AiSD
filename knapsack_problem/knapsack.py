import random
import time

def greedy(weight_g, capacity_g, value_g, n_cont):
    v_s = []
    knapsack = []
    for i in range(n_cont):
        v_s.append(value_g[i] / weight_g[i])
    while True:
        if v_s:
            x = max(v_s)
            index = v_s.index(x)
            if capacity_g < min(weight_g):
                break
            if capacity_g >= weight_g[index]:
                knapsack.append(value_g[index])
                capacity_g = capacity_g - weight_g[index]
                v_s = v_s[:index] + v_s[index + 1:]
                weight_g = weight_g[:index] + weight_g[index + 1:]
                value_g = value_g[:index] + value_g[index + 1:]
            else:
                v_s = v_s[:index] + v_s[index + 1:]
        else:
            break
    return knapsack


def dynamic(weight_d, capacity_d, value_d, n_con):
    dyn = [[0 for x in range(capacity_d + 1)] for y in range(n_con + 1)]
    for i in range(1, n_con + 1):
        for j in range(1, capacity_d + 1):
            if j < weight_d[i - 1]:
                dyn[i][j] = dyn[i - 1][j]
            else:
                dyn[i][j] = max(dyn[i - 1][j], dyn[i - 1][j - weight_d[i - 1]] + value_d[i - 1])
    return dyn[n_con][capacity_d]

# generator


for i in range(1, 16):
    weight_R = []
    value_R = []
    for j in range(1000 * i):
        weight_R.append(random.randrange(1, 10))
        value_R.append(random.randrange(10, 100))
    capacity_R = 500
    start = time.time()
    print("Value of knapsack (dynamic-programming):", dynamic(weight_R, capacity_R, value_R, 1000*i))
    end = time.time()
    total = end - start
    print("{0:02f}s".format(total))
    start = time.time()
    print("Value of knapsack (greedy):", sum(greedy(weight_R, capacity_R, value_R, 1000*i)))
    end = time.time()
    total = end - start
    print("{0:02f}s".format(total))
