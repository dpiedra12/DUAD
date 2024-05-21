list_a = ['first_name', 'last_name', 'role']
list_b = ['Danny', 'Piedra', 'SysAdmin']
dictionary = {}

for index in range (len(list_a)):

    keys = list_a[index]
    value = list_b[index]

    dictionary [keys] = value

print (dictionary)