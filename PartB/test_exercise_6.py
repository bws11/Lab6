import pytest
from exercise_6 import total_sum

def test_sum():
    assert total_sum([1, 2, 3, 4]) == 10

pytest.main()