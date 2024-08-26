#bubble_sort
def bubble_sort(list_numbers):

    for i in range(len(list_numbers)): # O(n)
        for x in range(len(list_numbers)-1): # O(n^2)
            if list_numbers[x]> list_numbers[x + 1]:  # O(1)
                temp = list_numbers[x]  # O(1)
                list_numbers[x] = list_numbers[x + 1]  # O(1)
                list_numbers [x+1] = temp  # O(1)


my_list = [10,20,11,1,2,3]
bubble_sort(my_list)
print (my_list)


#print_numbers_times_2
def print_numbers_times_2(numbers_list):
	for number in numbers_list: #O(n)
		print(number * 2) # O(1)
		
		
#check_if_lists_have_an_equal
def check_if_lists_have_an_equal(list_a, list_b):
	for element_a in list_a: #O(n)
		for element_b in list_b: # O(n^2)
			if element_a == element_b: # O(1)
				return True # O(1)
				
	return False # O(1)


#​print_10_or_less_elements
def print_10_or_less_elements(list_to_print):
	list_len = len(list_to_print) # O(1)
	for index in range(min(list_len, 10)): # O(1)
		print(list_to_print[index]) # O(1)


#generate_list_trios
def generate_list_trios(list_a, list_b, list_c):
	result_list = [] # O(1)
	for element_a in list_a: #O(n)
		for element_b in list_b: # O(n^2)
			for element_c in list_c: # O(n^3)
				result_list.append(f'{element_a} {element_b} {element_c}')  # O(1)
				
	return result_list  # O(1)