#indicating "no value" or "not set" by using none
a = None
print(a)

#printing the data type of none using type()
a = None
print(type(a))

#using is,isnot for comparisions
user = None
if user is None:
    print("No user logged in")
else:
    print("Welcome back!")

#isnot
user = "neeraj"
if user is not None:
    print("welcome back")
else:
    print("No user logged in")   

#functions returning none
def myfunc():
  x = 10

x = myfunc()
print(x)    