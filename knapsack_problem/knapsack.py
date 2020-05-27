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


file = open("dane.txt", "w")
file.write("weight_d;weight_g;time_d;time_g\n")
for i in range(1, 16):
    weight_R = []
    value_R = []
    for j in range(1000 * i):
        weight_R.append(random.randrange(20, 40))
        value_R.append(random.randrange(10, 100))
    capacity_R = 500
    start = time.time()
    d = dynamic(weight_R, capacity_R, value_R, 1000*i)
    end = time.time()
    time_d = end - start
    print("Value of knapsack (dynamic-programming):", d)
    print("{0:02f}s".format(time_d))
    start = time.time()
    g = sum(greedy(weight_R, capacity_R, value_R, 1000*i))
    end = time.time()
    time_g = end - start
    print("Value of knapsack (greedy):", g)
    print("{0:02f}s".format(time_g))
    file.write(str(d))
    file.write(";")
    file.write(str(g))
    file.write(";")
    file.write("{0:02f}".format(time_d))
    file.write(";")
    file.write("{0:02f}\n".format(time_g))


file.close()
