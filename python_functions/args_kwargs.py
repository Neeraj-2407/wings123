#program using *args
def print_numbers(*args):
    for num in args:
        print(num)

print_numbers(10, 20, 30, 40, 50)

#calculating the sum of any number of values using *args
def my_function(*numbers):
  total = 0
  for num in numbers:
    total += num
  return total

print(my_function(1, 2, 3))
print(my_function(10, 20, 30, 40))
print(my_function(5))

#program using **kwargs
def student_info(**student_detail):
  for key , value in student_detail.items():
    print(key, ":" , value)
student_info(name =" neeraj",rollno = 6618, branch="csm")

#combining both *args and **kwargs
def student_info(title,*args,**kwargs):
  print("Title:" ,title)
  print("positional arguments:",args)
  print("keyword arguments:",kwargs)
student_info("user info","neeraj","prem",age=22,city="mbnr")  

#unpacking argument
def my_function(a, b, c):
  return (a * b)+ c

numbers = [1, 2, 3]
result = my_function(*numbers) # * is used to unpack the list
print(result)