def print_parameter(func):
    def wrapper(*args):
        print (f"\nCalling the function '{func.__name__}' with the arguments: {args}\n")     
        result =  func(*args)    
              
        print(f"The function '{func.__name__}, returned {result}\n")

        return result
               
    return wrapper


@print_parameter
def get_parameter(name, lastname):
    
    return f"{name}, {lastname}"


get_parameter("Danny", "Piedra")


    