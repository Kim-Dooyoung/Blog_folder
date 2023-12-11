n = int(input())
paper = [[0 for i in range(101)] for j in range(101)]
count = 0

for i in range(n):
    x, y = map(int, input().split())
    
    for j in range(x, x+10):
        for k in range(y, y+10):
            paper[j][k] = 1
            
for i in range(100):
    count += paper[i].count(1)

print(count)