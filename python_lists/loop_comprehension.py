names = ["neeraj","sai","rohit","prem","raghav","vamshi"]
newlist = []

for x in names:
  if "e" in x:
    newlist.append(x)

print(newlist)

names = ["neeraj","sai","rohit","prem","raghav","vamshi"]

newlist = [x for x in names if "e" in x]

print(newlist)