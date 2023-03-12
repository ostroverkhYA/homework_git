size = 5
for (i % 2)   in range(0, size):
    for j in range(0, size):
        print(end=" ")
    size = size - 1
    for j in range(0, i + 1):
        print("*", end=' ')
    print(" ")
