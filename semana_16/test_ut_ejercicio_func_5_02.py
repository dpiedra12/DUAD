from ut_ejercicio_func_5_02 import count_uppercase_and_lowercase

def test_count_uppercase_and_lowercase_with_empty_string_returns_0_counts():

    #AAA
    #Arrange
    new_string= ""

    #Act
    result = count_uppercase_and_lowercase(new_string)

    #Assert
    assert result == "There’s 0 upper cases and 0 lower cases"


def test_count_uppercase_and_lowercase_with_uppercase_only_returns_correct_counts():

    #AAA
    #Arrange
    new_string = "PYTHON"

    #Act
    result = count_uppercase_and_lowercase(new_string)

    #Assert
    assert result == "There’s 6 upper cases and 0 lower cases"


def test_count_uppercase_and_lowercase_with_uppercase_lowercase_and_special_characters_returns_correct_counts():

    #AAA
    #Arrange
    new_string = "Python 3.8!"

    #Act
    result = count_uppercase_and_lowercase(new_string)

    #Assert
    assert result == "There’s 1 upper cases and 5 lower cases"
