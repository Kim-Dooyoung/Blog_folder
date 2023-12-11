s = [i for i in range(1, 31)]

for _ in range(28):
    a = int(input())
    s.remove(a)
    
print(min(s))
print(max(s))