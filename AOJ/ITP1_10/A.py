import math
x1, y1, x2, y2 = map(float, input().split())
# sqrtは平方根
L = math.sqrt((x1-x2)**2 + (y1-y2)**2)
# L = ((x1-x2)**2 + (y1-y2)**2)**0.5
print(L)