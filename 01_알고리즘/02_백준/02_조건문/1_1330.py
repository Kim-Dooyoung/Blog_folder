# 1
a, b = map(int, input().split())

if a > b:
    print('>')
elif a < b:
    print('<')
else:
    print('==')

# 2
a, b = map(int, input().split())

print(">" if a > b else "<" if a < b else "==")

# true_value if condition else false_value
# true_value if condition1 else true_value2 if condition2 else false_value
