def bubble_sort(list_numbers):

    for i in range(len(list_numbers)):
        for x in range(len(list_numbers)-1):
            if list_numbers[x]> list_numbers[x + 1]:
                temp = list_numbers[x]
                list_numbers[x] = list_numbers[x + 1]
                list_numbers [x+1] = temp


my_list = [10,20,11,1,2,3]
bubble_sort(my_list)
print (my_list)