# whileloop
i = 1
while i < 6:
  print(i)
  i += 1

# printing even numbers by using while loop
i = 2
while i <=15:
  print(i)
  i+=2

# stopping the loop when condition is true using break statement
i = 2
while i < 15:
  print(i)
  if i ==10:
    break
  i +=2

# to stop current iteration and continue to next step by using continue
i = 2
while i < 9:
  i += 1
  if i==5:
    continue
  print(i)

#printing a message if condition is false by using else statement
i = 1
while i < 7:
  print(i)
  i += 1
else:
  print("i reached 7,loop stopped")