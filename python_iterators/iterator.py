#printing each value by returning an iterator 
a = ("apple", "banana", "cherry")
b = iter(a)

print(next(b))
print(next(b))
print(next(b))

#printing each letter in a word by returning an iterator
a = "neeraj"
b = iter(a)

print(next(b))
print(next(b))
print(next(b))
print(next(b))
print(next(b))
print(next(b))

#iterate the value of a tuple
a = ("apple", "banana", "cherry")
for x in a:
    print(x)

#iterate each letter in word by using for loop
a = "neeraj"
for x in a:
    print(x)