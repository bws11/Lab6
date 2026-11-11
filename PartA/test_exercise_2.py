import pytest
from exercise_2 import sort_characters

def test_sort_string():
    assert sort_characters("programming") == "aggimmnoprr"
    assert sort_characters("civic") == "cciiv"
    assert sort_characters("aabb") == "aabb"
    assert sort_characters("PaBaBB") == "aaBBBP"
    assert sort_characters("BaAaA") == "AAaaB"


pytest.main()