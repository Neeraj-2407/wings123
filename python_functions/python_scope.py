#local variable
def myfunc():
  x = 300
  print(x)
myfunc()

#global variable
x = 300
def myfunc():
   print(x)
myfunc()
print(x)

#making variable global using global keyword
x = 300
def myfunc():
   global x 
   x = 200
myfunc()
print(x)
