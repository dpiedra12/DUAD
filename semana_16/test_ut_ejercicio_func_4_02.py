from ut_ejercicio_func_4_02 import invert_string

def test_invert_string_with_empty_string_returns_empty_string():

    #AAA
    #Arrange
    new_string= ""

    #Act
    result = invert_string(new_string)

    #Assert
    assert result == ""


def test_invert_string_with_single_word_returns_inverted_word():

    #AAA
    #Arrange
    new_string = "Python"

    #Act
    result = invert_string(new_string)

    #Assert
    assert result == "nohtyP"


def test_invert_string_with_spaces_and_special_characters_returns_inverted_string():

    #AAA
    #Arrange
    new_string = "Hello, world!"

    #Act
    result = invert_string(new_string)

    #Assert
    assert result == "!dlrow ,olleH"