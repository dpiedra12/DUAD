user_name = input ("Insert the user name: ")
user_lastname = input ("Insert the lastname: ")
user_age = int (input("Insert the age: "))

if (user_age <= 5):
    print(f'The user {user_name} {user_lastname} is a baby')
elif ( user_age<=10):
    print (f'The user {user_name} {user_lastname}  is a boy')
elif (user_age<= 12 ):
    print (f'The user {user_name} {user_lastname}  is a pre-adolescent')
elif (user_age<= 17 ):
    print (f'The user {user_name} {user_lastname}  is an adolescent')
elif (user_age<= 24 ):
    print (f'The user {user_name} {user_lastname}  is a young adult')
elif (user_age<= 64 ):
    print (f'The user {user_name} {user_lastname}  is an  adult')
else:
    print (f'The user {user_name} {user_lastname}  is an  older adult')