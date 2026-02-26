# remove an item
a = {"pen","pencil","scale","eraser"}
a.remove("eraser")
print(a)

# discard an item
a = {"pen","pencil","scale","eraser"}
a.discard("eraser")
print(a)

# removes any item by using pop()
x = {"pen","pencil","scale","eraser"}
a = x.pop()
print(a)
print(x)

# empties the set by using clear()
a = {"pen","pencil","scale","eraser"}
a.clear()
print(a)

#del function deletes the set so it shows error
a = {"pen","pencil","scale","eraser"}
del a
print(a)
