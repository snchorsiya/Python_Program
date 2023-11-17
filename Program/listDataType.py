# 3. Python List Data Type
# The list is a versatile data type exclusive in Python.

a = [1, 2, 3, 4, 5, 6, 1]
print(a)
print(a[::-1])
a.insert(3, "Sheetal")
print(a)
a.append("End")
print(a)
print(a[-1])

a[2] = "Chorsiya"
print(a)

del a[0]
print(a)

b = ["hey", "how", "are", "you", "?"]
print(b)

c = ["hey", "you", 1, 2, 3, 4, 5, "go"]
print(c)

print(c[4])

squares = [x**2 for x in range(10)]
print(squares)

even_squares = [x**2 for x in range(10) if x % 2 == 0]
print(even_squares)

fruits = ["apple", "banana", "mango", "orange"]

# Without enumerate
# for i in range(len(fruits)):
#     print(f"Index: {i}, fruit: {fruits[i]}")

# With enumerate

for i, fruit in enumerate(fruits):
    print(f"Index:{i}, fruit:{fruit}")

for i, fruit in enumerate(fruits, start=1):
    print(f"Index: {i}, fruit: {fruit}")