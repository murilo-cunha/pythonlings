from context_managers3 import managed_list


def test_sorted_after_with():
    with managed_list() as lst:
        lst.append(3)
        lst.append(1)
        lst.append(2)
    assert lst == [1, 2, 3]
