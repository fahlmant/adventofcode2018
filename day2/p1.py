import collections

with open('input') as f:
    lines = f.readlines()

numTwos = 0
numThrees = 0
i = 0
results = [None]*len(lines)
def getResults(line):
    result = collections.Counter(line)
    return result

for line in lines:
    results[i] = getResults(line)
    if 2 in (results[i].values()):
        numTwos = numTwos + 1
    if 3 in (results[i].values()):
        numThrees = numThrees + 1
    i = i+1

print(numTwos*numThrees)
