#remove an item using pop()
x = {
   "name" : "neeraj",
   "roll no" : 6618,
   "branch" : "cse"
}
x.pop("branch")

print(x)

#popitem() will delete the last item  
x = {
   "name" : "neeraj",
   "roll no" : 6618,
   "branch" : "cse"
}
x.popitem()
print(x)

#making dictionary empty by using clear()
x = {
   "name" : "neeraj",
   "roll no" : 6618,
   "branch" : "cse"
}
x.clear()

print(x)

#del() removes complete dictionary
x = {
   "name" : "neeraj",
   "roll no" : 6618,
   "branch" : "cse"
}
del x
print(x)