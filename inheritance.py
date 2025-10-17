# 1. Parent/Base Class
class Animal:
    def __init__(self, name):
        self.name = name
        
    def speak(self):
        # Default behavior (will be overridden)
        return f"{self.name} makes a sound."

# 2. Child/Derived Class (inherits from Animal)
class Dog(Animal):
    def __init__(self, name, breed):
        # Call the parent's constructor to initialize 'name'
        super().__init__(name) 
        self.breed = breed
        
    # Method Overriding: Changing the parent's method for the child
    def speak(self):
        return f"{self.name} the {self.breed} says Woof!"
        
    # New method unique to the Child
    def fetch(self):
        return f"{self.name} is fetching the ball."

# Usage
my_dog = Dog("Buddy", "Golden Retriever")

print(my_dog.speak()) # Output: Buddy the Golden Retriever says Woof! (Overridden method)
print(my_dog.fetch()) # Output: Buddy is fetching the ball. (New method)
print(my_dog.name)   # Output: Buddy (Inherited attribute)