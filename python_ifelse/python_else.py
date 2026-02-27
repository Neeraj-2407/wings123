a = 55
b = 20
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

#we can write else without elif
a = 789
b = 459
if b > a:
  print("b is greater than a")
else:
  print("a is greater than b") 

#checking odd and even by if and else
number = 13
if number % 2 == 0:
  print("The number is even")
else:
  print("The number is odd")  

#complete if-elif-else
score = 77
if score >= 90:
  print("Grade: A")
elif score >= 80:
  print("Grade: B")
elif score >= 70:
  print("Grade: C")
else:
  print("Grade: D")  