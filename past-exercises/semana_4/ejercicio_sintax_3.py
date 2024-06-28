secret_number = 3
number = int(input("Please insert a number: " ))

while (number != secret_number):
    print ("Please try again")
    number = int(input("Please insert a number: " ))

print ("You have guessed the secret number")