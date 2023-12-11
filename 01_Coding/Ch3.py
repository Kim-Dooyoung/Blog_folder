#3.1

#3.1.1

print(1 + 1)
print(3 - 2)
print(5 * 2)
print(6 / 3)

print(2 ** 3)
print(10 % 3)
print(10 // 3)

# 3.1.2

print(10 > 3)
print(4 >= 7)
print(10 < 3)
print(5 <= 5)

print(3==3)
print(4==2)
print(3+4==7)
print(1!=3)

# 3.1.3

print((3>0) and (3>5))
print((3>0) or (3>5))
print(not(1!=3))

print(5>4>3)
print(4>5>3)

# 3.2

print(2+3*4)
print((2+3)*4)

# 3.3

number=2+3*4
print(number)

number=2+3*4+2
print(number)

number=2+3*4
print(number)
number=number+2 #(2+3*4)+2
print(number)

number=2+3*4
print(number)

number+=2
print(number)
number-=2
print(number)
number*=2
print(number)
number/=2
print(number)
number**=2
print(number)
number//=2
print(number)
number%=2
print(number)

# 3.4

# 3.4.1

print(abs(-5))
print(pow(4,2))
print(max(5,12))
print(min(5,12))
print(round(3.14))
print(round(4.678,2))

#3.4.2

from math import *

result=floor(4.99)
print(result)
result=ceil(3.14)
print(result)
result=sqrt(16)
print(result)

import math 

result=math.floor(4.99)
print(result)
result=math.ceil(3.14)
print(result)
result=math.sqrt(16)
print(result)

# 3.4.3

from random import *

print(random())
print(random())
print(random())

print(random()*10)
print(int(random()*10))
print(int(random()*10)+1)

print(int(random()*45+1))

print(randrange(1,46))
print(randint(1,45))

print(randint(1,45))
print(randint(1,45))
print(randint(1,45))
print(randint(1,45))
print(randint(1,45))
print(randint(1,45))

# 실습 문제

from random import *

date=randint(4,28)

print("오프라인 스터디 모임 날짜는 매월 "+ str(date) +"일로 선정됐습니다.")

# 셀프체크

celsius=30
fahrenheit=(celsius*9/5)+32

print('섭씨 온도 : '+str(celsius))
print('섭씨 온도 : '+str(fahrenheit))
