import sys
filePath = sys.argv[1]
file = open(filePath, "r")
nums = list(map(int, file.read().splitlines()))
file.close()
average = int(round(sum(nums)/float(len(nums))))
minMoves = 0
for num in nums:
    minMoves += abs(average-num)
print(minMoves)
