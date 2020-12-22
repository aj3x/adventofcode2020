import userin

def parseInput(s):
    (time, arr) = s.splitlines()
    arr = arr.split(",")
    return (int(time), arr)

def nearestBus(cur, buses):
    while True:
        cur += 1
        for b in buses:
            if cur % b == 0:
                return (cur, b)

# Part 1
(curTime, busOrder) = parseInput(userin.default)
busIDs = [int(x) for x in busOrder if x != "x"]
(t, b) = nearestBus(curTime, busIDs)
part1 = (t - curTime) * b
print(part1)

userin_arr = userin.default.splitlines()
start = userin_arr[0]
busses = ["x" if x == "x" else int(x) for x in userin_arr[1].split(",")]
def part2():
    # Reduce to mods
    mods = {bus: -i % bus for i, bus in enumerate(busses) if bus != "x"}
    vals = list(reversed(sorted(mods)))
    val = mods[vals[0]]
    # first point
    # 
    r = vals[0]
    for b in vals[1:]:
        while val % b != mods[b]:
            val += r
        r *= b
    return val
print(part2())

# once an order is found the repitition pattern appears
# n = 12345678901234567890
# 1 = 0 0 0 0 1 0 0 0 0 1 
# 5 =     0    1    0    1
