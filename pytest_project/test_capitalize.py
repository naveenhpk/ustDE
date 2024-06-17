import pytest
def capital_case(x):
    if not isinstance(x,str):
        raise TypeError("Please enter the string as argument ")
    return x.capitalize()

def test_capital_case():
    # assert check with output and inpt
    assert capital_case("semaphore") == 'Semaphore'

def test_raise_exception_on_non_string_arguments():
    with pytest.raises(TypeError):
        capital_case(9)
