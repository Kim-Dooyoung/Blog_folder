n = int(input())
a = list(map(int, input().split()))

m = int(input())
b = list(map(int, input().split()))
    
result = {}

for i in b:
    result[i] = 0
    
for j in a:
    if j in result:
        result[j] = 1
        
for k in result:
    print(result[k], end=' ')