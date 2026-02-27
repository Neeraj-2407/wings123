names = ["neeraj","prem","sai"]
for x in names:
    print(x)

#looping through letters in the word by using for loop(looping through a string)
for a in "neeraj":
    print(a)

#stopping the loop before looping through all items
names = ["neeraj","prem","sai"]
for x in names:
    print(x)
    if x =="prem":
        break

#to stop current iteration and continue to next step by using continue
names = ["neeraj","prem","sai"]
for x in names:
    if x =="prem":
        continue
    print(x)

#print sequence of numbers using range()
for x in range(2, 16):
  print(x)

#changing the increment values bby using it as a third parameter
for x in range(2, 116, 20):
  print(x)

#we use else to print a message once loop statement is false
for x in range(12):
   print(x)
else:
  print("Finished Loop")

#nested for loops
colour = ["red","green","white"]
thing =  ["bat","ball","helmet"]
for a in colour:
   for b in thing:
      print(a,b)  