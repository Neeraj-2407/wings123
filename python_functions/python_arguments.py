#arguments are the values passes into a function when you call it
def student(rollno):
    print("My rollno is",rollno)
student(24)
student(17)
student(18)

#arguments and parameters
def student(rollno): #rollno is parameter
    print("My rollno is",rollno)
student(24)
student(17)
student(18) #24,17,18 are the values(arguments)

#number of arguments and number of parameters should be same
def student(rollno,branch):
    print("My rollno and branch is",rollno,branch)
student(24,"cse")
student(17,"csm")
student(18,"civil")

#default parameters
def function(name="sai"):
    print("Hello",name)
function("neeraj")
function()

#making code clearer by using keyword arguments
def neeraj(mobile,price):
    print("I have a",mobile) 
    print("My", mobile + " price is",price)
neeraj(mobile="vivo phone",price=35000) 

#positional arguments will not use keys
def neeraj(mobile,price):
    print("I have a",mobile) 
    print("My", mobile + " price is",price)
neeraj("vivo phone",35000)

#mixing keywords and positional arguments
def neeraj(mobile,model,price):
    print("I have a",mobile) 
    print("My", mobile + model + " price is",price)
neeraj("vivo phone",model=" x300pro",price=35000)

#function can return values by using return statement
def neeraj(a,b):
    return a * b 
result = neeraj(5,6) 
print(result)

#returning the list by function
def neeraj():
    return ["name","rollno","branch"]
details = neeraj()
print(details[0])
print(details[1])
print(details[2])