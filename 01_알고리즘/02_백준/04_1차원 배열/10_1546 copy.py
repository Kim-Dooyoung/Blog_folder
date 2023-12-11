n = int(input())
score = list(map(int, input().split()))

score = sorted(score)
sum = 0

for i in range(n):
    sum += (score[i]/score[n-1]*100)

print(sum/n)