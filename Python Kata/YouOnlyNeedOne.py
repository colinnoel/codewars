# You will be given an array a and a value x. All you need to do is check whether the provided array contains the value.

# Array can contain numbers or strings. X can be either.

# Return true if the array contains the value, false if not.

def check(seq, elem):
    for item in seq:
        #loop through each item in the list
        if elem == item:
            return True
            #if we find a match, just prematurely end the loop and return true.
        else:
            pass
            #if we dont find a match, iterate towards the next item in the list
    return False
    #if after iterating through each item and there wasn't a match, then we must be false
