VtoS = []
knapsack = []
n_containers = int(input("Number of containers: "))
size = list(map(int, input("Weight: ").split()))
value = list(map(int, input("Value: ").split()))
capacity = int(input("Capacity: "))

q = n_containers
e = capacity

Dyn = [[0 for x in range(capacity + 1)] for y in range(n_containers + 1)]
for i in range(1, n_containers + 1):
    for j in range(1, capacity + 1):
        if j < size[i - 1]:
            Dyn[i][j] = Dyn[i - 1][j]
        else:
            Dyn[i][j] = max(Dyn[i - 1][j], Dyn[i - 1][j - size[i - 1]] + value[i - 1])

for i in range(n_containers):
    VtoS.append(value[i] / size[i])

while True:
    if VtoS:
        x = max(VtoS)
        index = VtoS.index(x)
        if capacity < min(size):
            break
        if capacity >= size[index]:
            knapsack.append(value[index])
            capacity = capacity - size[index]
            VtoS = VtoS[:index] + VtoS[index + 1:]
            size = size[:index] + size[index + 1:]
            value = value[:index] + value[index + 1:]
        else:
            VtoS = VtoS[:index] + VtoS[index + 1:]
    else:
        break
print("Value of knapsack (greedy):", sum(knapsack))

print("Value of knapsack (dynamic-programming):", Dyn[q][e])
