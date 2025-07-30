class Animal:
    def speak(self):
        print("Animal makes a sound.")

class Dog(Animal):
    def speak(self):
        print("Dog barks.")

class Cat(Animal):
    def speak(self):
        print("Cat meows.")

class Pet(Dog, Cat):
    def __init__(self, name):
       super().__init__()
       self.name = name
       print(f"Pet {self.name} created.")

# Example usage
if __name__ == "__main__":
    my_pet = Pet("Buddy")
    my_pet.speak()
    print(f"MRO of Pet: {Pet.__mro__}")
