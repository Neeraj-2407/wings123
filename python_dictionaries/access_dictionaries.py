#it stores value in a and then it will print
# x = {
#     "name"    : "neeraj",
#     "roll no" :  6618,
#     "branch"  : "cse"
# }
# a = x["branch"]
# print(a)

#we can print the value by using get()
# x = {
#     "name"    : "neeraj",
#     "roll no" :  6618,
#     "branch"  : "cse"
# }
# a = x.get("name")
# print(a)

#by using keys() we can print values
# x = {
#     "name"    : "neeraj",
#     "roll no" :  6618,
#     "branch"  : "cse"
# }
# a = x.keys()
# print(a)

#by using values() we can print keys
# x = {
#     "name"    : "neeraj",
#     "roll no" :  6618,
#     "branch"  : "cse"
# }
# a = x.values()
# print(a)

#adding an extra key value pair and printing keys
# detail = {
#     "name"    : "neeraj",
#     "roll no" :  6618,
#     "branch"  : "cse"
# }
# a = detail.keys()
# print(a) #before the change
# detail["year"]= 4
# print(a) #after the change

#adding an extra key value pair and printing values
# detail = {
#     "name"    : "neeraj",
#     "roll no" :  6618,
#     "branch"  : "cse"
# }
# a = detail.values()
# print(a) #before the change
# detail["year"]= 4
# print(a) #after the change

#printing total items by using items()
# x = {
#     "name"    : "neeraj",
#     "roll no" :  6618,
#     "branch"  : "cse"
# }
# a = x.items()
# print(a)

#checking if key exist or not by using if statement
x = {
    "name" : "neeraj",
    "roll no" : 6618,
    "branch"  : "cse"
    }
if "year" in x:
    print("Yes,'year' is a key in x dictionary")
else:
    print("No,'year'is not a key in x dictionary")