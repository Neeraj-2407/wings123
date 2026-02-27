students = ["neeraj","prem","sai","sanjay"]
print(students)

#accessing the elements in an array
students = ["neeraj","prem","sai","sanjay"]
a = students[2]
print(a)

#lenght of elements in an array
students = ["neeraj","prem","sai","sanjay"]
a = len(students)
print(a)

#looping through the elements in an array
students = ["neeraj","prem","sai","sanjay"]
for a in students:
    print(a)

#adding an item in an array
students = ["neeraj","prem","sai","sanjay"]
students.append("jithu")
print(students)

#removing an element in an array(we can use pop()also)
students = ["neeraj","prem","sai","sanjay"]
students.remove("sai")
print(students)

#pop()
students = ["neeraj","prem","sai","sanjay"]
students.pop(1)
print(students)