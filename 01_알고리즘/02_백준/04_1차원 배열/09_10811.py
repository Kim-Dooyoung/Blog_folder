# Solution 1

n, m = map(int, input().split())
basket = [x for x in range(1, n+1)]
for y in range(m):
    i, j = map(int, input().split())
    r = j - i + 1
    for z in range(r//2):
        temp = basket[i-1]
        basket[i-1] = basket[j-1]
        basket[j-1] = temp
        i += 1
        j -= 1

for o in basket:
    print(o, end=' ')
    
# Solution 2

n, m = map(int, input().split())

basket = [x for x in range(1, n+1)]

for y in range(m):
    i, j = map(int, input().split())
    r = j - i + 1
    for z in range(r//2):
        basket[i-1], basket[j-1] = basket[j-1], basket[i-1]
        i += 1
        j -= 1
        
print(*basket)