# Solution 1

s = [i for i in range(1, 31)]

for j in range(28):
    a = int(input())
    s.remove(a)
    
print(min(s))
print(max(s))