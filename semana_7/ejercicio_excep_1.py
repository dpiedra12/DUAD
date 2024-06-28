def validate_option ():
        try:
                 option = int (input ("\nSelect a option: "))
                 if option <1 or option< 7:
                  return option
                 else:
                    raise ValueError ("Invalid value, please insert a number.")
        except ValueError as ex:
                    print(f"Error:{ex}")
       

def convert_input_to_int(user_input):
        try:
            return int(user_input)
            
        except ValueError as ex:
            print (f"Error: There was an error converting this string to a number: {ex}")
        return False
            
            
        
def calculate_numbers (actual_number):

        while True:
                
                num =0
                result_sum = 0

                print ("")
                print ("1. Addition")
                print ("2. Subtraction")
                print ("3. Multiplication")
                print ("4. Division")
                print ("5. Delete result")
                print ("6. Exit")

                option  = validate_option ()

                if option == 1:
                        user_input = input("Insert a number: ")
                        number = convert_input_to_int(user_input) 
                        result_sum =   actual_number + number
                        actual_number = result_sum
                elif option == 2:
                        user_input = input("Insert a number: ")
                        number = convert_input_to_int(user_input) 
                        result_sum =   actual_number - number
                        actual_number = result_sum
                elif option == 3:
                        user_input = input("Insert a number: ")
                        number = convert_input_to_int(user_input)  
                        result_sum =   actual_number * number
                        actual_number = result_sum
                elif option == 4:
                        user_input = input("Insert a number: ")
                        number = convert_input_to_int(user_input)  
                        result_sum =   actual_number / number
                        actual_number = result_sum
                elif option == 5:
                                    actual_number = 0
                elif option == 6:
                        exit()
                print ("")
                print (f'Total: {actual_number}')

def main():
        try:
          calculate_numbers(0)
                    
        except Exception as ex:
            print (f"Error: An unexpected error ocurred: {ex}")


main()