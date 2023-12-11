lst = list(map(int, input().split()))
lst_2 = [1, 1, 2, 2, 2, 8]

for i in range(6):
    if lst[i] != lst_2[i]:
        print(int(lst_2[i]) - int(lst[i]))
    else:
        print(0)
        
# 2
lst = list(map(int, input().split()))
lst_2 = [1, 1, 2, 2, 2, 8]
for i in range(6):
    print(int(lst_2[i]) - int(lst[i]))