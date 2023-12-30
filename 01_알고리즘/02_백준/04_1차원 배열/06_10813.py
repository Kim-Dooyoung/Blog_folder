# Solution 1

n, m = map(int, input().split())
basket = list(range(1, n+1))

for x in range(m):
    i, j = map(int, input().split())
    basket[i-1], basket[j-1] = basket[j-1], basket[i-1]
    
print(*basket, end=" ")

# Solution 2

n, m = map(int, input().split())
basket = list(range(1, n+1))

for x in range(m):
    i, j = map(int, input().split())
    basket[i-1], basket[j-1] = basket[j-1], basket[i-1]

for y in range(len(basket)):
    print(basket[y], end=" ")
    
# Solution 3

n, m = map(int, input().split())
basket = list(range(1, n+1))

for x in range(m):
    i, j = map(int, input().split())
    temp = basket[i-1]
    basket[i-1] = basket[j-1]
    basket[j-1] = temp
    
print(*basket, end=" ")