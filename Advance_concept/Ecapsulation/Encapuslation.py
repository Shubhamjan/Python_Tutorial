class A:

    def __init__(self,name,type,age):
        self.name = name
        self._type = type #protected(accesible in subclass also)
        self.__age = age #private(only within class)

    def get_Age(self):
        return self.__age


print(A("Shubham","Top",24).get_Age())
print(A("ROHAN","TOP",45)._type)