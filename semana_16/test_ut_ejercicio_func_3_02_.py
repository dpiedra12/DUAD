
from ut_ejercicio_func_3_02_ import sum_of_numbers

def test_sum_of_numbers_with_empty_list_returns_0():

    #AAA
    #Arrange
    list_of_numbers = []

    #Act
    result = sum_of_numbers(list_of_numbers)

    #Assert
    assert result == 0


def test_sum_of_numbers_with_negative_numbers_returns_correct_value():

    #AAA
    #Arrange
    list_of_numbers = [-3, -5, -7, 10]

    #Act
    result = sum_of_numbers(list_of_numbers)

    #Assert
    assert result == -5


def test_sum_of_numbers_with_one_number_returns_that_number():

    #AAA
    #Arrange
    list_of_numbers = [10]

    #Act
    result = sum_of_numbers(list_of_numbers)

    #Assert
    assert result == 10