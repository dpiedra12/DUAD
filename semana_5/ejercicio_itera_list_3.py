my_list =[1,2,3,4,5]

first_number = my_list[0] 
my_list [0] = my_list[-1]
my_list.pop(-1)
my_list.append(first_number)

print (my_list)