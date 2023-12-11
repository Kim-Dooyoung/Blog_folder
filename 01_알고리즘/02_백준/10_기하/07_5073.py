# while 1:
#     a, b, c = map(int, input().split())
#     if a == b == c == 0:
#         break
    
#     if a == b == c:
#         print("Equilateral")
#     elif a == b or b == c or c == a:
#         print("Isosceles")
#     elif a != b != c:
#         print("Scalene")
#     else:
#         print("Invalid")

while True :
    a, b, c = map(int, input().split())
    if a == b == c == 0 :
        break
    if sum((a, b, c)) - max((a, b, c)) <= max((a, b, c)) :
        print("Invalid")
    elif a == b == c :
        print('Equilateral')
    elif a == b or b == c or a == c :
        print("Isosceles")
    else :
        print("Scalene")