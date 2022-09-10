n, m = int(input()), int(input())
m = m-1
targetList = []
i = 0
while i < n*m:
    x = i%n+1
    if i%m == 0:
        targetList.append(x)
    i += 1
    if i%n == 0 and i%m == 0 and targetList:
        break
print(targetList)
