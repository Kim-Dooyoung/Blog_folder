# 출력 초과
# nums = list(map(int, input().split()))
# x_lst = []
# y_lst = []

# for x in range(-999, 1000):
#     for y in range(-999, 1000):
#         if nums[0] * x + nums[1] * y == nums[2]:
#             x_lst.append(x)
#             y_lst.append(y)
            
# for i in x_lst:
#     for j in y_lst:
#         if nums[3] * i + nums[4] * j == nums[5]:
#             print(i, j)

a, b, c, d, e, f = map(int, input().split())

for i in range(-999, 1000):
    for j in range(-999, 1000):
        if (a*i) + (b*j) == c and (d*i) + (e*j) == f:
            print(i, j)