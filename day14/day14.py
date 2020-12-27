import userin

def part1():
    user_input = userin.default.splitlines()
    memory = {}
    mask = ['X', 'X']
    for line in user_input:
        [cmd, val] = line.split(" = ")
        if cmd == 'mask':
            mask[0] = int(val.replace('X', '1'), 2)
            mask[1] = int(val.replace('X', '0'), 2)
        else:
            memAddress = cmd[4:-1]
            memory[memAddress] = int(val) & mask[0] | mask[1]
    return sum(list(memory.values()))


print(part1())


def part2():
    user_input = userin.default.splitlines()
    memory = {}
    maskBase = "X"
    maskOptions = []
    for line in user_input:
        [cmd, val] = line.split(" = ")
        if cmd == 'mask':
            mask = val
            maskBase = int(mask.replace('X', '0'), 2)
            maskOptions = [i for (i, x) in enumerate(mask) if x == 'X']
        else:
            memAddress = int(cmd[4:-1]) | maskBase
            memory[memAddress] = int(val)
            # 2 ^ n
            moLen = len(maskOptions)
            for i in range(0, 2 ** moLen):
                mask = [["1"] * 36, ["0"] * 36]
                
                for maskI, maskVal in enumerate(('0' * moLen + (bin(i)[2:]))[-moLen:]):
                    mask[int(maskVal)][maskOptions[maskI]] = maskVal
                mask = list(map(lambda x: int("".join(x), 2), mask))
                addr = (memAddress & mask[0]) | mask[1]
                memory[addr] = int(val)
    print(sum(list(memory.values())))

part2()
