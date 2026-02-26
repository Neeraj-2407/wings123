#adding an extra key value pair
x = {
   "name" : "neeraj",
   "roll no" : 6618,
   "branch" : "cse"
}
x["year"]= 4
print(x)

#updating a key using update()
x = {
   "name" : "neeraj",
   "roll no" : 6618,
   "branch" : "cse"
}
x.update({"clg": "aurora"})
print(x)