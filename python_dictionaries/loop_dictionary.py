#prints keys
x = {
    "name"    : "neeraj",
    "roll no" :  6618,
    "branch"  : "cse"
}
for a in x:
    print(a) 

#prints values
x = {
    "name"    : "neeraj",
    "roll no" :  6618,
    "branch"  : "cse"
}
for a in x:
    print(x[a])

#we can print values by value()also
x = {
    "name"    : "neeraj",
    "roll no" :  6618,
    "branch"  : "cse"
}
for a in x.values():  
     print(a)   

#we can print keys by keys() also   
x = {
    "name"    : "neeraj",
    "roll no" :  6618,
    "branch"  : "cse"
}
for a in x.keys():  
     print(a)     