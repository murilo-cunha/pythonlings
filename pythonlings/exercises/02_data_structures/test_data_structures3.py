from data_structures3 import evens_only, both, all_nums


def test_evens_only():
    assert evens_only == {4, 6, 8, 10}

def test_both():
    assert both == {2}

def test_all_nums():
    assert all_nums == {2, 3, 4, 5, 6, 7, 8, 10, 11}
