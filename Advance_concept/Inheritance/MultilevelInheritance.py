class Animal:

    def __init__(self,breed,name):
        self.breed = breed
        self.name = name

    def detail(self):
        print("the breed is ",self.breed," and name is ",self.name)
    
    def show(self):
        print("The breed is ",self.breed," and name is ",self.name)

class Dog(Animal):
    def __init__(self,mark,breed,name):
        super().__init__(breed,name)
        self.mark = mark
        
    
    def show(self):
        super().show()#for calling the parent class method
        print(self.mark)

class Labrador(Dog):
    def __init__(self,type,mark,breed,name):
        super().__init__(mark,breed,name)
        self.type = type
    def show(self):
        super(Dog,self).show()
        print(self.type)


# d1 = Dog("rash","Om","Lab")
d1 = Labrador("Abroad","rash","om", "Tom")
d1.show()

# super(Dog,d1).show()#for calling the parent class method
# d1.detail()


