
class Animal: #parent class
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass


class Dog(Animal):# Child class 
    def speak(self):
        return f"{self.name} says Woof!"


dog = Dog("Buddy") 


print(dog.speak())  # Output


