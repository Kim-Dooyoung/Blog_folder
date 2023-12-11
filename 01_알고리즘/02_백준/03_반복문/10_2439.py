n = int(input())

for i in range(n):
    print(" " * (n-i-1) + "*" * (i+1)) # 공백은 n-i-1만큼 *d은 i+1만큼 반복