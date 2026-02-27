#if we have only 1 statement we can put print and if in same line
#shorthand if 
a = 5
b = 2
if a > b: print("a is greater than b")

#shorthand if-else
a = 156
b = 200
print("A") if a > b else print("B")

#assigning a value with if-else
a = 10
b = 20
x = a if a > b else b
print("Bigger is", x)

#multiple commands in one line
a = 22
b = 33
print("A") if a > b else print("=") if a == b else print("B")

#maximun of 2 numbers
x = 15
y = 20
a = x if x > y else y
print("Maximum value:", a)