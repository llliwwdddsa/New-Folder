import time
import test
import os

# def max(a, b):
#     if a > b:
#         return a
#     else:
#         return b

# print(max(1, 2))


# def changeme(my_list):
#     my_list.append([1, 2, 3, 4])
#     print(my_list)

# mylist = [1, 2, 3]
# changeme(mylist)
# print(mylist)


def func_add(a, b):
    return a + b

def decorator(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} execution time is {start - end} seconds.")
        return result
    return wrapper

decoratored = decorator(func_add)
decoratored(1, 2)


current_directory = os.getcwd()
print(current_directory)

# while True:
#     try:
#         x  = int(input())
#         break
#     except ValueError:
#         print("ni shu ru de bushi shuzi")


class dog() :
    def __init__(self,color):
        self.color = color
    
    def func(self, Color):
        self.color = Color
        

dog_1 = dog("blue")
dog_1.name = 1
print(dog_1.color)
print(dog_1.name)

dog_2 = dog("white")
print(dog_2.color)
dog_2 = dog("black")
print(dog_2.color)
