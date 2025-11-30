class A:

    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    def __add__(self,other):
        return A(self.x+other.x,self.y+other.y)

a1 = A(3,4)
a2 = A(5,4)
a3 = a1+a2
print(a3.x," ",a3.y)


class B:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    def __eq__(self,other):
        return self.x == other.x and self.y == other.y

b1 = B(3,4)
b2 = B(3,5)
print(b1==b2)