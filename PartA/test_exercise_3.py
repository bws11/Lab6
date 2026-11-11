import pytest
from exercise_3 import find_common_elements

def test_common_elements():
    assert find_common_elements([1, 2, 3, 4], [3, 4, 19, 21, 5]) == [3, 4]
    assert find_common_elements([3, 3, 3], [4, 4, 4]) == []
    assert find_common_elements([3, 4, 5], [3, 4, 5]) == [3, 4, 5]
    assert find_common_elements([11, 10, 9, 23], [23, 11, 15]), [11, 23]
    assert find_common_elements([-11, 11, -9, 10, 8], [10, -3, 0, 14, 8, -9]) == [-9, 8, 10]

pytest.main()