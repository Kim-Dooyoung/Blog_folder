a = []

for i in range(5):
    a.append(int(input()))

a = sorted(a)

print(int(sum(a))//5)
print(a[2])