# String in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string methods

name = 'Manuel Figueiredo'
age = 32

#Concatenate
# print('Hello, my name is: ' +name + 'and I am ' +str(age))

# String Formatting


#Arguments by position
#print('My name is {name} and I am {age}'.format(name=name, age=age))


#F-Strings (3.6+)
#print(f'Hello, my name is {name} and I am {age}')

# String methods
s = 'hello World'

#Capitalize string. converte a primeira letra em maiuscula
print(s.capitalize())

#Make all uppercase
print(s.upper())

# Make all lower
print(s.lower())

# Swap case
print(s.swapcase())

# Get length
print(len(s))

#Replace
print(s.replace('World', 'everyone'))

# Count
sub = 'h'
print(s.count(sub))

# Starts with
print(s.startswith('hello'))

# Ends with
print(s.endswith('d'))

# Split into a list
print(s.split())

# Find position
print(s.find('r'))

# Is all alphanumeric
print(s.isalnum())

# Is all alphabethic
print(s.isalpha())

# Is all numeric
print(s.isnumeric())


