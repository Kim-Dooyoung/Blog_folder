# Solution 1

t = int(input()) # 테스트 케이스 입력

for i in range(1, t+1): # 1~t
    a, b = map(int, input().split())
    print("Case #" + str(i) + ":", a+b) # 직접 꾸미기
    
# Solution 2

t = int(input()) # 테스트 케이스 입력

for i in range(1, t+1): # 1~t
    a, b = map(int, input().split())
    print("Case #%s: %s"%(i, a+b)) # 문자열로 꾸미기
    
# Solution 3

t = int(input()) # 테스트 케이스 입력

for i in range(1, t+1): # 1~t
    a,b = map(int,input().split())
    print(f"Case #{i}: {a+b}") # f-string으로 꾸미기