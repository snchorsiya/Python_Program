# Python Tuple

# The tuple is another data type which is a sequence of data similar to a list. But it is immutable. That means data
# in a tuple is write-protected. Data in a tuple is written using parenthesis and commas.

a = (1, 2, 3, 1, 5)
print(a)

b = (1, 2, 3, "Sheetal", 4)
print(b[2])


# Python Dictionary

# Python Dictionary is an unordered sequence of data of key-value pair form. It is similar to the hash table type.
# Dictionaries are written within curly braces in the form key:value. It is very useful to retrieve data in an
# optimized way among a large amount of data.

dic = {"firstname": "Sheetal", "lastname": "Chorsiya", "age": 26}
print(dic)
print(dic["firstname"])
print(dic["age"])

dict = {}
dict["firstname"] = "Rishi"
dict["lastname"] = "patel"
dict["age"] = 38


print(dict)
