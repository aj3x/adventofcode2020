import userin

def parseInput(s):
    (time, arr) = s.splitlines()
    arr = arr.split(",")
    arr = [int(x) for x in arr if x != "x"]
    return (int(time), arr)

def nearestBus(cur, buses):
    while True:
        cur += 1
        for b in buses:
            if cur % b == 0:
                return (cur, b)

(curTime, busIDs) = parseInput(userin.default)
(t, b) = nearestBus(curTime, busIDs)
part1 = (t - curTime) * b
print(part1)
