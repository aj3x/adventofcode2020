import userin
# sort arr of ints
# run through list components
  # check difference between this and last item
# add one to list of items with 3 volts
# multiply list of 3 with list of 1

def sumDifferences(arr):
  counts = [1,0]
  prev = 0
  for i in range(0, len(arr)):
    counts[(prev - arr[i] - 1) // 2] +=1
    prev = arr[i]
  return counts

def getCombs(arr):
  prev = [arr[-1] + 3, 0, 0]
  counts = [1, 0, 0]
  for i in range(len(arr)-1, -1, -1):
    numSum = 0
    cur = arr[i]
    branchCount = 0
    for i in range(0,3):
      diff = prev[i] - cur
      if 1 <= diff <= 3:
        # TODO: is this correct
        branchCount += 1
        numSum += counts[i]

    prev = [cur, prev[0], prev[1]]
    counts = [numSum, counts[0], counts[1]]
    # print(prev, counts)
  
  return (prev, counts)

def getCombsBad(arr):
  d = dict()
  d[0] = [1,3]
  prev = []
  for i in range(0, len(arr)):
    a = arr[i]
    prev = arr[i + 1 : i + 4]
    # print(prev)
    d[a] = []
    for p in prev:
      diff = p - a
      if 1 <= diff <= 3:
        d[a].append(p)
  print(d)
  return recurseTree(d, 0, "0")

def recurseTree(d, i, path):
  if len(d[i]) == 0:
    # print(path)
    return 1
  s = 0
  for x in d[i]:
    s += recurseTree(d, x, path + "," + str(x))
  return s

vals = list(map(lambda x: int(x), userin.default.split("\n")))
vals.sort()
[a,c] = sumDifferences(vals)
part1 = a * c
print(part1)

vals.insert(0,0)
print(getCombs(vals)[1][0])
