import userin
def getPosition (val):
  row = int(val[:7].replace("F", '0').replace("B", '1'),2)
  col = int(val[7:].replace("L", '0').replace("R", '1'),2)
  return [row, col]

def getSeatID(pos):
  return pos[0] * 8 + pos[1]

def getSeatIDStr(str):
  return int(str.replace("F", '0').replace("B", '1').replace("L", '0').replace("R", '1'), 2)

def getBoundsID(arr):
  maxID = -1
  minID = 999999999999999
  idSum = 0
  for item in arr:
    seatID = getSeatID(getPosition(item))
    idSum += seatID
    maxID = max(seatID, maxID)
    minID = min(seatID, minID)
  return [minID, maxID, idSum]

def getMissing(arr):
  [n,m,s] = getBoundsID(arr)
  # include min value in count
  return (m*(m+1)/2) - (n*(n-1)/2) - s


print getMissing(userArr)
