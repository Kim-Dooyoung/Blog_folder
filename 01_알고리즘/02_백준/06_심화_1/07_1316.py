n = int(input())
group_n = n

for i in range(n):
    a = input()
    for j in range(len(a)-1):
        if a[j] == a[j+1]:
            continue
        elif a[j] in a[j+1:]:
            group_n -= 1
            break
print(group_n)