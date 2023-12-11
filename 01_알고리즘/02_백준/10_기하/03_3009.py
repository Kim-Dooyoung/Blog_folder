a = []
b = []

for i in range(3):
    x, y = map(int, input().split())
    a.append(x)
    b.append(y)
    
for i in range(3):    
    if a.count(a[i]) == 1:
        x1 = a[i]
    if b.count(b[i]) == 1:
        y1 = b[i]
        
print(x1, y1)