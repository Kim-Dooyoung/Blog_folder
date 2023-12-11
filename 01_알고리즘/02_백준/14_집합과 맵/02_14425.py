import sys
input = sys.stdin.readline # 시간 효율성

n, m = map(int, input().split())
s = set([input() for _ in range(n)])
cnt = 0
for i in range(m):
    t = input()
    if t in s:
        cnt += 1
print(cnt)