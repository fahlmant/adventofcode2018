from itertools import accumulate, cycle
with open('input') as f:
        lines = f.readlines()
numseen = set()
print(next(i for i in accumulate(cycle(lines)) if i in numseen or numseen.add(i)))
