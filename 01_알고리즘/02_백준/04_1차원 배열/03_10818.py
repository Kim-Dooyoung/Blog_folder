# solution 1
# n = int(input())
# m = list(map(int, input().split()))
# s = sorted(m)

# print(s[0], s[-1])

# solution 2
n = int(input())
numbers = list(map(int, input().split()))

print(min(numbers), max(numbers))