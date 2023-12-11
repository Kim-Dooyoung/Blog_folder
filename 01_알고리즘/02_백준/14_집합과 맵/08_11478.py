s = input()
a = set()

for i in range(len(s)):
    for j in range(i, len(s)):
        temp = s[i:j+1]
        a.add(temp)
print(len(a))