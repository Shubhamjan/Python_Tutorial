from abc import ABC, abstractmethod
class A(ABC):

    @abstractmethod
    def sound(self):
        print("dog barks")
    
    def play(self):
        print("Human play")

class B(A):
    
    def sound(self):
        print("B barks")
    
    def play(self):
        print("B plays")

b = B()
b.sound()
b.play()
