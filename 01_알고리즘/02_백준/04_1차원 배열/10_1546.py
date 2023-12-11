n = int(input())
lst = list(map(int, input().split()))
lst_2 = []

for i in range(n):
    lst_2.append(lst[i] / max(lst) * 100)
    
print(sum(lst_2) / n)