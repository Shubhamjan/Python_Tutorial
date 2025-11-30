class Demo:
    def addition(self,*args):
        return sum(args)

print(Demo().addition(3,4,5))

print(Demo().addition(3,4,54.5,3))

print(Demo().addition(3,4,5,1,2,2))

