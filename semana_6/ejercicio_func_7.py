def is_prime_number(number):

     if number > 1:
     
     
        count =0
        index=2
        while index<number and count==0:
            result=number%index
                        
            if result==0:
                count+=1
            index+=1    

        if count==0:
            return True
        else:
            return False
            
     else:
        number <= 1
        return False      


def return_prime_numbers(list_of_numbers):
    new_list = []

    for number in list_of_numbers:
        if is_prime_number(number):
               new_list.append(number)
    return new_list    
    

list_of_prime_numbers = return_prime_numbers ([ 1, 4, 6, 7, 13, 19, 67])
print(list_of_prime_numbers)