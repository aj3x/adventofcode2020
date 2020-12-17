import userin

arr = userin.default.split("\n")

def parseSet(string, s):
  for char in string:
    s.add(char)
  return s

s = None
count = 0
for string in arr:
  if (string == ''):
    count+= len(list(s))
    s = None
  elif s == None:
    s = parseSet(string, set())
  else:
    s = s.intersection(parseSet(string, set()))

print(count)

