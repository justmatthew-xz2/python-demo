# List

#          0  1   2   3  4
#         -5 -4  -3  -2  -1
numbers = [1, 2, 3.5, 4, 1]
print(type(numbers))
print(numbers)

print('-------------------------------------')

print(numbers[0])  # 1
print(numbers[-1])  # aka print(numbers[5]) -> 1
print(numbers[-3])  # aka print(numbers[2]) -> 3.5

print('-------------------------------------')

# .append(), .remove(), .pop(), .extend(), .count(), .clear()

# no need ( a = numbers.append(100) ) - them gia tri vao cuoi list
numbers.append(100)
print(numbers)

print('-------------------------------------')

numbers.remove(1)  # [2, 3.5, 4, 1, 100] - xoa gia tri cu the k theo thu tu
print(numbers)

# numbers.remove(-1000) - ValueError: list.remove(x): x not in list

print('-------------------------------------')

last_value = numbers.pop()  # aka ( numbers.pop() ) - xoa gia tri cuoi list
print(last_value)  # 100
print(numbers)  # [2, 3.5, 4, 1]

print('-------------------------------------')

numbers.extend([2.5, 1000, 100, 125])  # them vao cuoi 1 list khac
print(numbers)  # [2, 3.5, 4, 1, 2.5, 1000, 100, 125]

print('-------------------------------------')

# numbers[vi tri] = gia tri

numbers[0] = 75  # thay gia tri o vi tri 0 -> 75
print(numbers)  # [75, 3.5, 4, 1, 2.5, 1000, 100, 125]

print('-------------------------------------')

# 1 - dem so phan tu co gia tri tuong ung trong ngoac
amount = numbers.count(1000)
print(amount)

print('-------------------------------------')

numbers.clear()  # clear list numbers -> []
print(numbers)

print('-------------------------------------')

# len(), .insert(), .reverse(), .index(), .sort()

numbers2 = [1, 2, 4, 7, 9]

# len()

items_amount = len(numbers2)  # 0 - tra ve so phan tu co trong list
print(items_amount)

print('-------------------------------------')

# .insert()

# [1, 1000, 2, 4, 7, 9] - insert(thu tu, gia tri muon dat vao vi tri do)
numbers2.insert(1, 1000)
print(numbers2)

numbers2.insert(1000, 1000)  # [1, 1000, 2, 4, 7, 9, 1000]
print(numbers2)

numbers2.insert(-1000, 1000)  # [1000, 1, 1000, 2, 4, 7, 9]
print(numbers2)

print('-------------------------------------')

# .index()

index_of_2 = numbers2.index(2)  # 3 - .index(gia tri can tim vi tri)
print(index_of_2)

# index_of_3000 = numbers2.index(3000)
# print(index_of_3000)    ValueError: 3000 is not in list

print('-------------------------------------')

# .reverse()

numbers2.reverse()  # lat nguoc list
print(numbers2)

print('-------------------------------------')

# .sort()

# [1, 2, 4, 7, 9, 1000, 1000, 1000] - sap xep theo thu tu tang dan
numbers2.sort()
print(numbers2)

# [1000, 1000, 1000, 9, 7, 4, 2, 1] - sap xep theo thu tu giam dan
numbers2.sort(reverse=True)
print(numbers2)

# del

del numbers2[2]  # [1000, 1000, 9, 7, 4, 2, 1] - xoa phan tu o vi tri 2
print(numbers2)

print('-------------------------------------')

# max(), min() (cung la so)
numbers3 = [12, 36, 56, -100, 67]

max_value = max(numbers3)  # tim so lon nhat trong list
print(max_value)

min_value = min(numbers3)  # tim so nho nhat trong list
print(min_value)

print('-------------------------------------')
