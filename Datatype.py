import keyword

#The following are standard or built-in data types in Python:

# Numeric: int, float, complex
# Sequence Type: string, list, tuple
# Mapping Type: dict
# Boolean: bool
# Set Type: set, frozenset
# Binary Types: bytes, bytearray, memoryview

# printing all keywords at once using "kwlist()"
# print("The list of keywords are : ")
# print(keyword.kwlist)


#int 
# a = 10
# print(type(a))

# b = 10.5
# print(type(b))#float
# print(type(3+4j))#complex number

str = '''shubham'''
str = 'shubham'
# str = "shubham" #way to intialize string
# print(str[3])#access the string with index

# List Data Type
# Lists are similar to arrays found in other languages. 
# They are an ordered and mutable collection of items. 
# It is very flexible as items in a list do not need to be of the same type.
a =[] #empty list
a = [1,2,4]
a = ['shubham',2,3.4]
# print(a)
#In list accessing element from end like -1,-2
# print(a[-4])
# print(a[1])

# Tuple Data Type
# Tuple is an ordered collection of Python objects. 
# The only difference between a tuple and a list is that tuples are immutable. 
# Tuples cannot be modified after it is created
a = ("shubham",3,4.5)
# print(a[-1])
# print(a[0][2])

# Boolean dataype
# a = True
# print(type(a))
# print(type(False))

#Truth and falsy value
# if 10>12:
#     print("true")
# if not 10>12:
#     print("false")

# 4. Set Data Type
# In Python Data Types, 
# Set is an unordered collection of data types that is iterable, mutable, and has no duplicate elements. 
# The order of elements in a set is undefined though it may consist of various elements.
s = set([2,"shubham",5.6])
# for i in s:
#     print(i)

# Dictonary

d = {1:"Shubham",2:"Jangale"}
print(d.get(1))
print(d[2])
