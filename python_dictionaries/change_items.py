#updating the value of a particular key
a = {
    "name" : "neeraj",
    "roll no":6618,
    "year":4
}
a["year"]=3
print(a)

#we can update multiple keys by using update()
a = {
    "name": "neeraj",
    "roll no" : 6618,
    "year" : 4
}
a.update({"roll no":6617 , "year":3})
print(a)
