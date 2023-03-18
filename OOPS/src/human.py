class Human: ## Capital Camel Case
    # Class Property
    count = 0
    __abc = None
    def __init__(self,name,color="grey"):
        ## Instance Properties
        self.__color = color
        self.name = name

    ### Instance Method
    def eat(self):
        print(f"{self.name} with color {self.__color}")

    @classmethod
    def increase(cls):
        cls.count = cls.count + 1

    ## Getters
    def get_color(self):
        return self.__color

    ## Setters
    def set_color(self,color):
        self.__color = color

    @staticmethod
    def abc():
        return "Static Method"

def main():
    print("Example Of OOPS")
    obj1 = Human("Sitaram","white") ### count = 0, color = white, name = Sitaram -- object state
    print(f"Object Details:{obj1.get_color()}")
    print(f"Name of the Object:{obj1.name}")
    print(f"Class Property Accessing from class:{Human.count}")
    print(f"Class Proprty accessed from obj {obj1.count}")
    obj1.increase()
    print(f"Object count in a class is {Human.count}")
    obj2 = Human("SaiKiran")
    obj2.increase() ### self, cls both will be passed automatically 
    print(f"Object count in a class is {Human.count}")
    Human.increase()
    print(f"Object count in a class is {Human.count}")
    # print(f"Accessing Instance method {Human.eat()}") cls will be passed automatically
    print(f"calling static method:{Human.__abc}")
    print(f"Calling static method using object: {obj1.abc()}")

if __name__ == "__main__":
    main()