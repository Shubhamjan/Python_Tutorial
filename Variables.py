#dynaming typing
# Same variable can hold different type of values

a = 23
a = "String"
# print(a)

#assigning same values for multiple variables

a=b=c=100
# print(a)

#assigning different values
x,y,z = 2,"Shubham",2.5
# print(x)
# print(y)
# print(type(z))
# print(type('a'))
# print(type(str(2)))


# Object Reference
x =5
#when x=5 then python create the object an object to represent the value 5
#and makes x references this object
y=x
#This statement creates y and references the same object as x not x itself. This is called 'Shared reference"

# if we assign the y="Computer" then python create the object for computer and update
# y to reference it.
#Python variables hold references to object no the actual objects themselves
#Reassinging the variables doesnot affect the other variables referencing the same object unless explicitly updated.

x= 10
# del x it just delete the references not object. Objects deleted automatically by garbage collection
print(x)
