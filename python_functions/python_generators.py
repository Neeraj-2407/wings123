# # def neeraj():
# #     for i in range(5):
# #         yield i

# # b = neeraj()

# # print(next(b)) 
# # print(next(b))  
# # print(next(b))  

# #looping through generator
# def neeraj(n):
#     for i in range(n):
#         yield i
# for i in neeraj(7):
#     print(i)

# #yield keyword
# def count_up_to(n):
#   count = 1
#   while count <= n:
#     yield count
#     count += 1

# for num in count_up_to(7):
#   print(num)   

# #using next()function in generators
# def simple_gen():
#   yield "neeraj"
#   yield "prem"
#   yield "sai"

# a = simple_gen()
# print(next(a))
# print(next(a))
# print(next(a))

# #generator expression
# list1 = [x * x for x in range(7)]
# print(list1)
# gen_exp = (x * x for x in range(7))
# print(gen_exp)
# print(list(gen_exp))

# #fibinocci sequence using generator
# def fibonacci():
#   a, b = 0, 1 #initializing first two fibinocci numbers
#   while True:
#     yield a
#     a, b = b, a + b
# a = fibonacci()
# for _ in range(30):
#   print(next(a))

#sending a value to generator by using send()
def echo_generator():
 while True:
    received = yield
    print("Received:", received)

gen = echo_generator()
next(gen)  # Prime the generator
gen.send("Hello")
gen.send("World")  

#closing the generator by using close()
def my_gen():
  try:
    yield 1
    yield 2
    yield 3
  finally:
    print("Generator closed")

a = my_gen()
print(next(a))
print(next(a))
a.close()