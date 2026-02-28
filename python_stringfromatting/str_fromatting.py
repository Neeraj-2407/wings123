#f-strings is a feature to embed expressions directly into a string
txt = f"Good Morning"
print(txt)

#formatting the values in f-string by using placeholder{}
price = 27000
txt = f"The car price is {price} dollars"
print(txt)

#including a modifier by using (:)
price = 50550
txt = f"The car price is {price:.3f} dollars"
print(txt)

#performing operations in string
txt = f"The price is {300 * 159} dollars"
print(txt)

#performing if-else statement
price = 4700
txt = f"It is very {'Expensive' if price>8000 else 'Cheap'}"
print(txt)

#executing functions inside placeholders
animals = "dogs"
txt = f"I love {animals.upper()}"
print(txt)

#Creating a function that converts feet into meters
def myconverter(x):
  return x * 0.3048

txt = f"The plane is flying at a {myconverter(25000)} meter altitude"
print(txt)

#using comma as as thousand seperator
price = 27000
txt = f"The car price is {price:,} dollars"
print(txt)

#by using format method
price = 27000
txt = "The car price is {} dollars"
print(txt.format(price))

#format method for modifiers
price = 27000
txt = "The car price is {:.2f} dollars"
print(txt.format(price))

#index numbers
quantity = 4
itemno = 468
price = 67
myorder = "I want {0} pieces of item number {1} for {2:.2f} dollars."
print(myorder.format(quantity, itemno, price))

#named indexes
order = "I have a {dogname}, it is a {breedname}."
print(order.format(dogname = "coco", breedname = "golden doodle"))