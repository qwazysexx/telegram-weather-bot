class Animal:
    def sound(self):
        return "Some sound"

class Dog(Animal):
    # Re-validation of the sound method
    def sound(self):
        return "Bark"

class Cat(Animal):
    # Re-validation of the sound method
    def sound(self):
        return "Meow"

# Example of use
dog = Dog()
cat = Cat()

print(dog.sound())  
print(cat.sound()) 
