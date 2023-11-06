"""
Person
   string name
   string birthday
   char sex
   
   - talk()
    
    
"""
    
class Person:
    def __init__(self,name, birthday, sex):
        self.name = name
        self.birthday = birthday
        self.sex = sex
        
    def talk(self):
        print(f"Hello I'm {self.name} and I am talking.")
        
John = Person("John","1st January 2005", 'M')
        
print(John.birthday)
John.talk()