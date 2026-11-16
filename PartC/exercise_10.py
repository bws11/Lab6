def first(x):
    print("Starting first")
    second(x)

def second(x):
    print("Starting second")
    third(x)

def third(x):
    print("Starting third")
    try:
        result = 10 / x
        return result
    except:
        x += 1
        first(x)

first(0)

# The first run through will cause a zero division error
# then when x = 1 it will return result as 10