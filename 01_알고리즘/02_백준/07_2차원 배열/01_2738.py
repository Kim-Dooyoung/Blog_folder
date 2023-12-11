n, m = map(int, input().split())
a = []
b = []

for i in range(n):
    a.append(list(map(int, input().split())))

for i in range(n):
    b.append(list(map(int, input().split())))
    
for i in range(n):
    for j in range(m):
        print(int(a[i][j]) + int(b[i][j]), end=' ')
    print()
    