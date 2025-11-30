class A:
    def quack(self):
        print("Quack by A")

class B:
    def quack(self):
        print("Quack by B")

def make_it_quack(obj):
    obj.quack()

make_it_quack(A())