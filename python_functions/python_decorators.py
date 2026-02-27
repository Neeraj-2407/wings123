#basic decorator
def my_decorator(func):
    def wrapper():
        print("hii")
        func()
        print("bye")
    return wrapper


@my_decorator
def say_hello():
    print("Hello!")

say_hello()