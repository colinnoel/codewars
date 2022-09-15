# Given an array of ones and zeroes, convert the equivalent binary value to an integer.

# Eg: [0, 0, 0, 1] is treated as 0001 which is the binary representation of 1.

# Examples:

# Testing: [0, 0, 0, 1] ==> 1
# Testing: [0, 0, 1, 0] ==> 2
# Testing: [0, 1, 0, 1] ==> 5
# Testing: [1, 0, 0, 1] ==> 9
# Testing: [0, 0, 1, 0] ==> 2
# Testing: [0, 1, 1, 0] ==> 6
# Testing: [1, 1, 1, 1] ==> 15
# Testing: [1, 0, 1, 1] ==> 11
# However, the arrays can have varying lengths, not just limited to 4.

def binary_array_to_number(arr):
    binary_value = 0
    #set variable for our return value
    binary_power = 0
    #increase this by 1, per iteration of the list
    for ones_and_zeroes in reversed(arr):
        if ones_and_zeroes == 0:
            #binary value += 0
            #if a binary term is 0, then we dont add anything.
            binary_power +=1
        else: 
            binary_value += 2**binary_power
            #if a binary term is 1, then add 2 to the power of the index of the list to our total, binary_value
            binary_power +=1
        
    return binary_value
        