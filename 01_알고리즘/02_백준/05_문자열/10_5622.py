a = list(input())
al = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
time = 0

for i in a:
    for j in al:
        if i in j:
            time += al.index(j) + 3
            
print(time)