# Operators

# falsy: 0, 0.0, 0j, None
# list: []
# set: set()
# dict: {}
# tuple: ()
# '' = "" - empty string

# so sanh ky tu = ASCII
    
# +, -, *, /, //, %
print(1 + 2)
print(1 - 2)
print(3 * 2)
print(3 / 2)  # float 1.5
print(3 // 2)  # int 1
print(3 % 2)  # so du 1

# >, <, >=, <=, ==, != (bool)

print('-----------------------')

print(3 > 2)  # True
print('a' != 'a')  # False

print('-----------------------')

# and or not (and False phai or True trai)

print(True and True)  # True
print(True and False)  # False
print(False and False)  # False
print(False and True)  # False

print('-----------------------')

print(True or True)  # True
print(True or False)  # True
print(False or False)  # False
print(False or True)  # True


print('-----------------------')

print(not True)  # False
print(not False)  # True

print('-----------------------')

print(0 or 2)  # 2
print(0 and 1)  # 0

print('-----------------------')

# +=, -=, *=, /=, //=, %=, **=

x = 5

x += 5  # 10 (aka x = x + 5)

x -= 9  # 1 (aka x = x - 9)

# print('-----------------------')

# str(variables), f-strings and .format()

age = 15

print("I am " + str(age))

print(f"I am {age}")

print("I am {}".format(age))

# .upper(), .captialize(), .lower(), .title(), .split()

s = 'hello'
uppercase = s.upper()
print(uppercase)  # HELLO

capitalize = s.capitalize()
print(capitalize)  # Hello

lowercase = s.lower()
print(lowercase)  # hello

s2 = 'hello world'
title_string = s2.title()
print(title_string)  # Hello World

lst = s2.split()  # tach thanh list
print(lst)  # ['Hello', 'World']
