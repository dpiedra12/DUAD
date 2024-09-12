def invert_string(my_string):

    new_string= ""
    for letter in range(len (my_string)-1,-1,-1):
        letter = my_string[letter]
        new_string +=letter
    return new_string

word= invert_string("Hello, world!")
print (word)