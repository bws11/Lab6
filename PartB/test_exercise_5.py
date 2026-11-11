import pytest
from exercise_5 import minimum

def test_min():
    assert minimum([4, 2, 7, 3]) == 2

pytest.main()