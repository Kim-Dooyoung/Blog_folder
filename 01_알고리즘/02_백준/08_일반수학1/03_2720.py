t = int(input())

for i in range(t):
    c = int(input())
    for j in [25, 10, 5, 1]:
        print(c // j, end=' ')
        c = c % j