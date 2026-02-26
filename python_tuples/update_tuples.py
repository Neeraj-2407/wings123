a = ("Neeraj","sai","vamshi","teja")
b = list(a)
b[2] = "prem"
a = tuple(b)
print(a)

a = ("Neeraj","sai","vamshi","teja") #add an item using append
b = list(a)
b.append("nipun")
a = tuple(b)
print(a)

x = ("neeraj","sai","prem") #adding tuple to tuple
y = ("saikiran",)
x += y
print(x)

x = ("pen","pencil","book")
y = list(x)
y.remove("book")
x = tuple(y)
print (x)