# solution 1

# a = list(str(input()))
# b = list(reversed(a))

# if a == b:
#     print(1)
# else:
#     print(0)
    
# solution 2
a = list(input())

if a == list(a[::-1]):
    print(1)
else:
    print(0)