list_of_keys = ['access_level', 'nam']
employee = {
    'nam': 'John', 
    'email': 'john@ecorp.com', 
    'access_level': 5, 
    'age': 28
    }

for label in list(employee.keys()):

    for index in range (len(list_of_keys)):
        title = list_of_keys[index]
            
        if (title == label):
            employee.pop (label)

print(employee)