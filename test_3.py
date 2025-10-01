import random
import time

# print("now, let us play a game")
# print("I will randomly make a num, you try to guess it")
# num = random.randint(1, 100)
# b = int(input("please input your num:"))

# count = 0
# while num != b:
#     if num > b :
#         print("you guessed too low")
#     else :
#         print("you guessed too high")
#     count += 1
#     b = int(input("please input again:"))
# print("congratulation you guessed it right")
# print(f"it was input a total of {count}")


a = 'a' 
print(a)

for i in range(101):
    bar = '[' + '=' * (i // 2) + ' ' * (50 - i//2) + ']'
    print(f"\r{bar} {i:3}%", end=' ', flush = True)
    time.sleep(0.05)
print()

my_list = [1, 2, 3]
print(max(my_list))

my_dict = {1:2, 2:3, 3:4}
for i in my_dict:
    print(my_dict[i])

a, b = 0, 1
while b < 10:
    print(b)
    a, b = b, a + b