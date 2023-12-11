m = int(input())
n = int(input())
a = []

for i in range(m, n+1):
    error = 0
    if i > 1:
        for j in range(2, i):
            if i % j == 0:
                error += 1
                break
        if error == 0:
            a.append(i)
            
if len(a) == 0:
    print(-1)
else:
    print(sum(a))
    print(min(a))