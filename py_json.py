#  JSON is commonly used with data APIS. Here we can parse JSON into a Python dictionary
import json

# Sample JSON
userJSON = '{"first_name": "Manuel", "last_name":"Figueiredo", "age": 30}'

#Parse to dict
user = json.loads(userJSON)

print(user)
# Getting the first name
print(user['first_name'])

car = {'make': 'Ford', 'model':'Raptor','year':2018}

carJSON = json.dumps(car)
print(carJSON)
