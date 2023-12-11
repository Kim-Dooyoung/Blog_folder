x = int(input()) # 총 금액
n = int(input()) # 물건 종류의 수

total = 0 # 더해질 값

for i in range(n): # 1~n
    a, b = map(int, input().split()) # 물건의 가격과 개수를 입력
    total += a * b # n번 a*b를 더해줌

print("Yes" if total == x else "No") # Yes or No