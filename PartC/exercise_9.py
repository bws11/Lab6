# numbers = [10, 20, 30, 40]
# index = int(input("Enter an index number: "))
# divisor = int(input("Enter a divisor: "))
# result = numbers[index] / divisor
# print("Result:", result)

# Firstly, you get a ValueError because a word cannot be turned into an integer
# Secondly, you get an IndexError because the index inputted is larger than what the list holds
# Thirdly, you get a ZeroDivisionError because numbers cannot be divided by 0

# Modification of the program
# Turned this into a function because it would have to be repeated a lot
def main():
    index = int(input("Enter an index number: "))
    divisor = int(input("Enter a divisor: "))
    result = numbers[index] / divisor
    return index, divisor, result

numbers = [10, 20, 30, 40]
try:
    index, divisor, result = main()
except ValueError:
    print("The value you entered was not an integer, please re enter your answers")
    index, divisor, result = main()
except IndexError:
    print("The index value you entered was either too large or small. Use the range of 0-3")
    index, divisor, result = main()
except ZeroDivisionError:
    print("Please try not to divide numbers by zero.")
    index, divisor, result = main()
except:
    print("unexpected error")

print("Result:", result)

# Yes, you can use multiple execpt blocks to handle different errors
# Yes, you can handle all errors with a general except block