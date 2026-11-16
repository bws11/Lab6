import pytest
from exercise_8 import find_first_even

def test_even_num():
    assert find_first_even([1, 3, 5, 6, 7, 8]) == 6
    assert find_first_even([1, 3, 5, 4, 7, 8]) == 4
    assert find_first_even([1, 3, 2, 6, 7, 8]) == 2
    assert find_first_even([1, 3, 5, 3, 2, 8]) == 2

pytest.main()