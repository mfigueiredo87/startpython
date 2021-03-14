# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.

#Create a dictionary
person = {
    'first_name':'Manuel',
    'last_name': 'Figueiredo',
    'age':30
    }

#print(person, type(person))

# Use constructor
#person2 = dict(first_name='Adameire', last_name='Ricardo')

# Get Value
print(person['first_name'])
print(person.get('last_name'))

# Add key/value
person['phone']='999-999-999'
print(person)

# Get dict keys
print(person.keys())

# Get dict items
print(person.items())

# Copy dict
person2 = person.copy()
person2['city']='Huila'
#print(person2)

#Remove item
del(person['age'])
person.pop('phone')

#Clear
person.clear()

# Get length
print(len(person2))
      
# List of dict
people = [
    {'name': 'Vicky', 'age':30},
    {'name': 'Carlos','age':32}
]
# Knowing the specific field
print(people[1]['name'])
