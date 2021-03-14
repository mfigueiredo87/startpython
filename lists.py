# A list is a collection which is ordered and changeable. Allows duplicate members

#Create a list
numbers = [1, 2, 3, 4, 5]
fruits = ['Apples', 'Orange', 'Grapes', 'Pears']
#Use a constructor
#numbers2 = list((1, 2, 3, 4, 5))

#print(numbers, numbers2)

# Get a value
print(fruits[1])

#Get length
print(len(fruits))

# Append to list
fruits.append('mango')
print(fruits)

#Remo from list
fruits.remove('Grapes')

# Insert into position
fruits.insert(2,'Strawberries')
print(fruits)

# Change value
fruits[0] = 'Blueberries'
print(fruits)

#Remove into position with pop
fruits.pop(2)
print(fruits)

#Reverse list
fruits.reverse()
print(fruits)

#Sort list
fruits.sort()
print(fruits)

#Reverse sort
fruits.sort(reverse=True)
print(fruits)




