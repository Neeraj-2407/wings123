x = ["neeraj","sai","rohit"] #joining of list
y = [18,44,29]

z = x + y
print(z)

a = ["neeraj","sai","rohit"] #using append
b = [18,44,29]

for x in b:
  a.append(x)

print(a)

a = ["neeraj","sai","rohit"] #using extend()
b = [18,44,29]

a.extend(b)
print(a)