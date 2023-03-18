class Base:
    _a = "Class Property -- Base"
    def __init__(self) -> None:
        self.b = "Instance Proprty -- Base"

    def show(self,className): ## public member instance method
        print(f"I am in {className} class")

    def describe_obj(self,className):
        self.show(className)
        print(f"Object Class Property:{self._a}\nObject Instance Property:{self.b}")


class Child(Base):
    c = "Class Proprty-- Child"
    def __init__(self) -> None:
        super().__init__()
        self.d = "Instance Property -- Child"


def main():
    obj = Base()
    obj.describe_obj("Base")

    child_obj = Child()
    
    """
    properties:(c,d,_a,b)
    mehods:(show,describe)
    """

    child_obj.describe_obj("Child")

if __name__ == "__main__":
    main()


