# solition 1
a = int(input())
b = input()

print(a * int(b[2]))
print(a * int(b[1]))
print(a * int(b[0]))
print(a * int(b))

# 2
a = int(input())
b = input()

for i in range(2, -1, -1):
    print(a * int(b[i]))
print(a * int(b))