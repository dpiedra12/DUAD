my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9,10] 
even_numbers_list = []

for number in range (len(my_list)):
    num =  my_list [number]
    
    if num % 2 == 0:
        even_numbers_list.append(num)

print (even_numbers_list)