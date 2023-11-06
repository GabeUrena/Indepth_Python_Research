class Mammal:
    def walk(self):
        print("Walk")
    
        
class Dog(Mammal):
   def bark(self):
       print("Bark")
    

class Cat(Mammal):
    def meow(self):
        print("meow")

    
class Human(Mammal):
    pass # pass tells python to skip over this empty class


dog1 = Dog()
dog1.walk()
cat1 = Cat()
cat1.meow()
print("Done")
