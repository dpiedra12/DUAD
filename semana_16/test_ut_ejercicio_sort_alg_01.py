import pytest
from ut_ejercicio_sort_alg_01 import bubble_sort

def test_bubble_sort_order_a_small_list_correctly():

    #AAA
    #Arrange
    my_list = [1,20,3]

    #Act
    sorted_list = bubble_sort(my_list)

    #Assert
    assert sorted_list ==[1,3,20]


def test_bubble_sort_order_a_large_list_correctly():

    #AAA
    #Arrange
    my_list = [1, 12, 23, 34, 45, 56, 67, 78, 89, 100, 11, 22, 33, 44, 55, 66, 77, 88, 99, 10, 21, 32, 43, 54, 65, 76, 87, 98, 9, 20, 31, 42, 53, 64, 75, 86, 97, 8, 19, 30, 41, 52, 63, 74, 85, 96, 7, 18, 29, 40, 51, 62, 73, 84, 95, 6, 17, 28, 39, 50, 61, 72, 83, 94, 5, 16, 27, 38, 49, 60, 71, 82, 93, 4, 15, 26, 37, 48, 59, 70, 81, 92, 3, 14, 25, 36, 47, 58, 69, 80, 91, 2, 13, 24, 35, 46, 57, 68, 79, 90, 101, 102, 103, 104]
    my_list_sorted = list(range(1, 105))

    #Act
    sorted_list = bubble_sort(my_list)

    #Assert
    assert sorted_list == my_list_sorted


def test_bubble_sort_with_empty_list_returns_empty_list():

    #AAA
    #Arrange
    my_list = []

    #Act
    sorted_list = bubble_sort(my_list)

    #Assert
    assert sorted_list ==[]


def test_bubble_sort_with_invalid_parameter_type_raises_value_error():

    #AAA
    #Arrange
    new_parameter = {}

     # Act Assert
    with pytest.raises(ValueError):
        bubble_sort(new_parameter)

   