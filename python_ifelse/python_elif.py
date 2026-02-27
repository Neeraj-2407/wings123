#if if statement is not true then it will go to elif statement
a = 18
b = 18
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")

 #multiple elif statements
temperature = 15

if temperature >= 30:
  print("Very Hot")
elif temperature >= 20:
  print("Warm")
elif temperature >= 10:
  print("Cool")
elif temperature >= 0:
  print("Cold") 