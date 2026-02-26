#create and print a dictionary
x = {
    "name"    : "neeraj",
    "roll no" :  6618,
    "branch"  : "cse"
}
print(x)

#print the value by key name
x = {
    "name"    : "neeraj",
    "roll no" :  6618,
    "branch"  : "cse"
}
print(x["roll no"])

#it will not allow duplicates
x = {
    "name"    : "neeraj",
    "roll no" :  6618,
    "branch"  : "cse",
    "name"    : "neeraj"
}
print(x)

#len() will find length of dictionary
x = {
    "name"    : "neeraj",
    "roll no" :  6618,
    "branch"  : "cse"
}
print(len(x))

#type() finds which form it is
x = {
    "name"    : "neeraj",
    "roll no" :  6618,
    "branch"  : "cse"
}
print(type(x))

# making dictionary by using dict() constructor 
a = dict(name = "neeraj" , rollno = 6618 , branch = "cse")
print(a)

