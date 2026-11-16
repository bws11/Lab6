# First even number

def find_first_even(numbers: list) -> int | float | None:
    for num in numbers:
        if num % 2 == 0:
            return num    
    return None
        