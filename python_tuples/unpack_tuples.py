fruits = ("apple","banana","cherry") #unpacking a tuple
(grapes,watermelon,kiwi)= fruits
print (grapes)
print(watermelon)
print(kiwi)

names =("neeraj","prem","nipun","sai","satya","rohit") #using asterisk *
(vishal,jayanth,varun,*bhanu) = names
print(vishal)
print(jayanth)
print(varun)
print(bhanu)

names =("neeraj","prem","nipun","sai","satya","rohit") #giving * for middle variable
(vishal,*jayanth,bhanu) = names
print(vishal)
print(jayanth)
print(bhanu)