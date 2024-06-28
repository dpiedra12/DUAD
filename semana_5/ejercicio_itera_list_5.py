high_number = 0
list_of_numbers = []
print ("Please insert 10 numbers\n")

for index in range (1,11,1):

    number = int(input(f'Insert number {index}: '))
    list_of_numbers.append(number)

    if number > high_number:
        high_number = number
    
print (f'{list_of_numbers}\n')
print (f'The highest number was: {high_number}')