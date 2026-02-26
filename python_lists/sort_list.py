names = ["neeraj","sai","rohit","prem","raghav","vamshi"] #sorting as per alphabets
names.sort()
print(names)

x = [23,84,12,36,100] #ascending order
x.sort()
print(x)

x = [23,84,12,36,100] #descending order we use reverse=True
x.sort(reverse=True)
print(x)

def myfunc(n):  #sorting as per nearest number to 35 
  return abs(n - 35)

x = [100, 50, 65, 82, 23]
x.sort(key = myfunc) #we use key=myfunc
print(x)