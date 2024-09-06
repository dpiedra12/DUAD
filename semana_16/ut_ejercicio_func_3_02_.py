def sum_of_numbers(list_of_numbers):

    total=0
    for number in list_of_numbers:
            total+=number
    return total


result = sum_of_numbers([3,6,2,29])
print (result)