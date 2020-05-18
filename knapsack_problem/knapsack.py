VtoS = []
knapsack = []
n_containers = int(input("Number of containers: "))
size = list(map(int, input("Size: ").split()))
value = list(map(int, input("Value: ").split()))
capacity = int(input("Capacity: "))
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
print("Value of knapsack:", sum(knapsack))
