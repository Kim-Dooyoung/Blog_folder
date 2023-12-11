# Solution 1

n = int(input())
total = 0 # 더해지는 값

for i in range(1, n+1): # 1~n
    total += i # 1부터 n까지 값이 계속 더해짐
    
print(total)

# Solution 2

n = int(input())

print(sum(range(1, n+1))) # 1~n까지 합을 출력

# Solution 3

print(sum(range(1, int(input()) + 1)))