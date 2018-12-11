with open('input') as f:
    items =  f.read().split()

def sumOfMetadata(node):
    result = 0
    for value in node[0]:
        result += value
    for child in node[1]:
        result+= sumOfMetadata(child)
    return result

def parseTree(root):
    childrenNodes = []
    metaNodes = []

childNodeNum = items[0]
metadataNum = items[1]


