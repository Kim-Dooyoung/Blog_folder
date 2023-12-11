while 1: # 반복
    try: # 실행할 코드
        a, b = map(int, input().split())
        print(a+b)
    except: # 예외가 발생했을 때 처리하는 코드
        break