import userin
# 

# sort range of numbers
# while sorting add to key map

def convertArr(item):
  return int(item)

preamble = 25
parsedArray = map(convertArr, userin.default.splitlines())


# check numbers between (n/2,n)
  # binary search sorted array for being in between range
  # try going up and down till reaching bounds

def verifyNumber(key, numarr):
  lowerBound = key/2
  upperBound = key
  numset = set(numarr)
  for num in numarr:
    if numset.__contains__(key - num):
      return True
  return False

# Solve for Key
# for i in range(preamble, len(parsedArray)):
#   preambleArr = parsedArray[i - preamble:i]
#   num = parsedArray[i]
#   if not verifyNumber(num, preambleArr):
#     print num

def checkSumArr(arr, val):
  for kSum in arr:
    if kSum == val:
      return True
  return False 

def getSumArr(key, arr):
  sumArr = []
  for i in range(0, len(arr)):
    curNum = arr[i]
    sumArr = map(lambda val: val + curNum, sumArr)
    if checkSumArr(sumArr, key):
      return arr[sumArr.index(key)] + arr[i - 1]
    sumArr.append(curNum)

print getSumArr(507622668, parsedArray)