import userin
from parse import *

arr = userin.default.splitlines(False)
a = '''nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6'''.splitlines()

def parseLine(x):
  return (x[:3],int(x[4:]))

def getNextOp((op, num)):
  if (op == "jmp"):
    return num
  else:
    return 1

def parseOp(line):
  return getNextOp(parseLine(line))

def accumulate(nodes):
  s = set()
  cur = 0
  accum = 0
  while 0<=cur<len(nodes) and not s.__contains__(cur):
    s.add(cur)
    op = parseLine(nodes[cur])
    if op[0] == "acc":
      accum += op[1]
    cur += getNextOp(op)
  return accum

# print accumulate(arr)

def floyd(nodes):
  tortoise = 0
  hare = parseOp(nodes[0])
  while 0 <= hare < len(nodes) and tortoise != hare:
    tortoise += parseOp(nodes[tortoise])
    hare += parseOp(nodes[hare])
    if (tortoise == hare):
      break
    hare += parseOp(nodes[hare])
  return (tortoise, hare)

def checkCode(lines, visited=set(), startIndex=0):
  curLine = startIndex

  while not visited.__contains__(curLine) and 0 <= curLine < len(lines):
    visited.add(curLine)
    curLine += parseOp(lines[curLine])
  return curLine == len(lines)

def fixCode(lines):
  fullset = set()
  firstOp = 0
  fullset.add(firstOp)

  while (len(fullset) < len(lines)):
    curSet = fullset.copy()
    curOp = firstOp
    change = True
    (changeOp, changeNum) = parseLine(lines[firstOp])
    if (changeOp == "acc"):
      curOp += 1
      change = False
    elif (changeOp == "jmp"):
      curOp += 1
    elif (changeOp == "nop"):
      curOp += changeNum
    
    if change and checkCode(lines, curSet, curOp):
      return firstOp
    else:
      fullset.add(firstOp)
      firstOp += parseOp(lines[firstOp])

val = parseLine(arr[216])
# arr[216] = "nop -44"

print accumulate(arr)
# print checkCode(arrChanged)
    # if change:
    #   while (not fullset.__contains__(curOp))

# change op
# go through list until loop or end
# if end return cur changed index
# else go to next op and try to change

# print floyd(arr)

