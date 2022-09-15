# In this little assignment you are given a string of space separated numbers, and have to return the highest and lowest number.

# Examples
# Kata.HighAndLow("1 2 3 4 5");  // return "5 1"
# Kata.HighAndLow("1 2 -3 4 5"); // return "5 -3"
# Kata.HighAndLow("1 9 3 4 -5"); // return "9 -5"

# Notes
# All numbers are valid Int32, no need to validate them.
# There will always be at least one number in the input string.
# Output string must be two numbers separated by a single space, and highest number is first.

def high_and_low(numbers):
    #We are given one singular string with spaces as a delimeter.
    # 1. Use split() turn the big string into a list of smaller strings
    # 2. Use map() to convert the elements of the list to integers
    # 3. With this new list, find the max and min
    # 4. Return an F string with our max and min variables combined inside
    
    new_list = list(map(int,numbers.split()))

    maximum = max(new_list)
    minimum = min(new_list)
    
    return f"{maximum} {minimum}"
