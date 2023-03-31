# A class is like a blueprint for creating objects. An object has properties and methods(functions) associated with it. Almost everything in Python is an object

class User:
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
        print(f'\n created an User with name {self.name}, age {self.age}, and email {self.email}\n')
    
    def greeting(self):
        return f'Hello my name is {self.name}, I am {self.age} years of age.'
    
    def has_birthday(self):
        self.age += 1

class Customer(User):
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
        self.balance = 500
        
    def greeting(self):
        return f'\n Hello my name is {self.name}, I am {self.age} years of age, an I have {self.balance} in my account'
    
    

biswajit = User('Biswajit Rajaguru', 'br@gmail.com', 40)
janet = Customer('Jennifer', 'jennifer@gmail.com', 25)


print(janet.greeting())


