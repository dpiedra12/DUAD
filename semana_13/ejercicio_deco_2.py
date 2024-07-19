def validate_number(func):
    def wrapper(*args):
        for num in args:

            if not isinstance(num, (int, float)):
                raise ValueError (f"{num} is not a number")  
            
        return func(*args)     
                
    return wrapper


@validate_number
def insert_number(num1, num2):
   print (f"The numbers {num1}, {num2} have been validated")


insert_number(1.2,"d")
