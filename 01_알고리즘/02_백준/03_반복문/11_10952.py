while 1: # 무한 반복
    a, b = map(int, input().split())
    if a == 0 and b == 0: # a, b 둘 다 0이면
        break # 반복 종료
    else:
        print(a+b) # 합을 출력