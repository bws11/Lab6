import pytest
from exercise_1 import multiply

def test_multiply():
    # normal cases
    assert multiply(2, 5) == 10
    assert multiply(3, 4) == 12

    # Negative cases
    assert multiply(-4, 2) == -8
    assert multiply(-8, -6) == 48

    # Zero cases
    assert multiply(33, 0) == 0


pytest.main()