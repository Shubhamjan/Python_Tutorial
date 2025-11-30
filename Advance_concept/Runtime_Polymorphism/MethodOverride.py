class Animal:
    def bark(self):
        print("Animal is bark")

class Dog(Animal):
    def bark(self):
        super().bark()
        print("Dog is barking")

Dog().bark()