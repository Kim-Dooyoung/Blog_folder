case = int(input())

for i in range(case):
    r, s = list(map(str, input().split()))
    r = int(r)
    s = str(s)
    for j in range(len(s)):
        print(s[j] * r, end = '')
    print('')