import math
a = float(input("Nhập cạnh a > "))
b = float(input("Nhập cạnh b > "))
c = float(input("Nhập cạnh c > "))
p = (a+b+c)/2

print(f'''
Chu vi: {a+b+c}
Diện tích: {round(math.sqrt(p*(p-a)*(p-b)*(p-c)), 3)}
''')
