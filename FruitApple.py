#call child method from parent object
class Fruit:
    def __init__(self):
        pass
    def one_fruit(self):
        print("First Fruit")
class Apple(Fruit):
    def child_fruid(self):
        print("Child method")
        
f = Fruit()
#a = Apple()

f.__class__ = Apple
f.child_fruid()
