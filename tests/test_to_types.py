from VK_education import tuple_check
import pytest
from VK_education import int_check


def test_check_adding_type_int():
    assert tuple_check(123) is tuple

def test_check_adding_type_str():
    assert tuple_check('test') == tuple

@pytest.mark.parametrize("expected_excepion", [(AssertionError)])
def test_wrong_type(expected_excepion):
    with pytest.raises(expected_excepion):
        assert tuple_check('123') is not tuple

def test_check_add_type_int():
    assert int_check(1) == int

def test_check_adding_text():
    try:
        assert int_check('test') == int
    except ValueError:
        print('Not int')

@pytest.mark.parametrize("item, expected_excepion", [('123', int)])
def test_check_string_to_integer(item, expected_excepion):
    assert int_check(item) == expected_excepion
