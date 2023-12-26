# Solution 1
n = int(input())
n_list = list(map(int, input().split()))

print(min(n_list), max(n_list))

# Solution 2
n = int(input())
n_list = list(map(int, input().split()))
s = sorted(n_list)

print(s[0], s[-1])