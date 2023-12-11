n = []
for i in range(9):
    n.append(int(input()))

print(max(n), n.index(max(n))+1)