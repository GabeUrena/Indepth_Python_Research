class Person:
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height
        
        
    def speak(self):
        print(f'Hello, my name is {self.name} and I am {self.age} years old. I am {self.height} feet tall.')
        
        
class Student(Person):
    def __init__(self, name, age, height, major):
        super().__init__(name, age, height)
        self.major = major
        
    def speak(self):
        print(f'Hello, my name is {self.name} and I am a {self.major} major.')
        
        
person = Person('Gabriel', 22, 5.4)
student = Student('Shylin', 24, 5.5, 'Communication Design')

person.speak()
student.speak()
