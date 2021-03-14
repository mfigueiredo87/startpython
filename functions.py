# A function is a block of code wich only runs when it is called. In Python, we, we do not use curly brackets, we use indentation with tabs or spaces

# Create function
def sayHello(name):
    print(f'Hello {name}')
sayHello('Manuel Figueiredo')

#Outra forma
def nameFunc(name='Manuel Figueiredo'):
    print(f'Bem vindo: {name}')
nameFunc()

#Return values
def getSum(num1, num2):
    total = num1 + num2
    return total
#print(getSum(5,11))
num = getSum(4,7)
print(num)


# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression. Very similar to JS arrow function

getSum = lambda num1, num2 : num1 + num2

print(getSum(10,3))
