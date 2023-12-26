n, m = map(int, input().split())
basket = list(range(1, n+1))

for x in range(1, m+1):
    i, j = map(int, input().split())
    basket[i], basket[j] = basket[j], basket[i]
    
print(basket)