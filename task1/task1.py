import sys
n, m = int(sys.argv[1]), int(sys.argv[2])
m = m-1
targetList = []
i = 0
iMax = n*m
while i < iMax:
    x = i%n+1
    if i%m == 0:
        targetList.append(x)
    i += 1
    if i%n == 0 and i%m == 0 and targetList:
        break
print(''.join(map(str, targetList)))
