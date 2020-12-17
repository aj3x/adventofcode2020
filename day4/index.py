from parse import *;
import userin
import re

format = "{}:{}"

def parseDict(rowStr, d=dict()):
  arr = rowStr.split(" ")
  for entry in arr:
    [key, value] = parse(format, entry)
    d[key] = value
  return d

ui = userin.default.split("\n")

requiredFields = ['ecl', 'pid', 'eyr', 'hcl', 'byr', 'iyr', 'hgt']
def fieldValidator(d):
  adder = 1
  for field in requiredFields:
    val = d.get(field)
    if val == None and field != 'cid':
      adder = 0
    elif (field == 'byr' and not(len(val)==4 and 1920 <= int(val) <= 2002)):
      adder = 0
    elif (field == 'iyr' and not(len(val)==4 and 2010 <= int(val) <= 2020)):
      adder = 0
    elif (field == 'eyr' and not(len(val)==4 and 2020 <= int(val) <= 2030)):
      adder = 0
    elif (field == 'hgt' and not re.match("^((59|6[0-9]|7[0-6])in)|(1(([5-8][0-9])|(9[0-3]))cm)$", val)):
      adder = 0
    elif (field == 'hcl' and not(re.match("^#[0-9a-f]{6}$", val))):
      adder = 0
    elif (field == 'ecl' and not(re.match("^(amb|blu|brn|gry|grn|hzl|oth)$", val))):
      adder = 0
    elif (field == 'pid' and not(re.match("^[0-9]{9}$", val))):
      adder = 0
  return adder

items = []
cur = dict()
count = 0
for item in ui:
  if (item == ""):
    items.append(cur)
    count += fieldValidator(cur)
    cur = dict()
  if (item != ""):
    cur = parseDict(item, cur)

print count
# print not(re.match("^#[0-9a-f]{6}$", "#124356"))
# print re.match("^((59|6[0-9]|7[0-6])in)|(1(([5-8][0-9])|(9[0-3]))cm)$", "150cm")

