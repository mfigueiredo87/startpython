# A module is a basically a file containing a set of functions to include in your application. There are core python modules, modules you can install using the pip package manager (including Django) as well as custom modules

import datetime
from datetime import date
import time
from time import time

# import custom module
import validator
from validator import validate_email

#today = datetime.date.today()

today = date.today()
print(today)

#timestamp = time.time()
timestamp = time()

print(timestamp)

# Exmaple of import
email = 'test@test.com'
if validate_email(email):
    print('Email is valid')
else:
    print('Sorry, email is bad!')

