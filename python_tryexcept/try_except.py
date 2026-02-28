# try:
#   print(x)
# except:
#   print("An exception occurred")

#many exceptions
# try:
#   print(x)
# except NameError:
#   print("Variable x is not defined")
# except:
#   print("Something else went wrong")
 
#using else keyword to define a block
try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong") 

#the finally block executes no matter wheather the try block generates an error or not
try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")  

#Raise an error and stop the program if x is lower than 0:
x = -1

if x < 0:
  raise Exception("Sorry, no numbers below zero")