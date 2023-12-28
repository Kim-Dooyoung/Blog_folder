# Solutio 1

n = []

for i in range(10):
    a = int(input())
    n.append(a % 42)
    
print(len(set(n)))

# Solution 2

n = []
for i in range(10):
    a = int(input())
    if a%42 not in n:
        n.append(a % 42)

print(len(n))