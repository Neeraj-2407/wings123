#sum using lambda function(lamda has only one expression)
x = lambda a, b: a + b
print(x(5, 3))

#multiplying two variables using lambda
x = lambda a, b, c: (a * b)*c
print(x(5, 3, 4))

#function inside function using lambda
def func(n):
    return lambda a: a + n

add = func(15)

print(add(20))

#applying a function to every item using map()
numbers = [1, 3, 5, 7, 9]
tripled = list(map(lambda x: x * 2, numbers))
print(tripled)

#finding even numbers from the list by filter()
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)

#doing custon sorting by using sorting()
students = [("neeraj", 22), ("prem", 23), ("vishal", 30)]
sorted_students = sorted(students, key=lambda x: x[1])
print(sorted_students)



