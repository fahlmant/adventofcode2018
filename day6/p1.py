with open('input') as f:
    lines = [line.rstrip('\n') for line in f]

points = []
infiniteAreaPoints = []

for line in lines:
    x = int(line[:line.find(',')])
    y = int(line[line.find(',')+1:])
    points.append((x,y))

def mannDist(point1, point2):
    return (abs(point1[0] - point2[0]) + abs(point1[1] + point2[1]))

#find the closest point for each point in the grid
#ignore infinite spaces
#count areas of each finite space