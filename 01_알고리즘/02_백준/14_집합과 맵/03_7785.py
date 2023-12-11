import sys

n = int(sys.stdin.readline())
result = {}

for _ in range(n):
    a, b = map(str, sys.stdin.readline().split())
    
    if b == "enter":
        result[a] = b
    else:
        del result[a]
    
result = sorted(result.keys(), reverse=True)

for i in result:
    print(i)