from datetime import date


class User:
     
    def __init__(self, date_of_birth):
            self.date_of_birth = date_of_birth


    @property
    def age(self):
            #Calculates age from current date
            today = date.today()
            return (
                today.year
                - self.date_of_birth.year
                - (
                    (today.month, today.day)
                    < (self.date_of_birth.month, self.date_of_birth.day)
                )
            )


def validate_age(func):
    def wrapper(user,*args):
            
                if user.age< 18:
                                    
                    raise ValueError ("The user is not of legal age")  
                
                return func(user, *args)     

    return wrapper
    

@validate_age
def insert_age(user):
          
         print(f"Action performed for user {user.age} years old")


user = User(date(2006, 1, 1))
insert_age(user)



