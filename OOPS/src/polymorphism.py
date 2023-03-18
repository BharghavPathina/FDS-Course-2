class Bird:
    def __init__(self,name) -> None:
        self.name = name
    def describe(self):
        print(f"I am a Bird, my name is {self.name}")

class FlyighingBird(Bird):
    def __init__(self, name) -> None:
        super().__init__(name)
    def describe(self):
        print(f"I am flyighing bird, my name is {self.name}")

def main():
    bird = Bird("Parrot")
    bird.describe()

    bird2 = FlyighingBird("Crow")
    bird2.describe()

if __name__=="__main__":
    main()