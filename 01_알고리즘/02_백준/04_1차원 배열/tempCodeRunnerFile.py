n = int(input())
lst = []
lst_2 = []

for _ in range(n):
    lst.append(int(input()))
    
for i in range(n):
    lst_2.append(lst[i] / max(lst) * 100)
    
print(sum(lst_2) / n)