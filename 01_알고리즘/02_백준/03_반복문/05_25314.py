# Solution 1

n = int(input()) // 4 # n을 4로 나눈 몫을 구한다

for i in range(n): # 몫만큼 반복
    print("long") # 몫만큼 "long" 출력
print("int") # 마지막에 "int"출력

# Solution 2

n = int(input())

print("long " * (n//4) + "int") # n을 4로 나눈 몫만큼 "long"을 반복