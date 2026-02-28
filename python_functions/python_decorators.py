#basic decorator
def my_decorator(func):
    def wrapper():
        print("hii")
        func()
        print("bye")
    return wrapper


@my_decorator
def say_hello():
    print("Hello!")

say_hello()

#using @changecase for two decorators
def changecase(func):
  def myinner():
    return func().upper()
  return myinner

@changecase
def myfunction():
  return "Hello Sally"

@changecase
def otherfunction():
  return "I am speed!"

print(myfunction())
print(otherfunction())

#decorators using arguments
def changecase(n):
  def changecase(func):
    def myinner():
      if n == 1:
        a = func().lower()
      else:
        a = func().upper()
      return a
    return myinner
  return changecase

@changecase(1)
def myfunction():
  return "Hello neeraj"

print(myfunction())

#using multiple decortors
def changecase(func):
  def myinner():
    return func().lower()
  return myinner

def addgreeting(func):
  def myinner():
    return "Hello " + func() + " Have a good day!"
  return myinner

@changecase
@addgreeting
def myfunction():
  return "neeraj"

print(myfunction())