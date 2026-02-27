x = range(12) #one argument
print(list(x))

x = range(3,15) #two argumnents
print(list(x))

x = range(3,16,3) # three arguments
print(list(x))

#by using for loops
for a in range(12):
    print(a)

#2
for a in range(1,32,5):
    print(a)

#using lists to display ranges
print(list(range(8)))
print(list(range(3, 9)))
print(list(range(5, 100, 9)))   

#slicing ranges
r = range(17)
print(r[6])
print(r[:8])
print(r[3:])

#support membership testing with the "in" operator.
r = range(3, 98, 9)
print(list(r))
print(78 in r)
print(66 in r)

#prints length of the list using len
r = range(3, 98, 9)
print(list(r))
print(len(r))
