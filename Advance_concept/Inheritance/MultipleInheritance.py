class Dog:
    def __init__(self,mark):
        self.mark = mark
        
    
    def show(self):
        # super().show()#for calling the parent class method
        print(self.mark)
    
class Friend:
    def __init__(self,name):
        self.name = name
    def sound(self):
        print("Friend is "+self.name)

class Labrador(Dog,Friend):
    def __init__(self,type,mark,name):
        Dog.__init__(self,mark)
        Friend.__init__(self,name)
        self.type = type
    def show(self):
        Dog.show(self)
        print(self.type)

l = Labrador("om","rash","Tom")
l.sound()
l.show()


