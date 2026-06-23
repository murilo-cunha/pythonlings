import pytest
from variables5 import hello_mutable_list


def test_list_mutation():
    assert hello_mutable_list[0] == "I WORK"

def test_list_join():
    assert "".join(hello_mutable_list) == "I WORKello"
