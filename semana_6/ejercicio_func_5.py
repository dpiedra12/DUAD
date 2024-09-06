def count_uppercase_and_lowercase(sentence):

    sentence_without_spaces = sentence.replace(' ', '')
    upper=0
    lower = 0

    for letter in sentence_without_spaces:
        
                if letter.islower():
                    lower += 1
                    
                else:
                    upper += 1
    
    print (f'There’s {upper} upper cases and {lower} lower cases')


count_uppercase_and_lowercase("Python 3.8!")