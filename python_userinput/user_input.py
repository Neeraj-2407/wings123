# #user input
print("Enter your name:")
name = input()
print(f"Hi {name}")

# #using input()as a message
name = input("Enter your name:")
print(f"Hi {name}")

# #using multiple inputs
name = input("Enter your name:")
print(f"Hello {name}")
fav1 = input("What is your favorite car? ")
fav2 = input("What is your favorite color? ")
fav3 = input("What is your favorite number? ")
print(f"Do you want a {fav2} {fav1} with {fav3} wheel driving?")

# #converting input into a number by float()
import math 
a = input("Enter a number:")
b = math.sqrt(float(a))
print(f"The square root of {a} is {b}")

#validating the input
y = True
while y == True:
  x = input("Enter a number:")
  try:
    x = float(x);
    y = False
  except:
    print("Wrong input, please try again.")

print("Thank you!")