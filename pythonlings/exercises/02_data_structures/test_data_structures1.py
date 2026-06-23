from data_structures1 import my_list


def test_length():
    assert len(my_list) == 4

def test_first_element():
    assert my_list[0] == 1

def test_second_element():
    assert my_list[1] == "world"

def test_third_element():
    assert my_list[2] is False
