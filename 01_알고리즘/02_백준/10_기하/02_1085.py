x, y, w, h = map(int, input().split())

a = [x, (w-x), y, (h-y)]

print(min(a))