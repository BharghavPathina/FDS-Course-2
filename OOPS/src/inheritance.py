## Single Inheritance
class Base:
    ### CHaracteristics -- proprties and actions
    pass

class Child(Base):
    ### Child class inherits the parents  class behiaviours & states
    pass


## Multiple Inheritance
class A:
    pass

class B:
    pass

class C(A,B):
    pass


## Multi level Inheritance
class A:
    pass

class B(A):
    pass

class C(B):
    pass


## Hierachial Inheritance
class A:
    pass

class B(A):
    pass

class C(A):
    pass

## Hybrid Inheritance
class A:
    def __init__(self) -> None:
        self.a = "A"
        print("in A")
class B:
    def __init__(self) -> None:
        self.a = "B"
        print("in B")


class Test(A,B): ## Left to Right
    def __init__(self) -> None:
        super().__init__()
        print("in Test")



##MRO: METHODS RESOLUTION ORDER

obj = Test()
print(obj.a)