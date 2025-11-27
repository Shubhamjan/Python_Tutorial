class Dog:
    species = 'Canien'

    def __init__(self,name,age):
        self.name = name
        self.age = age
    

d = Dog("shubham",23)
f = Dog("Lokesh",89)

# print(d.name)
# print(d.age)
# print(f.age)
Dog.species = "kutta"
print("secies for d",d.species)
print("secies for f",f.species)