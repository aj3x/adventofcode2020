
# init
vals = [0,3,6]
import time
def part1(stopIndex):
    numSet = dict()
    for i in range(len(vals)):
        val = vals[i]
        index = i+1
        numSet[val] = index
        
    index = len(vals)
    prevNumber = vals[-1]
    ts = time.time()
    while index < stopIndex:
        prevIndex = numSet.get(prevNumber)
        if prevIndex == None:
            curNumber =  0
        else:
            curNumber = index - prevIndex
        numSet[prevNumber] = index
        prevNumber = curNumber
        index += 1
    tf = time.time()
    print(tf - ts)
    print(index, prevNumber)

def alternate(stopIndex):
    indexes = dict()
    for i in range(len(vals)):
        indexes[vals[i]] = i + 1
    bucket = None
    target = vals[-1]
    ts = time.time()
    for index in range(len(vals), stopIndex):
        target = index - indexes.get(target) if indexes.__contains__(target) else 0
        indexes[bucket] = index
        bucket = target
    tf = time.time()
    print(tf - ts)
    print(target)

alternate(2020)
part1(30000000)