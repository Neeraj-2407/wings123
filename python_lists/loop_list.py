b = ["Neeraj","sai","vamshi"] #loop through list
for a in b:
    print(a)

x = ["Neeraj","sai","vamshi"] #looping through the index numbers
for i in range(len(x)):
  print(x[i])

x = ["Neeraj","sai","vamshi"]
i = 1
while i < len(x):
  print(x[i])
  i = i + 1

x = ["Neeraj","sai","vamshi"] #it prints all the values in the list
[print(y) for y in x]