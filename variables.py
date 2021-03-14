# a variable is a container for a value, wich can be of various types

'''
This is a multiline comment or docstring (used to define a functions purpose)
can be single or double quotes'''

"""
VARIABLES RULES:
    - Variable names are case sensitive (name and NAME are different variables)
    - Must start with a letter or an underscore
    - Can have numbers but can not start with one
"""

x = 1           #int
y = 2.5         #float
name = 'Manuel' #str
is_cool = True  #bool

#Multiple assignment
x, y, name, is_cool = (1, 2.5, 'Manuel', True)

#Basic math
a = x + y

# Casting/ trocando os tipos de dados das variaveis
x = str(x)
y = int(y)
z = float(y)

#para verificar o tipo da variavel
print(type(z),z,y,x)
print('Hello', name,a)
