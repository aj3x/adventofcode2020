import userin


FLOOR = "."
EMPTY_SEAT = "L"
OCCUPIED_SEAT = "#"

def inBounds(arr, m, n):
    return 0<=n<len(arr[0]) and 0<=m<len(arr)

def posOccupied(arr, m, n, i, j):
    m += i
    n += j
    return 0 <= n < len(arr[0]) and 0 <= m < len(arr) and arr[m][n] == OCCUPIED_SEAT

def checkSight(arr, m, n, i, j):
    m += i
    n += j
    if not inBounds(arr, m, n):
        return False
    seat = arr[m][n]
    if seat == OCCUPIED_SEAT:
        return True
    if seat == EMPTY_SEAT:
        return False
    return checkSight(arr, m, n, i, j)

def neighbourCount(arr, m, n, func):
    count = 0
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            if i == j == 0:
                continue
            count += func(arr, m, n, i, j)
    return count

# If a seat is empty (L) and there are no occupied seats adjacent to it, the seat becomes occupied.
# If a seat is occupied (#) and four or more seats adjacent to it are also occupied, the seat becomes empty.
# Otherwise, the seat's state does not change.
def nextSeat(m, n, arr):
    seat = arr[m][n]
    nCount = neighbourCount(arr, m, n, posOccupied)
    if seat == EMPTY_SEAT and nCount == 0:
        return OCCUPIED_SEAT
    elif seat == OCCUPIED_SEAT and nCount >= 4:
        return EMPTY_SEAT
    return seat
def nextSeatSight(m, n, arr):
    seat = arr[m][n]
    nCount = neighbourCount(arr, m, n, checkSight)
    if seat == EMPTY_SEAT and nCount == 0:
        return OCCUPIED_SEAT
    elif seat == OCCUPIED_SEAT and nCount >= 5:
        return EMPTY_SEAT
    return seat

def nextArr(arr, func):
    newArr = []
    for i in range(0, len(arr)):
        newArr.append("")
        for j in range(0, len(arr[0])):
            newArr[i] += func(i,j, arr)
    return newArr

def cycleSeats(arr):
    return nextArr(arr, nextSeat)

def cycleSeatsSight(arr):
    return nextArr(arr, nextSeatSight)

def getStableSeats(arr):
    cur = arr
    prev = None
    while prev != cur:
        prev = cur
        cur = cycleSeatsSight(cur)
    occCount = 0
    for row in cur:
        occCount += row.count(OCCUPIED_SEAT)
    return occCount

def printSeats(arr):
    for row in arr:
        print(row)
x = userin.default.splitlines()
part1 = getStableSeats(x)
print(part1)
