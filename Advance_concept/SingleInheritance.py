class Animal:

    def __init__(self,breed,name):
        self.breed = breed
        self.name = name

    def detail(self):
        print("the breed is ",self.breed," and name is ",self.name)

class Dog(Animal):
    def __init__(self,mark,name,breed):
        super().__init__(name,breed)
        self.mark = mark
        
    
    def show(self):
        print(self.mark)


d1 = Dog("rash","Om","Lab")
d1.show()
d1.detail()


