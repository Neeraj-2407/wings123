#joining sets using union() function,here it creates new set
x1 = {"a", "b", "c"}
x2 = {1, 2, 3}
x3= x1.union(x2)
print(x3)

# we can use | instead of union 
x1 = {"a", "b", "c"}
x2 = {1, 2, 3}
x3= x1 | x2
print(x3)

#we can use union funtion to join list and sets also
x1 = {"a", "b", "c"}
x2 = (1, 2, 3)
x3= x1.union(x2)
print(x3)

#union is similar to update but here it modifies the set
x1 = {"a", "b", "c"}
x2 = {1, 2, 3}
x1.update(x2)
print(x1)

#intersetion,it returns only the common element 
x1 = {"a", "b", "c"}
x2 = {"c","d","a"}
x3= x1.intersection(x2)
print(x3)

#difference, it removes the common element and returns remaining elements in first set
x1 = {"a", "b", "c"}
x2 = {"c","d","a"}
x3= x1.difference(x2)
print(x3)

#instead of difference function we can use "-"
x1 = {"a", "b", "c"}
x2 = {"c","d","a"}
x3= x2-x1
print(x3)