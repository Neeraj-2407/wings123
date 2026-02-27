#when if statement has no content we use pass statement to avoid error 
a = 33
b = 200

if b > a:
  pass

#pass in development
age = 16

if age < 18:
  pass 
else:
  print("Access granted")

 #using pass statement with multiple conditions
value = 20

if value < 0:
  print("Negative value")
elif value == 0:
  pass # Zero case - no action needed
else:
  print("Positive value") 