import userin

arr = userin.default.split("\n")

def parseInput(line):
  lineArr = line.split(" ")
  baseColor = lineArr[0] + " " + lineArr[1]
  i = 4
  if lineArr[i] == 'no':
    return (baseColor, [])
  else:
    contains = []
    while i < len(lineArr):
      containCount = lineArr[i]
      containColor = lineArr[i+1] + " " + lineArr[i+2]
      contains.append((containColor, containCount))
      i += 4
    return (baseColor, contains)

def tree(array, reverse=False):
  d = dict()
  for line in array:
    (parentColor, contains) = parseInput(line)
    for (color, count) in contains:
      parent = parentColor
      child = color
      if (reverse):
        child = parentColor
        parent = color
      if not d.get(parent):
        d[parent] = []
      d[parent].append((child, count))
  return d

def getTarget(key):
  d = tree(arr, True)
  visited = set()
  bagCount = 0
  track = d.get(key)
  while len(track):
    [cur, count] = track.pop(0)
    
    # print(cur)
    if not visited.__contains__(cur):
      visited.add(cur)
      if d.has_key(cur):
        track += d[cur]
      bagCount += 1
  return bagCount

def dfs(d, visited, key):
  if visited.get(key):
    return visited.get(key)
  innerBags = d.get(key)
  if innerBags and len(innerBags):
    count = 1
    for (bagName, bagCount) in innerBags:
      x = int(bagCount)
      count += dfs(d, visited, bagName) * int(bagCount)
    visited[key] = count
    return count
  else:
    visited[key] = 1
    return 1
test = '''shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark indigo bags contain 1 dark blue bag.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags.'''
testArr = test.split("\n")
testD = tree(testArr)
visited = dict()
print dfs(tree(arr), visited, "shiny gold") - 1


def countBags(key):
  d = tree(arr)
  visited = dict()
  bagCount = 0
  track = d.get(key)
  print(track)
  while False and len(track):
    [cur, count] = track.pop(0)
    
    # print(cur)
    if visited[cur]:
      visited[cur]
    else:
      if d.has_key(cur):
        track += d[cur]
      bagCount += 1
  return bagCount

# print getTarget("shiny gold")

# countBags("shiny gold")
