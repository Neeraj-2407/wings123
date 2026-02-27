import my_module

my_module.greet("Jonathan")

import my_module1
a = my_module1.student1["age"]
print(a)

#renaming the module using as
import my_module1 as ns
a = ns.student1["name"]
print(a)

#platform module
import platform
x = platform.system()
print(x)

#listing all the function names in a module by using dir() function
import platform
x = dir(platform)
print(x)

from my_module3 import student1
print(student1["country"])