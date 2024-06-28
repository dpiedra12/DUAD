greater_number = 0
list_of_numbers = [1,2,3]

for num in list_of_numbers: 
    number = int(input("Please insert a number: " ))
    if(number > greater_number):
        greater_number = number
        
print(f"The greatest number is: {greater_number}" )
