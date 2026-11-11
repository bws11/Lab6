import pytest
from exercise_4 import movie_ticket_price

def test_ticket_price():
    assert movie_ticket_price(-2, 5, 6, 2) == None
    assert movie_ticket_price(2, -5, 6, 2) == None
    assert movie_ticket_price(2, 5, -6, 2) == None
    assert movie_ticket_price(0, 1, 0, 10) == 14.25
    assert movie_ticket_price(2, 2, 0, 17) == 30
    assert movie_ticket_price(2, 2, 0, 13) == 28.5
    assert movie_ticket_price(2, 1, 1, 13) == 30.4
    #assert movie_ticket_price(3, 2, 1, 14) == 38.95
    #assert movie_ticket_price(3, 1, 2, 15) == 49
    #assert movie_ticket_price(4, 3, 2, 11) == 69.35



pytest.main()