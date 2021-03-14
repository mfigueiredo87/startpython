# A class is like a blueprint for creating objects. An object has properties and methods (functions) associated with it. Almost everything in Python in an object

# Create class
class User:
     
#Construtor (is  basically run when instancied an object in a class. Self is the same to this in other languages
    
    def __init__(self, name, email, age):
        self.name = name
        self.email= email
        self.age = age

# creating a method
    def greeting(self):
        return f'My name is: {self.name} and I am {self.age}'

#method add 1 to the age
    def has_birthday(self):
        self.age += 1

# extended a class
class Customer(User):
#construtor
    def __init__(self, name, email, age):
        self.name = name
        self.email= email
        self.age = age
        self.balance = 0

# methods customer
    def set_balance(self, balance):
        self.balance = balance
        
# creating a method
    def greeting(self):
        return f'My name is: {self.name} and I am {self.age} and my balance is {self.balance}'
    
# Init user object
fig = User('Manuel Figueiredo', 'figtch@gmail.com',32)

# Init customer object
vicky = Customer('Vicky Ricardo','vicky@gmail.com',30)
vicky.set_balance(500)
print(vicky.greeting())

fig.has_birthday()     
print(fig.greeting())
