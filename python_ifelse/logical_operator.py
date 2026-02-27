#and operator returns true if both statements are true
a = 238
b = 98
c = 467
if a > b and c > a:
  print("Both conditions are True")

#or operator returns true if one of the statement is true
a = 200
b = 33
c = 500
if a > b or a > c:
  print(" one of the condition is True")

#NOT operator returns reverse results
a = 33
b = 200
if not a > b:
  print("a is NOT greater than b")  

#combining multiple operators
age = 25
is_student = False
has_discount_code = True

if (age < 18 or age > 65) and not is_student or has_discount_code:
  print("Discount applies!")